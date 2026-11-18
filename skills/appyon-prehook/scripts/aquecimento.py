"""Monta o vídeo completo de aquecimento da Appyon: pre-hook do carro + avatar falando ao volante.

Uso: python aquecimento.py receita.json [saida.mp4]

Modelo: o vídeo do Oliver que o Pedro editou no CapCut em 2026-11-18 (appyon_aquecimento_1.mp4),
medido quadro a quadro e camada por camada:
- Pre-hook do carro SEM música própria (a música é uma faixa só, do 1,2 s até o fim do vídeo).
- Transição "Heatwave Flash" de ~0,6 s entre o último plano do pre-hook e o 1º take: clarão quente
  que fica branco (pico ~0,45 s depois do corte para o volante) e desce já no avatar falando.
- Finger snap no meio da transição, no pico do branco.
- Takes do avatar falando em sequência, SEM as pausas em que ele não fala (corte seco dentro do take).
- Interstellar a 0,95x com o tom alterado (asetrate), -12 dB sobre o original, entrando em 1,22 s com
  fade-in de 0,4 s e sem parar até o fim. No Oliver a música medida dá -34 dB RMS sob a voz.
- Voz de cada take no mesmo nível (no Oliver, ~-23 dB RMS de (L+R)/2 no corpo).

Receita (caminhos relativos à pasta da receita):
{
  "prehook": {"receita": "prehook.json"},      # receita do prehook.py; aqui ele sai sem música, snap e flash
  "takes": [                                    # em ordem de fala
    {"arquivo": "take1a.mp4", "auto": true},    # auto: corta as pausas pela energia da voz
    {"arquivo": "take2.mp4", "trechos": [[0.5, 3.2], [3.6, 7.4]]},  # ou trechos à mão (s no arquivo)
    {"arquivo": "take3.mp4", "auto": true, "audio": "take3_limpo.wav"}  # áudio limpo (denoise.py)
  ],
  # Take com ronco de motor alto (pausas acima de -35 dB): limpe com
  #   python denoise.py take.mp4 take_limpo.wav "ini:fim,ini:fim"   (trechos só de ronco, sem fala)
  # ou gere o take de novo no Flow.
  "fala": {"rms": -23.0, "filtro": "highpass=f=80", "antes": 0.10, "depois": 0.18,
           "pausa_max": 0.30, "primeiro_antes": 0.25},
  "transicao": {"apos_corte": 0.47, "sobe": 0.27, "segura": 0.06, "desce": 0.17},
  "snap": {"arquivo": "snap_ref.wav", "ataque": 0.01, "pico": -21.5},
  "musica": {"arquivo": "interstellar.mp3", "inicio": 22.68, "fator": 0.95, "entra": 1.22,
             "fade_in": 0.4, "ganho_db": -12},
  "resolucao": [1080, 1920], "saida": "aquecimento.mp4"
}
"""
import json
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from prehook import SR, ler, rms_db, pico_db, fade, dur, run  # noqa: E402


def energia(x, passo=0.02):
    m = x.mean(axis=1).astype(np.float64)
    n = int(passo * SR)
    k = len(m) // n
    e = (m[: k * n].reshape(k, n) ** 2).mean(axis=1)
    return 10 * np.log10(e + 1e-12)


def trechos_auto(arquivo, cfg, primeiro):
    """Acha os blocos de fala pela energia na faixa da voz (250 Hz a 4 kHz, que ignora o ronco do
    motor que o Flow às vezes gera). Pausa maior que pausa_max vira corte.
    Não use as palavras do whisper para isso: ele estica a palavra por cima do silêncio."""
    x = ler(arquivo, filtro="highpass=f=250,highpass=f=250,lowpass=f=4000")
    e = energia(x)
    piso, fala = np.percentile(e, 10), np.percentile(e, 95)
    on = e > piso + cfg.get("limiar", 0.3) * (fala - piso)
    T = len(x) / SR
    blocos, i = [], 0
    while i < len(on):
        if on[i]:
            j = i
            while j < len(on) and on[j]:
                j += 1
            if blocos and i * 0.02 - blocos[-1][1] <= cfg.get("pausa_max", 0.30):
                blocos[-1][1] = j * 0.02
            else:
                blocos.append([i * 0.02, j * 0.02])
            i = j
        else:
            i += 1
    blocos = [b for b in blocos if b[1] - b[0] >= 0.10]
    out = []
    for bi, (a, b) in enumerate(blocos):
        antes = cfg.get("primeiro_antes", 0.25) if (primeiro and bi == 0) else cfg.get("antes", 0.10)
        out.append([max(0.0, a - antes), min(T, b + cfg.get("depois", 0.18))])
    # trechos que se encostam depois das folgas viram um só
    final = []
    for s in out:
        if final and s[0] <= final[-1][1] + 0.05:
            final[-1][1] = max(final[-1][1], s[1])
        else:
            final.append(s)
    return [[round(a, 3), round(b, 3)] for a, b in final]


