# Appyon | Manual de produção

> Fontes: calls de 2026-11-17 (manhã e tarde) com David e Rodrigo. Prompts em
> [prompts.md](prompts.md); links e calls em [referencias.md](referencias.md).

## Qual funil rodar: Manifestação
| | **Manifestação** (o quiz "Tarot Manifest") | Soulmate |
|---|---|---|
| Preço / comissão | US$ 20 → **US$ 15** por venda | US$ 10 → US$ 7 |
| Depois do clique | quiz + **VSL de 20 min** | quiz curto, ~2 min até o checkout |
| Vídeo de venda | **1:40 a 1:50**, estilo orgânico (no carro, em casa) | 30 a 40 s, muitos com tela dividida e gameplay |

**Decisão (2026-11-17): Manifestação.** Na hora de espionar, vídeo curto com tela dividida é
Soulmate. (Nas notas anteriores aparece "Solvete": era Soulmate mal transcrito.)

## As ferramentas e para que serve cada uma
| Etapa | Ferramenta | Observação |
|---|---|---|
| Prompt JSON (avatar, cenário) | Claude ou GPT | O David recomenda o Claude para gerar prompt |
| Imagens (avatar, blueprint, cenário, roupa) | **Flow** (Google) | Conta grátis tem 50 créditos e já dá para os vídeos de aquecimento; Pedro tem 4 mil+ créditos |
| Prompts de vídeo (takes, duração, velocidade, câmera) | **Gerador de animação da Appyon** | Central Appyon → Appyon Materiais → Creative Hub. Ele não gera o vídeo: devolve os prompts de cada take para colar no Flow. No futuro o Pedro passa essa base para o Claude gerar os prompts daqui |
| Vídeo (pre-hook e avatar falando) | **Flow**, modelo **Omni Flash**, modo Elementos (Ingredients) | Vídeo de venda de 1:40 gasta 200 a 250 créditos |
| Edição | **CapCut** | Receita abaixo; música e exemplo no Drive |

## 1. Avatar (uma vez por persona)
1. Referência no **TikTok**: homem de tarô com vários vídeos virais (100 mil a 800 mil por vídeo).
   Vale a aparência, não a qualidade dos vídeos dele.
