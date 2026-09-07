# Proveniência dos assets de marca (spec 033)

Origem: `sdr-agrobiozone/` (repo legado, só leitura). Todo asset abaixo foi copiado — não editado —
do legado; checksums conferem no momento da migração (01/jul/2026). `brand.css` é o espelho canônico
(não editar).

| asset (MVPG) | origem (sdr-agrobiozone) | md5 | tipo | fundo |
|---|---|---|---|---|
| `brand.css` | `brand/brand.css` | `ea1571707f6541871fd6c60e96f4acb5` | css | — |
| `logo/mista/logo-mista-vertical-claro.svg` | `brand/logo/agrobiozone-logo.svg` | `d9d5550d115744ba3b42cb17aa667c89` | mista | claro |
| `logo/mista/logo-mista-vertical-claro.png` | `brand/logo/agrobiozone-logo.png` | `dc91e6e79f7cf057d0036b35a78baa0c` | mista | claro |
| `logo/mista/logo-mista-horizontal-claro.svg` | `3_Marketing/31 Logo e fontes da marca/SVGs/LOGO4-AGROBIOZONE-SVG.svg` | `9c923b42811f1db1220d4d2390e72b02` | mista | claro |
| `logo/mista/logo-mista-horizontal-claro.png` | `3_Marketing/31 Logo e fontes da marca/LOGO4-AGROBIOZONE.png` | `c550f0ae46f9a3d191116b76c44dfe36` | mista | claro |
| `logo/mista/logo-mista-vertical-escuro.svg` | `3_Marketing/31 Logo e fontes da marca/SVGs/LOGO2-AGROBIOZONE-SVG.svg` | `62de11dcb608ee7724ef40254da57fbb` | mista | escuro |
| `logo/mista/logo-mista-horizontal-escuro.svg` | `3_Marketing/31 Logo e fontes da marca/SVGs/LOGO5-AGROBIOZONE-SVG.svg` | `29e569ac48cffd507384eb96c2016ad1` | mista | escuro |
| `logo/figurativa/icone.svg` | `3_Marketing/31 Logo e fontes da marca/SVGs/ICONE2-AGROBIOZONE-SVG.svg` | `f3f816b9f3a221b56dc44753a8b5f74c` | figurativa | claro (arredondado — escolha do dono) |
| `logo/figurativa/icone.png` | `3_Marketing/31 Logo e fontes da marca/ICONE2-AGROBIOZONE.png` | `cd36dcb7870f2c52798af9dda1940909` | figurativa | claro |
| `logo/figurativa/icone-escuro.svg` | `3_Marketing/31 Logo e fontes da marca/SVGs/ICONE3-AGROBIOZONE-SVG.svg` | `e825701dc8542d341ff2479192ce5369` | figurativa | escuro |
| `logo/nominativa/wordmark-claro.png` | `3_Marketing/31 Logo e fontes da marca/TIPOGRAFIA1-AGROBIOZONE.png` | `cdb0f86592f332810b447901b64b2150` | nominativa | claro |
| `logo/nominativa/wordmark-escuro.png` | `3_Marketing/31 Logo e fontes da marca/TIPOGRAFIA2-AGROBIOZONE.png` | `175c0b25c2b88838d8a9f725215cec6f` | nominativa | escuro |
| `paleta/paleta-cores.jpg` | `3_Marketing/31 Logo e fontes da marca/paleta de cores.JPG` | `b9f426985b51ad5ec222165013b3e491` | paleta | — |
| `pattern/pattern-campo.png` | `3_Marketing/31 Logo e fontes da marca/PATTERN1-AGROBIOZONE.png` | `eedcd66c38770161a5e4f2b8741eb4bf` | pattern | — |
| `fonts/*.ttf` (10 arquivos) | `3_Marketing/31 Logo e fontes da marca/Fontes da Marca/*.ttf` | (ver spec 001) | fonte | — |

## Decisões registradas

- **Ícone figurativo:** escolhido o hexágono **arredondado** (ICONE2), não o pontudo (ICONE1) — decisão
  explícita do dono em 01/jul/2026.
- **Mista fundo escuro:** LOGO2/LOGO5 (não LOGO3), conforme o `README.md` do recorte curado do legado.

## Excluídos na migração (dedupe)

`.cdr` Corel (+ backup), PDFs vetoriais redundantes com os SVGs equivalentes, `LOGO1/LOGO3` e PNGs
escuros redundantes, `ICONE1` (pontudo, substituído por ICONE2), `logo.png` solto na raiz do marketing,
`LOGO-WORKSPACE` (baixa resolução), thumbnails `Marca *.jpg`/pasta INPI, assinaturas de e-mail, avatares
de rede social (o ícone SVG serve de avatar vetorial), pasta `FONTES/` duplicada (mantida só
`Fontes da Marca/`).
