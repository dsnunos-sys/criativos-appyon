---
name: appyon-producao
description: Manual de produção da Appyon (creators orgânicos do app Auraly nos EUA, funil Manifestação) - avatar e blueprint de 8 vistas no Flow, cenário por body swap, roupa, tatuagem, prompts prontos, pre-hook do carro, avatar falando pelo gerador de animação, aquecimento das páginas (10 vídeos por conta) e regras de página - mais o perfil criativo da conta auraly-manifestacao. Use em qualquer vídeo, roteiro, avatar ou página da Appyon/Auraly, ou quando o usuário disser "cria o avatar", "blueprint", "body swap", "troca a roupa", "vídeo de aquecimento", "copy de aquecimento", "manual da Appyon".
---

# Produção da Appyon

As skills da base (`criativos`) fazem o trabalho; esta skill diz **como a Appyon faz**. Leia antes de
qualquer etapa de um vídeo da Appyon.

## O que ler, e quando
| Arquivo | Quando |
|---|---|
| `manual/producao.md` | sempre: funil, ferramentas, avatar, imagens, pre-hook, avatar falando, aquecimento, regras de página |
| `manual/prompts.md` | ao gerar imagem ou vídeo: blueprint, cenário, roupa, tatuagem, vídeo |
| `manual/processo.md` | ao criar ou aquecer conta (manual, fora do Claude) |
| `manual/referencias.md` | vídeos de referência, material do David, calls |
| `contas/auraly-manifestacao/criativo.md` | voz, voz escrita, personagens, headline, o que não pode |

## Regras que não mudam
- **Toda imagem nova sai do blueprint**, nunca de outra imagem gerada (o rosto deriva).
- Vídeo no Flow: Omni Flash, modo Elementos; 2 ou 3 versões e o melhor trecho de cada uma. Em
  volume, use o modo lote (`geracao-de-video-ia`, `flow_lote.js`) e diga o custo antes.
- Pre-hook: skill `appyon-prehook`.
- Aviso de conteúdo feito com IA fica na página (bio), não no vídeo.
- Criação, aquecimento e verificação de conta são manuais: o Claude não cria conta nem digita senha.
- Planilha de contas tem credenciais: nunca copiar para arquivo, repositório ou conversa.

## De onde vêm estes arquivos
Cópias do Cérebro do Pedro, atualizadas por `ferramentas/sincronizar_cerebro.py`. Não edite a cópia:
sugestão de mudança vai para o Pedro (conversa ou issue no repositório).
