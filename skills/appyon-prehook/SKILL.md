---
name: appyon-prehook
description: Monta o pre-hook do carro da Appyon (Auraly) por script - avatar abre o pote de canela, despeja debaixo do tapete, entra no carro - com trechos sem som acelerados, som de cada ação preso ao quadro (pote, tapete, mão, porta), riser desde o 1º quadro, música Interstellar a 0,95x com tom alterado entrando no fim do riser, headline com bandeiras dos EUA, snap e flash branco de transição para o avatar falando, e níveis iguais aos da referência camada por camada. Também monta o vídeo completo de aquecimento (pre-hook + avatar falando ao volante, sem pausas, transição Heatwave Flash com finger snap e Interstellar contínua). Use quando o usuário disser "faz o pre-hook", "pre-hook do carro", "monta o pre-hook do Liam/Noah/Oliver", "refaz o pre-hook", "ajusta o snap", "som do pote", "vídeo de aquecimento", "vídeo completo", "junta o pre-hook com as falas".
---

# Pre-hook do carro (Appyon)

O pre-hook são os ~6 s sem fala antes do avatar falar. É ele que faz o vídeo viralizar: o que
segura a pessoa é o som de cada ação no quadro exato. Esta skill usa as regras gerais de som e de
níveis da `edicao-de-video` (base) e acrescenta o método da Appyon.

## Antes de começar
1. Leia `appyon-producao` (manual, seção 3) e o `criativo.md` da conta (`appyon-producao/contas/`).
2. Precisa dos takes do Flow (2 ou 3 versões da cena), do riser, do snap e da música do kit do David
   (`03. Kit de Produção (David)`): `riser_harm.wav`, `snap_ref.wav` (ou `snap_dedo.wav`),
   Interstellar. O exemplo pronto e o print da linha do tempo estão no mesmo kit.
3. Um vídeo por pasta, com `estado.py PASTA novo --conta auraly-manifestacao --formato prehook-carro`.

## Montar
1. Copie `receitas/prehook-carro.json` para a pasta do vídeo. Os exemplos que deram certo estão em
   `receitas/exemplo-aprovado-liam-v3.json` (aprovado pelo Pedro) e `exemplo-recente-noah-v5.json`.
2. **Cenas:** comece no primeiro movimento; trecho sem som acelerado (1,5x), trecho com som em 1x.
   Prefira o trecho em que imagem e som vêm do mesmo take. Pó ou líquido sem nuvem de poeira subindo:
   procure outro take antes de regerar.
3. **Mapa de sons:** liste cada ação visível e ache o som dela nos takes (espectrograma + RMS a cada
   0,05 s). No bloco `foley`, `ancora` é o estalo no arquivo do som e `ponto` é o quadro da ação na
   cena. Dois sons fortes com pelo menos 0,2 s entre si; nada sintético.
4. **Porta:** corte da entrada para o plano de fora com a porta JÁ fechada, com a batida no 1º quadro
   desse plano. Clipe de porta gerado à parte deu "entra 2x". Com porta batendo antes, use
   `snap_dedo.wav` (passa-alta, sem o grave), senão se ouvem "duas portas" e "sem snap".
5. **Snap e flash:** o flash branco começa ~0,17 s depois do corte, tem pico ~0,44 s e a headline
   some no branco. O snap cai no **pico do clarão** (corte + 0,42 s): `snap.ataque` negativo empurra
   o estalo para depois do corte (ex.: `snap_ref.wav` com `ataque` -0,42).
6. **Níveis** (Piloto pedrin, 2026-11-18, RMS de (L+R)/2): riser -40,7 antes do primeiro som,
   música -35,5, som de ação mais forte -19,2 de pico, snap -21,5 com o `snap_ref.wav`.
7. Rode: `python scripts/prehook.py receita.json`. O script imprime o ganho e o nível de cada camada
   contra o alvo: mostre essa tabela junto com o vídeo.

