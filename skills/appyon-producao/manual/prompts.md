# Appyon | Prompts de produção

> Fonte: Drive "Materiais - Appyon" do David (2026-11-17) e call de 2026-11-17.
> Ordem de uso: blueprint (uma vez por avatar) → cenário → roupa → tatuagem (se bugar) → vídeo.

## Regra de ouro
**Toda imagem nova sai do blueprint**, nunca de outra imagem gerada. Cada geração "alucina" um
pouco; gerando em cima da anterior, em 10 imagens o avatar vira outra pessoa.

## 1. Blueprint do avatar (Flow ou GPT, com a imagem do avatar anexada)
Dica: se o rosto sair deformado ("gordo"), use uma imagem mais próxima do rosto como referência.
Se o Flow errar, teste no GPT.

```
Create a professional, photorealistic 8-view character reference sheet (Character Blueprint) using the uploaded image as the ONLY identity reference.

The goal is to transform the person in the uploaded image into a comprehensive, studio-quality character turnaround sheet, showing the exact same individual from multiple angles and distances.

IDENTITY AND CHARACTER CONSISTENCY:
Preserve the uploaded avatar's exact identity throughout all eight views. Maintain identical facial structure, face shape, eyes, eyebrows, nose, lips, skin tone, skin texture, hairstyle, hair color, hair length, hairline, body proportions, apparent age, and all distinctive physical characteristics, including every tattoo in the same position and design.

Do not beautify, reinterpret, redesign, or alter the person's appearance. Every panel must depict unmistakably the same individual. Facial identity consistency is the highest priority.

COMPOSITION AND LAYOUT:
Create one single vertical canvas with a clean, symmetrical, professional contact-sheet layout consisting of exactly 8 separate photographic views, organized into three horizontal sections:

TOP SECTION – 2 LARGE PORTRAITS:
- VIEW 01: Front-facing head-and-shoulders portrait. The avatar looks directly at the camera with a neutral, relaxed expression.
- VIEW 02: Strict 90-degree side-profile head-and-shoulders portrait, showing the avatar facing left.

MIDDLE SECTION – 2 LARGE PORTRAITS:
- VIEW 03: Strict 90-degree side-profile head-and-shoulders portrait, showing the avatar facing right.
- VIEW 04: Three-quarter facial portrait, approximately 45 degrees, showing the avatar looking slightly toward the camera.

BOTTOM SECTION – 4 FULL-BODY VIEWS:
- VIEW 05: Full-body frontal view, standing naturally, facing directly toward the camera.
- VIEW 06: Full-body strict 90-degree left-facing side profile.
- VIEW 07: Full-body strict 90-degree right-facing side profile.
- VIEW 08: Full-body rear view, showing the back of the avatar's head, hairstyle, clothing, and body proportions.

VISUAL PRESENTATION:
Use a minimalist, seamless, light gray or off-white studio background across all eight panels.
Use soft, evenly distributed professional studio lighting, realistic shadows, natural skin texture, and high-end commercial fashion photography quality.
The avatar must wear the same outfit, accessories, hairstyle, and makeup in every panel. If the uploaded image does not show the entire outfit, create a simple, understated outfit that complements the visible clothing, without changing the avatar's identity or introducing distracting elements.
For the full-body views, show the entire figure from head to feet, with arms naturally resting alongside the body and feet positioned naturally.
Maintain consistent camera perspective, lighting, exposure, color grading, and proportions across all panels.

GRID STRUCTURE AND LABELING:
- Top row: 2 equally sized, large portrait panels.
- Middle row: 2 equally sized, large portrait panels.
- Bottom row: 4 equally sized, narrower full-body panels.
- Separate each view with thin, subtle black or dark gray dividing lines.
- Below each panel, add a small, clean, centered label from "VIEW 01" to "VIEW 08" in a simple sans-serif font.
- No other text, logos, watermarks, or graphic elements.
```
*O original do David termina em "dividing"; o fim (das linhas divisórias em diante) e a frase
sobre tatuagens foram completados pelo Claude seguindo o padrão do blueprint do Liam.*