2. Print de frame apresentável, de frente e de perto → prompt JSON → imagem no Flow (4 por vez).
3. Tatuagem no pescoço e cenário com elementos dos EUA (bandeira, bola de futebol americano).
4. Não pode ficar igual à pessoa real (regra da Appyon).
5. **Blueprint** de 8 vistas ([prompt](prompts.md#1-blueprint-do-avatar-flow-ou-gpt-com-a-imagem-do-avatar-anexada)).
   Daí em diante, toda imagem sai do blueprint.
6. Manter os avatares parecidos entre si: o formato que funciona em um funciona nos outros; o que
   muda entre eles é a roupa que combina.

Avatares do Pedro (2026-11-17), um por conta: **Liam Smith** (asiático, antes chamado de Japa), **Oliver
Smith** (cabelo ondulado) e **Noah Smith** (saiu de um erro de body swap na call; blueprint feito pelo
Claude no Flow em 2026-11-17, opção 1). Erros assim já deram
certo: o avatar mais vendedor do Rod (Jimmy) nasceu do mesmo jeito.

## 2. Imagens do vídeo (Flow)
1. **Cenário por body swap:** JSON da foto de referência + blueprint + foto de referência.
2. **Roupa:** "não mude nada na imagem, apenas a vestimenta do avatar" + foto da roupa.
3. **Tatuagem bugou:** remover todas → adicionar todas com base no blueprint.

## 3. Pre-hook do carro (o primeiro que se aprende)
Sequência: avatar abre o pote de canela → close dele despejando a canela debaixo do tapete do
carro e cobrindo com o tapete → entra pelo lado do motorista. Sem fala, áudio ASMR.
- Imagens: avatar com o pote (agachado na porta) + avatar dentro do carro.
- Gerar 2 ou 3 vídeos no Flow (Elementos, Omni Flash) e juntar o que ficou bom de cada um.

**Montagem no CapCut** (é o que faz viralizar):
1. Começar no **primeiro movimento** do avatar; cortar o início parado.
2. **Acelerar os trechos sem som** (ex.: até abrir o pote, levantar o tapete) e voltar à
   velocidade normal onde tem áudio, senão o áudio distorce.
3. **Realçar os sons satisfatórios (o mais importante para a retenção):** cada ação tem o seu som,
   no quadro exato: tampa do pote abrindo, tapete levantando, tapete caindo, mão alisando o tapete,
   porta batendo. O Flow costuma gerar esses sons baixos ou nenhum: extrair de um take não usado e
   sobrepor (skill `appyon-prehook`, repositório `criativos-appyon`, bloco `foley`). Dois sons
   fortes nunca no mesmo instante. Sem som real, deixar sem: nada de chiado sintético.
4. Cortar a entrada no carro a partir de quando a perna já está dentro; somar som de **porta
   batendo** (extraído de outro hook).
5. **Riser 01** (biblioteca do CapCut) desde o primeiro frame, volume **-12**.
6. **Música Interstellar** (arquivo no Drive): entra **no fim do riser (~1,9 s)**, baixa, por baixo
   dos sons de ação, como no "Piloto pedrin" do Pedro (2026-11-18). Isso substitui a correção de
   2026-11-17 ("não entra no pre-hook"). Começar em **0:23**,
   fade-in de 0,3 a 0,4 s, volume baixo de fundo, **velocidade 0,95x com "Alterar tom do áudio"
   ligado** (sem isso o Facebook derruba por direito autoral).
   O estalo da tampa tem que cair no quadro exato em que ela solta, bem alto.
7. Headline: **"It works so fast, it's scary"**.
8. Sticker da **bandeira dos EUA**.
9. **Finger snap** (biblioteca do CapCut) no fim do pre-hook + transição "Flash" sincronizada com o
   estalo para entrar no avatar falando.
10. Capa do vídeo nunca preta: primeiro frame preto faz a pessoa pular.
11. **Volume igual ao da referência, camada por camada** (medido no "Piloto pedrin", RMS de (L+R)/2):
    riser -40,7 dB antes do primeiro som, música -35,5, som de ação mais forte -19,2 de pico, snap
    -21,5 (RMS de 0,1 s do estalo de dedo da referência). Não normalizar o pre-hook para -14 LUFS.
12. **Corte** para o avatar no carro; o flash branco começa ~0,17 s depois, sobe devagar (~0,27 s)
    e a headline some no branco. É a ponte para o avatar falando. **O finger snap cai no pico do
    clarão** (corte + 0,42 s), não no corte: medido no Piloto pedrin em 2026-11-18. O som do snap é
    o recorte cru da referência (`docs/appyon/pre-hooks/snap_ref.wav`), no mesmo volume.

Pre-hook aprovado: `docs/appyon/pre-hooks/Liam_prehook-carro_v3.mp4` (takes do Flow de
2026-11-17), com a receita ao lado.

Exemplo pronto: `03. Kit de Produção (David)/Exemplos prontos`. Print da linha do tempo no mesmo kit.

## 4. Avatar falando (corpo do vídeo)
Atualizado com a call de 2026-11-18 e o vídeo do Oliver que o Pedro editou (`appyon_aquecimento_1.mp4`).

**Imagem:** avatar ao volante, de frente (câmera no painel), camiseta preta. Sai por body swap da foto
do Oliver ao volante com o blueprint do avatar (Nano Banana no Flow, 0 crédito).

**Prompts dos takes:** Central MVM Creators App → Creative Hub → **Gerador de animação**. Colar a copy
(trocar a data), velocidade de fala **Média** e câmera **Zoom in** (só valem para o 1º take),
movimentação "meu avatar dirige enquanto fala" (prompt nos materiais do Drive) colada **nos dois
campos** de movimentação, tom **Sedutor** (os outros tons geram voz inconsistente), perfil de voz
**homem, místico, grave**. Copy curta (aquecimento): o take 1 vira dois clipes de **8 s** (até antes
de "Tomorrow" em Média + Zoom in; a partir de "Tomorrow" em Rápido + Estático), tirando o enter e o
espaço que bugam o texto; os takes 2 a 4 em Rápido + Estático, **10 s**. Flow: Omni 1.1 Flash,
Elementos, 9:16, 720p (baixar em 720p; 1080p trava). Custo: 12 + 12 + 15 x 3 = **69 créditos** por
vídeo. A mesma copy em outro avatar reaproveita os prompts do projeto do Flow, só trocando a imagem.

**Edição (modelo do Oliver, medido camada por camada):**
1. Pre-hook **sem música própria**; o riser fica.
2. **Interstellar** numa faixa só, do 1,22 s até o fim: cortada em ~0:23 da faixa, volume **-12**,
   velocidade **0,95x com "Alterar tom" ligado** (o CapCut mostra "0.9X"; medido: 0,95), fade-in de 0,4 s.
   Sob a voz ela fica em ~-34 dB RMS.
3. Transição **Heatwave Flash** (Transitions → New), **0,6 s**, entre o hook e o 1º take: clarão quente
   que fica branco. **Finger snap** ("Fingersnap Patreon Reverberation") no meio da transição, no pico
   do branco.
4. **Cortar todas as pausas** em que o avatar não fala (Ctrl+B e Q/W no CapCut), inclusive dentro do
   take; se ele repetir uma frase, cortar a repetição. Take com voz ruim: gerar de novo com o mesmo prompt.
5. Voz no mesmo nível em todos os takes (~-23 dB RMS). Vídeo final ~40 s, ~-20 LUFS.

O Claude faz tudo isso por script: `appyon-prehook/scripts/aquecimento.py` (receita
`aquecimento-carro.json`). Primeiro vídeo assim: Liam, 2026-11-18
(`docs/appyon/aquecimento/Liam_aquecimento-1_carro.mp4`).

## 5. Aquecimento das páginas (os primeiros 10 vídeos de cada conta)
- **30 vídeos** no total (10 por avatar). Começa em **2026-11-18 a partir das 16h**, ~**2 por dia por
  conta** no início.
- Copy única de aquecimento (doc "Copy de aquecimento" no Drive, ~28 s): tirar o CTA e fica ~15 s.
  Trocar a data ("If you're watching this on ...").
- Objetivo: aprender a produzir e **testar pre-hook, cenário e roupa**. Viralizar depende do hook,
  não da copy. Página que viraliza no aquecimento já chega à venda com 2 a 3 mil seguidores.
- Ao fim dos 10: pegar a combinação vencedora (cenário + roupa + pre-hook) e refazer o mesmo
  vídeo com a **copy de vendas** e o link.
- Repostar no TikTok e no YouTube.

## 6. Regras de página
- **Aviso de conteúdo feito com IA na página (bio/perfil)**, não no vídeo. Sem isso a página não
  sobe. O objetivo do realismo é parar o scroll, não enganar.
- Facebook: não mudar nome/foto da página até ter 4 ou 5 vídeos.

## Lição de casa de 2026-11-17 → sessão de 2026-11-18 às 11h
- **6 pre-hooks do carro**: 2 por avatar, um com a camisa preta básica (padrão) e um com uma camisa
  diferente (só a camisa muda). Salvar em `04. Produção/Pre-hooks`.
- ~~Blueprint do Noah Smith~~ (feito em 2026-11-17, Nano Banana 2.1 no Flow, a partir do recorte do rosto).
- 2026-11-18 às 11h, com o David: montar os vídeos de aquecimento completos e aprender o pre-hook
  da gaveta.

## Referência de resultado (2026-11-17)
David ~970 e Rod ~2 mil no dia (moeda não dita). O Jimmy do Rod vendeu 11 a 12 num dia.
