"""Tira ronco de motor/ambiente constante de um take do Flow por subtração espectral.

Uso: python denoise.py take.mp4 take_limpo.wav [pausas|auto] [over=2.0] [floor=0.08]
  pausas: "ini:fim,ini:fim" (s) com só ronco, sem fala. "auto" (padrão) usa os 15% de quadros
  com menos energia na faixa da voz como perfil do ruído.
Aprovado pelo Pedro no take 2 do Liam (2026-11-18): pausas de -24 para -45 dB, voz intacta.
Só atua abaixo de 3-4 kHz: limpar a faixa toda comia o "S" de "Save" (whisper ouvia "Leave").
"""
import sys, subprocess, wave
import numpy as np
SR = 48000
N, HOP = 2048, 512


def ler(p):
    return np.frombuffer(subprocess.check_output(["ffmpeg", "-v", "error", "-i", p, "-ac", "2", "-ar", str(SR),
                                                  "-f", "f32le", "-"]), np.float32).reshape(-1, 2).copy()


def stft(s, win):
    n = 1 + (len(s) - N) // HOP
    return np.array([np.fft.rfft(win * s[i * HOP:i * HOP + N]) for i in range(n)])


def istft(S, L, win):
    out, ws = np.zeros(L), np.zeros(L)
    for i, F in enumerate(S):
        out[i * HOP:i * HOP + N] += win * np.fft.irfft(F, N)
        ws[i * HOP:i * HOP + N] += win ** 2
    return out / np.maximum(ws, 1e-6)


def main():
    x = ler(sys.argv[1])
    modo = sys.argv[3] if len(sys.argv) > 3 else "auto"
    over = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
    floor = float(sys.argv[5]) if len(sys.argv) > 5 else 0.08
    win = np.hanning(N)
    f = np.fft.rfftfreq(N, 1 / SR)
    banda = (f > 250) & (f < 4000)
    Sm = stft(x.mean(axis=1).astype(np.float64), win)
    if modo == "auto":
        ev = (np.abs(Sm[:, banda]) ** 2).sum(axis=1)
        idx = np.where(ev <= np.percentile(ev, 15))[0]
    else:
        pausas = [tuple(map(float, s.split(":"))) for s in modo.split(",")]
        idx = [i for i in range(len(Sm)) if any(a * SR <= i * HOP and i * HOP + N <= b * SR for a, b in pausas)]
    y = np.zeros_like(x)
    k = np.ones(5) / 5
    for c in range(2):
        S = stft(x[:, c].astype(np.float64), win)
        mag = np.abs(S)
        ruido = mag[idx].mean(axis=0)
        g = np.maximum(1 - over * ruido / (mag + 1e-12), floor)
        g = np.apply_along_axis(lambda v: np.convolve(v, k, mode="same"), 0, g)
        # o ronco fica abaixo de ~3 kHz: acima disso não mexe, para não comer o "s" e o "f" das falas
        mistura = np.clip((f - 3000) / 1000, 0, 1)
        g = g * (1 - mistura) + mistura
        y[:, c] = istft(S * g, len(x), win)
    with wave.open(sys.argv[2], "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(y, -1, 1) * 32767).astype("<i2").tobytes())


if __name__ == "__main__":
    main()