def main():
    rp = Path(sys.argv[1]).resolve()
    base = rp.parent
    R = json.loads(rp.read_text(encoding="utf-8"))
    out = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else base / R.get("saida", "aquecimento.mp4")
    W, H = R.get("resolucao", [1080, 1920])
    tmp = Path(tempfile.mkdtemp(prefix="aquec_"))
    TR = {"apos_corte": 0.47, "sobe": 0.27, "segura": 0.06, "desce": 0.17}
    TR.update(R.get("transicao", {}))
    FL = {"rms": -23.0, "filtro": "highpass=f=80", "antes": 0.10, "depois": 0.18, "pausa_max": 0.30,
          "primeiro_antes": 0.25}
    FL.update(R.get("fala", {}))

    # 1. pre-hook sem música, sem snap e sem flash; termina no meio da transição
    prp = (base / R["prehook"]["receita"]).resolve()
    P = json.loads(prp.read_text(encoding="utf-8"))
    P.pop("musica", None)
    P.pop("snap", None)
    P["flash"] = {**P.get("flash", {}), "alpha": 0.0, "comeca": TR["apos_corte"] - 0.03,
                  "pico": TR["apos_corte"] - 0.02, "segura": 0.04}
    P["final_apos_corte"] = TR["apos_corte"]
    tmp_rec = prp.parent / "_aquec_prehook.json"
    tmp_rec.write_text(json.dumps(P, ensure_ascii=False, indent=1), encoding="utf-8")
    hook = tmp / "hook.mp4"
    run(sys.executable, AQUI / "prehook.py", tmp_rec, hook)
    tmp_rec.unlink()
    J = dur(hook)   # junção = pico da transição

    # 2. takes: trechos de fala, cada take no mesmo nível de voz
    vparts, apart, log = [hook], [], []
    for k, tk in enumerate(R["takes"]):
        arq = base / tk["arquivo"]
        som = base / tk["audio"] if tk.get("audio") else arq   # áudio limpo à parte (ex.: ronco tirado)
        if tk.get("trechos"):
            tr = tk["trechos"]
        else:
            tr = trechos_auto(som, FL, primeiro=(k == 0))
        auds = [fade(ler(som, a, b, filtro=FL.get("filtro")), 0.006, 0.012) for a, b in tr]
        juntos = np.concatenate(auds) if auds else np.zeros((1, 2), np.float32)
        ganho = FL["rms"] - rms_db(juntos) + tk.get("db", 0)
        apart.append(juntos * (10 ** (ganho / 20)))
        for i, (a, b) in enumerate(tr):
            n = tmp / f"t{k:02d}_{i:02d}.mp4"
            vf = (f"trim={a}:{b},setpts=PTS-STARTPTS,fps=30,scale={W}:{H}:force_original_aspect_ratio=increase,"
                  f"crop={W}:{H},setsar=1")
            run("ffmpeg", "-v", "error", "-y", "-i", arq, "-vf", vf, "-an", "-c:v", "libx264", "-preset",
                "medium", "-crf", "16", n)
            vparts.append(n)
        log.append(f"take {k + 1} {tk['arquivo']}: {len(tr)} trecho(s) {tr}  voz {ganho:+.1f} dB "
                   f"-> {rms_db(apart[-1]):.1f}  ({sum(b - a for a, b in tr):.2f}s)")
    lst = tmp / "lista.txt"
    # o hook tem áudio; os pedaços não. Concatena só a imagem.
    hv = tmp / "hook_v.mp4"
    run("ffmpeg", "-v", "error", "-y", "-i", hook, "-an", "-c:v", "copy", hv)
    vparts[0] = hv
    lst.write_text("".join(f"file '{p.as_posix()}'\n" for p in vparts), encoding="utf-8")
    junto = tmp / "junto.mp4"
    run("ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", junto)
    T = dur(junto)

    # 3. som: hook + voz + música contínua + snap no pico do clarão
    n_total = int(T * SR) + SR
    mix = np.zeros((n_total, 2), np.float32)
    rel = []

    def soma(x, em, nome):
        i = int(round(em * SR))
        if i < 0:
            x, i = x[-i:], 0
        j = min(n_total, i + len(x))
        mix[i:j] += x[:j - i]
        rel.append(f"{nome:10s} em {em:6.2f}s  pico {pico_db(x):6.1f}  rms {rms_db(x):6.1f}")

    soma(ler(hook), 0.0, "pre-hook")
    soma(np.concatenate(apart), J, "voz")
    M = R.get("musica")
    if M:
        f = M.get("fator", 0.95)
        entra, ini = M.get("entra", 1.22), M.get("inicio", 23)
        x = ler(base / M["arquivo"], ini, ini + (T - entra) * f + 0.5, fator=f)[: int((T - entra) * SR)]
        x = fade(x, M.get("fade_in", 0.4), 0.3) * (10 ** (M.get("ganho_db", -12) / 20))
        soma(x, entra, "musica")
    S = R.get("snap")
    pico_branco = J - TR["segura"] / 2
    if S:
        x = ler(base / S["arquivo"])
        x = fade(x, 0.0, 0.05) * (10 ** ((S.get("pico", -21.5) - pico_db(x)) / 20))
        soma(x, pico_branco - S.get("ataque", 0.01), "snap")
    mix = mix[: int(T * SR)]
    lim = 10 ** (-1 / 20)
    if np.abs(mix).max() > lim:
        g = np.minimum(1.0, lim / (np.abs(mix).max(axis=1) + 1e-9))
        g = np.convolve(g, np.ones(240) / 240, mode="same")
        mix = np.clip(mix * np.minimum(1.0, g)[:, None], -lim, lim)
    wav = tmp / "som.wav"
    with wave.open(str(wav), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(mix, -1, 1) * 32767).astype("<i2").tobytes())

    # 4. clarão quente que fica branco, centrado na junção
    s0 = J - TR["segura"] / 2 - TR["sobe"]
    s1 = J - TR["segura"] / 2
    s2 = J + TR["segura"] / 2
    vfx = (f"color=c=0xFFB59A:s={W}x{H}:r=30:d={T:.3f},format=rgba,colorchannelmixer=aa=0.55,"
           f"fade=t=in:st={s0:.3f}:d={TR['sobe'] * 0.6:.3f}:alpha=1,"
           f"fade=t=out:st={s2:.3f}:d={TR['desce']:.3f}:alpha=1[q];"
           f"color=c=white:s={W}x{H}:r=30:d={T:.3f},format=rgba,colorchannelmixer=aa=0.95,"
           f"fade=t=in:st={s0 + TR['sobe'] * 0.35:.3f}:d={TR['sobe'] * 0.65:.3f}:alpha=1,"
           f"fade=t=out:st={s2:.3f}:d={TR['desce']:.3f}:alpha=1[b];"
           f"[0:v][q]overlay=0:0:shortest=1[v1];[v1][b]overlay=0:0:shortest=1,format=yuv420p[vout]")
    run("ffmpeg", "-v", "error", "-y", "-i", junto, "-i", wav, "-filter_complex", vfx, "-map", "[vout]",
        "-map", "1:a", "-t", f"{T:.3f}", "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-c:a", "aac",
        "-ar", str(SR), "-b:a", "256k", "-movflags", "+faststart", out)
    print("\n".join(log))
    print("\n".join(rel))
    print(f"junção (pico do clarão) {J:.2f}s | clarão {s0:.2f}-{s2 + TR['desce']:.2f}s | "
          f"snap {pico_branco:.2f}s")
    print("ok", out.name, round(dur(out), 2), "s")


if __name__ == "__main__":
    main()
