# Marca Agrobiozone — como usar em qualquer projeto

> **Fonte da verdade da marca Agrobiozone.** Use daqui; nunca redesenhe cor, logo ou fonte.
> A proveniência de cada arquivo está em `PROVENANCE.md`.

## O caminho mais curto: 1 linha

```html
<link rel="stylesheet"
      href="https://cdn.jsdelivr.net/gh/PetersonGardin/agrobiozone-brand@main/brand.css">
```

Pronto — as cores e o gradiente da marca passam a existir na página, como variáveis CSS.

Para um logo, mesma ideia:

```html
<img src="https://cdn.jsdelivr.net/gh/PetersonGardin/agrobiozone-brand@main/logo/mista/logo-mista-horizontal-claro.svg"
     alt="Agrobiozone">
```

⚠️ **As fontes NÃO estão aqui.** HeadingNow e HeadingPro são comerciais e não podem ser
redistribuídas em repositório público. Sem elas o `brand.css` cai no fallback (`system-ui`) — o
layout continua certo, só a tipografia não é a da marca. Quem tem a licença põe os `.ttf` numa
pasta `fonts/` do próprio projeto, ao lado de uma cópia do `brand.css`.


## As cores — as 4 oficiais

```
#00AFEF   cyan            primária      Pantone Process Cyan C
#95C949   verde claro     secundária    Pantone P 157-8 C
#54B952   verde médio                   Pantone P 151-8 C
#079D50   verde escuro    destaque      Pantone P 145-16 C
```

Neutros de apoio, para UI clara:

```
#0f2e22   tinta           texto principal (viés verde, não preto puro)
#5b7268   tinta 2         texto secundário e labels
#e3eae6   linha           bordas e separadores
#f5f8f6   fundo           fundo de página
#ffffff   card            cartões
```

Gradiente da marca (o do wordmark): `#00AFEF → #54B952 → #079D50`, 90°.

**Usando o CSS:** `var(--abz-cyan)`, `var(--abz-verde-escuro)`, `var(--abz-gradiente)`…

---

## As fontes

```
HeadingNow   títulos, wordmark, números fortes    var(--abz-font-titulo)
HeadingPro   corpo de texto e labels              var(--abz-font-texto)
```

⚠️ **HeadingNow é fonte de DISPLAY.** Em corpo de texto pequeno ela cansa a leitura — use no título
e deixe o corpo com HeadingPro. Esse erro já foi cometido no MVPG.

Os arquivos `.ttf` **não estão neste repositório** (licença comercial). Peça ao Peterson — ele os
mantém no OneDrive da empresa. O `brand.css` já declara os 4 pesos que a UI usa: basta pôr os
arquivos numa pasta `fonts/` ao lado dele.

---

## Qual logo escolher

```
logo/mista/          símbolo + nome     o uso padrão, quando há espaço
logo/figurativa/     só o símbolo       avatar, favicon, espaço apertado
logo/nominativa/     só o nome          quando o símbolo já apareceu na página
```

Cada um tem versão **clara** (para fundo claro) e **escura** (para fundo escuro), e a mista vem
**horizontal** e **vertical**.

**Prefira sempre o `.svg`** — escala sem perder qualidade. Os `.png` existem para onde SVG não entra.

```
pattern/pattern-campo.png    textura de apoio para fundo de arte
paleta/paleta-cores.jpg      a paleta impressa, para conferência visual
```

---

## Regras que não se quebram

```
NÃO   recolorir o logo, esticar, girar ou aplicar sombra
NÃO   colocar a versão clara sobre fundo escuro (e vice-versa)
NÃO   inventar cor "parecida" — as 4 acima são as que existem
SIM   dar respiro em volta do logo, no mínimo a altura do símbolo
```

---

## Se a marca mudar

Este repositório é a fonte. Altere aqui, e depois sincronize a cópia local do MVPG
(`app/static/brand/`) — ela existe para o sistema não depender de rede para servir o próprio logo.

---

## Quem usa

```
mvpg                  a plataforma de vendas (cópia local, por causa do deploy)
agrobiozone.com.br    o site público
análise preditiva
```
