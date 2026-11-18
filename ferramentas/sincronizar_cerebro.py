r"""Copia para este repositório os arquivos da Appyon que vivem no Cérebro do Pedro.

O Cérebro do Pedro (pasta "Claude - Cérebro" no disco D) é a fonte: é lá que o manual, os prompts e o perfil da conta são
atualizados. Rode isto depois de mudar algum deles e faça o commit. Quem não tem o Cérebro (o time)
só recebe as cópias pelo repositório; sugestões voltam por conversa ou issue, não editando a cópia.

Uso: python ferramentas/sincronizar_cerebro.py [pasta do Cérebro]
"""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CEREBRO = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"D:\Claude - Cérebro")
A = CEREBRO / "docs" / "appyon"
P = REPO / "skills" / "appyon-producao"

COPIAS = {
    A / "producao.md": P / "manual" / "producao.md",
    A / "prompts.md": P / "manual" / "prompts.md",
    A / "processo.md": P / "manual" / "processo.md",
    A / "referencias.md": P / "manual" / "referencias.md",
    A / "contas" / "auraly-manifestacao" / "criativo.md": P / "contas" / "auraly-manifestacao" / "criativo.md",
}
PROIBIDO = ("senha:", "password:", "token:")   # trava: arquivo com credencial não sai do Cérebro
# O repositório é PÚBLICO desde 2026-11-18: links privados (gravações de call, Drive, projeto do CapCut) ficam só
# no Cérebro. Posts públicos de Instagram e TikTok podem ir.
import re
PRIVADO = re.compile(r"https?://(?:[\w.-]*\.)?(?:fathom\.video|drive\.google\.com|docs\.google\.com|capcut\.com)/\S+")

for de, para in COPIAS.items():
    texto = PRIVADO.sub("(link privado: no Cérebro do Pedro)", de.read_text(encoding="utf-8"))
    if any(p in texto.lower() for p in PROIBIDO):
        sys.exit(f"PAROU: {de.name} parece ter credencial. Tire do arquivo antes de sincronizar.")
    para.parent.mkdir(parents=True, exist_ok=True)
    mudou = not para.exists() or para.read_text(encoding="utf-8") != texto
    para.write_text(texto, encoding="utf-8")
    print(("atualizado " if mudou else "igual      ") + str(para.relative_to(REPO)))