## Vídeo completo de aquecimento (pre-hook + avatar falando)
Modelo: o vídeo do Oliver editado pelo Pedro no CapCut em 2026-11-18, medido camada por camada.
Exemplo aprovado para replicar: `receitas/exemplo-liam-aquecimento-1.json`.
1. **Takes (Flow, conta com assinatura):** imagem do avatar ao volante, de frente, por body swap da
   foto de referência do carro com o blueprint (Nano Banana, 0 crédito). Os prompts saem do Gerador de
   animação da Appyon (Creative Hub): copy colada, fala Média + câmera Zoom in só no 1º take, o resto
   Rápido + Estático; movimentação "meu avatar dirige enquanto fala" nos dois campos; tom Sedutor;
   perfil de voz homem, místico, grave. Take 1 dividido em dois de 8 s (até antes de "Tomorrow" e a
   partir dele), os outros de 10 s. Omni 1.1 Flash, Elementos, 9:16, 720p, x1: 69 créditos.
   Mesma copy de outro avatar: reaproveite os prompts dele no projeto do Flow, só trocando a imagem.
2. **Confira cada take:** transcrição contra a copy e o ruído nas pausas. Pausa acima de -35 dB é
   ronco de motor (veio em quase todos os takes de 18/11): limpe com
   `scripts/denoise.py take.mp4 take_limpo.wav auto` (perfil automático, só abaixo de 3-4 kHz para não
   comer o "S") e aponte `"audio"` do take para o arquivo limpo. Frase repetida: `"trechos"` à mão.
   **Versão com outra roupa:** troca de roupa nas 3 fotos (agachado com o pote, ao volante de lado,
   ao volante de frente) e pre-hook novo (2 takes de 10 s); para outro avatar, body swap do blueprint
   nessas mesmas fotos. Cada take de pre-hook tem os sons em outro lugar: refaça o mapa de sons; se
   faltar a porta, use a batida de outro take do mesmo carro (`"arquivo"` do foley ≠ cena).
3. **Montar:** copie `receitas/aquecimento-carro.json` e a receita do pre-hook aprovado para a pasta;
   `python scripts/aquecimento.py receita.json`. O script:
   - roda o `prehook.py` sem música, sem snap e sem flash, terminando 0,47 s depois do corte para o
     volante (a headline fica até o branco);
   - corta as pausas de cada take pela energia da voz (pausa > 0,30 s vira corte seco; 0,10 s antes e
     0,18 s depois de cada bloco; 0,25 s antes da 1ª fala para o clarão descer);
   - põe a voz de todos os takes em -23 dB RMS (nível do Oliver);
   - clarão quente que fica branco (Heatwave Flash de ~0,5 s), pico na junção, e o finger snap
     (`snap_ref.wav`, -21,5) no pico do branco;
   - Interstellar do 22,68 s da faixa, 0,95x com tom alterado, -12 dB sobre o original, entrando em
     1,22 s com fade-in de 0,4 s e sem parar até o fim (no Oliver: -34 dB RMS sob a voz).
4. Confira: transcrição do vídeo final com a copy inteira, folha de contato da transição e LUFS
   integrado perto de -20 (Oliver: -20,5).
5. **Revisão de bug de IA (o Pedro faz em todo vídeo, faça antes dele):** folha a 6-8 quadros por
   segundo do pre-hook. Reprovam: despejo sem o tapete levantado ou tapete "aparecendo do nada",
   canela por cima do tapete, alguém atravessando a porta, mão deformada. Troque pelo mesmo momento de
   outro take ou gere de novo. Voz que muda num take: costuma vir com fundo de áudio diferente dos
   outros (sem o ruído de carro); gere 2 e fique com o de fundo igual.

## Depois
- `qa-de-criativo` com `--lufs` no valor da referência (não -14) e a checagem de sons de ação.
- Correção do usuário que vale para os próximos: `estado.py PASTA aprendizado edicao "..."`.
- Receita salva ao lado do vídeo, versão nova com sufixo (`_v2`, `_v3`); nada é sobrescrito.

## Guardrails
- Música de terceiros só com 0,95x e tom alterado (sem isso o Facebook derruba). O CapCut mostra
  "0.9X", mas a música medida no vídeo do Oliver está em 0,95x.
- Primeiro quadro nunca preto.
- Avatar não pode ficar igual a uma pessoa real.