## 2. Cenário: pedir o JSON da foto de referência (no Claude ou no GPT, com a foto anexada)
```
Me envie o JSON EXATO do cenário e da postura do avatar. Não inclua características físicas nem legendas no prompt, apenas o cenário, acessórios e como o avatar está na foto. Eu tenho um avatar que quero inserir nesse cenário, dessa mesma forma, sem mudar nada, apenas trocando o avatar. Lembre-se de inserir roupas no prompt. Não insira tatuagens no prompt, vou preservar as tatuagens originais do meu avatar. Eu quero o PROMPT, não a imagem.
```
Depois, no Flow: colar o JSON + anexar o **blueprint** + anexar a **foto de referência** = body swap
(mesmo cenário, avatar trocado). Sem a foto de referência ele inventa um cenário novo (bom para
testar cenário). Gerar até ficar parecido com o avatar.

## 3. Trocar a roupa (Flow, anexando a imagem da roupa)
```
Agora o avatar está vestido assim. Não mude nada na imagem, apenas a vestimenta do avatar.
```
Roupa é o maior teste de viralização (mesmo vídeo: 5 mil views com uma camisa, 1 milhão com
outra). Camisa básica preta é a validada do David. Trocar só a camisa; calça fica.

## 4. Consertar tatuagem (quando a troca de roupa mistura tatuagens)
1. `Remova todas as tatuagens do avatar. Não mude mais nada na imagem.`
2. Anexar o blueprint: `Adicione todas as tatuagens do avatar baseada no blueprint. Não mude nada na imagem, só adicione as tatuagens.`

Nunca pedir para "adaptar" as tatuagens: ele mescla as de todo mundo. Tatuagem diferente entre
cenas do mesmo vídeo tira a credibilidade.

## 5. Vídeo do pre-hook do carro (Flow)
No Flow, modo **Elementos** (Ingredients) com o modelo **Omni Flash**. Anexar primeiro a imagem inicial (avatar com o
pote) e depois a do carro. Gerar 2 ou 3 vídeos e juntar as melhores partes no CapCut.
```
Meu avatar destampa o pote de canela em pó, depois, o vídeo vira um close-up shot dele despejando a canela em pó debaixo do tapete do carro e em seguida, botando o tapete por cima da canela em pó. Depois ele entra no carro pela porta do motorista e se prepara para dirigir. Ele não fala nada, o áudio é em ASMR. A primeira imagem anexada deverá ser o frame inicial.
```
Por que Elementos e não Frames: por frames o vídeo é obrigado a terminar no frame final e fica
engessado. Em Elementos a IA não sabe qual é o frame inicial, por isso a última frase do prompt.

## 6. Vídeo do avatar falando no carro (prompts no Gerador da Appyon, vídeo no Flow)
```
Meu avatar dirige enquanto fala. Ele gesticula com a mão que está livre baseado nas falas. Durante as falas, ele olha levemente para a frente, como se estivesse checando o trânsito para dirigir. O carro está sempre em movimento. O áudio sai com ruídos de carro, para simular que o avatar de fato está em movimento.
```
No Gerador de animação da Appyon: colar este prompt + a copy inteira (trocando a data). Ele devolve
os prompts de cada take com a duração; cada take é gerado no Flow com essa duração.
- **3 primeiros takes (hook): velocidade Média + Zoom in.** Falar mais devagar segura mais tempo
  de vídeo. (Devagar é para avatar mais velho.)
- **Resto (corpo): velocidade Rápida + Estática.** O espectador já está preso; falar rápido leva
  mais gente até o CTA.
- No Flow, modelo sempre **Omni Flash** (o mais barato e o melhor). Aviso do David: o Omni Flash
  1.1 e o Veo devem sair do ar em 2026-12-05; fica o 1.2, mais caro.

Onde fica o gerador de prompts: Central Appyon → Appyon Materiais → Creative Hub → Gerador de animação.
