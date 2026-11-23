# Guia de Prompts para Geração em Lote — Imagens Ilustrativas (Catálogo Assifarma 2026)

Este documento reúne todos os **25 placeholders de imagens ilustrativas panorâmicas (2 colunas)** presentes no Catálogo Oficial Assifarma 2026 (`INTERCRON / FORHEALTH`).
Cada prompt foi construído respeitando **estritamente a paleta de cores hexadecimal extraída da embalagem de cada produto**, garantindo harmonia visual absoluta com o cabeçalho, os boxes de destaque e o fundo da respectiva página.

---

## 1. Diretrizes Globais para Geração em Lote (Antigravity Gemini / GPT Codex)

- **Total de Imagens:** `25 banners horizontais panorâmicos`
- **Pasta de Destino Recomendada:** `/Users/joel/Documents/CATÁLOGO PDF/ASSIFARMA - CATÁLOGO/imagens_ilustrativas/`
- **Proporção / Resolução:** `1600 x 500 px` (ou geração nativa em `16:9` / `21:9` widescreen com recorte central suave `object-fit: cover` no card panorâmico).
- **Restrições Negativas Obrigatórias (Negative Prompt):** `Sem textos, sem tipografia, sem palavras escritas, sem rótulos de frascos, sem marcas d'água, sem logotipos, sem aparência de banco de imagens genérico.` (`No text, no typography, no letters, no bottle labels, no watermarks, no logos`).
- **Estilo Fotográfico Padronizado:** Fotografia editorial farmacêutica/nutracêutica de alto padrão combinada a elementos macro conceituais (cristais minerais, esferas lipídicas/vitamínicas translúcidas, fibras de colágeno, iluminação de estúdio com profundidade de campo suave `shallow depth of field`).

---

## 2. Tabela-Resumo das 25 Imagens e Paletas de Cores

| Pág. | Produto | Linha | Dimensão | Cor Principal | Tom Escuro | Tom Claro | Arquivo Sugerido | Conceito do Placeholder |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---|:---|
| **Pág. 06** | Borg Cálcio 500mg | Borg | `1600 x 500 px` | `#414795` | `#1d2043` | `#dbdef9` | `p06_borg_calcio_500mg.png` | Saúde Óssea, Fortalecimento Dental & Absorção Mineral |
| **Pág. 07** | Borg Feno Grego | Borg | `1600 x 500 px` | `#968243` | `#433a1e` | `#f9f2db` | `p07_borg_feno_grego.png` | Vigor Físico, Força & Metabolismo Ativo |
| **Pág. 08** | Borg Magnésio Dimalato | Borg | `1600 x 500 px` | `#146fb0` | `#09324f` | `#dbedf9` | `p08_borg_magnesio_dimalato.png` | Energia Muscular, Disposição & Redução do Cansaço |
| **Pág. 09** | Borg Magnésio P.A. | Borg | `1600 x 500 px` | `#1d77b1` | `#0d354f` | `#dbeef9` | `p09_borg_magnesio_p_a.png` | Equilíbrio Eletrolítico & Funcionamento Neuromuscular |
| **Pág. 10** | Borg Magnésio Treonato | Borg | `1600 x 480 px` | `#0969b4` | `#042f51` | `#dbecf9` | `p10_borg_magnesio_treonato.png` | Foco Cognitivo, Memória & Desempenho Mental |
| **Pág. 11** | Borg NAC 600mg | Borg | `1600 x 500 px` | `#32706b` | `#163331` | `#dbf9f7` | `p11_borg_nac_600mg.png` | Ação Antioxidante, Defesa Celular & Saúde Respiratória |
| **Pág. 15** | Carti Master Colágeno Tipo II + Ácido Hialurônico | Carti Master | `1600 x 480 px` | `#064d7c` | `#022237` | `#dbeef9` | `p15_carti_master_colageno_tipo_ii_acido_hialuronico.png` | Mobilidade Articular, Firmeza & Hidratação Tecidual |
| **Pág. 16** | Carti Master Condroitina + MSM | Carti Master | `1600 x 500 px` | `#b06637` | `#4f2e18` | `#f9e7db` | `p16_carti_master_condroitina_msm.png` | Flexibilidade Articular, Conforto & Movimento Ativo |
| **Pág. 17** | Carti Master Ultra | Carti Master | `1600 x 500 px` | `#c25d24` | `#572a10` | `#f9e6db` | `p17_carti_master_ultra.png` | Proteção Articular Avançada & Alívio do Desconforto |
| **Pág. 19** | Cronovit Cálcio | Cronovit | `1600 x 500 px` | `#149690` | `#094340` | `#dbf9f8` | `p19_cronovit_calcio.png` | Saúde Óssea, Fortalecimento Dental & Absorção Mineral |
| **Pág. 23** | Cronovit Vitamina E 400 UI | Cronovit | `1600 x 550 px` | `#118379` | `#073a36` | `#dbf9f7` | `p23_cronovit_vitamina_e_400_ui.png` | Proteção Celular Contra Danos dos Radicais Livres |
| **Pág. 24** | Cronoliv Cabelo, Pele e Unhas | Cronoliv | `1600 x 500 px` | `#a33681` | `#49183a` | `#f9dbf0` | `p24_cronoliv_cabelo_pele_e_unhas.png` | Nutrição Capilar, Unhas Fortes & Pele Radiante |
| **Pág. 25** | Cronoliv Colágeno Verisol® | Cronoliv | `1600 x 480 px` | `#604396` | `#2b1e43` | `#e6dbf9` | `p25_cronoliv_colageno_verisol.png` | Elasticidade da Pele, Síntese de Colágeno & Firmeza |
| **Pág. 26** | Cronoliv Própolis | Cronoliv | `1600 x 550 px` | `#c0880a` | `#563d04` | `#f9f0db` | `p26_cronoliv_propolis.png` | Defesa Imunológica Natural & Proteção Diária |
| **Pág. 27** | Nutrivix Coenzima Q10 | Nutrivix | `1600 x 450 px` | `#7a1c6b` | `#360c30` | `#f9dbf5` | `p27_nutrivix_coenzima_q10.png` | Antioxidante Celular, Vitalidade & Energia Mitocondrial |
| **Pág. 28** | Nutrivix Magnésio Dimalato | Nutrivix | `1600 x 500 px` | `#166d97` | `#093143` | `#dbf0f9` | `p28_nutrivix_magnesio_dimalato.png` | Energia Muscular, Disposição & Redução do Cansaço |
| **Pág. 29** | Nutrivix Magnésio Treonato | Nutrivix | `1600 x 480 px` | `#4d3b84` | `#221a3b` | `#e3dbf9` | `p29_nutrivix_magnesio_treonato.png` | Foco Cognitivo, Memória & Desempenho Mental |
| **Pág. 32** | Odessy Tempo | Odessy | `1600 x 480 px` | `#b35f50` | `#502b24` | `#f9e0db` | `p32_odessy_tempo.png` | Antienvelhecimento Celular & Renovação Vital |
| **Pág. 33** | Biomov Colágeno Tipo II + Ácido Hialurônico | Biomov | `1600 x 480 px` | `#3a1c6b` | `#1c0d33` | `#e7dbf9` | `p33_biomov_colageno_tipo_ii_acido_hialuronico.png` | Mobilidade Articular, Firmeza & Hidratação Tecidual |
| **Pág. 34** | Ceitil Acetilcisteína | Ceitil | `1600 x 500 px` | `#274f82` | `#11233a` | `#dbe9f9` | `p34_ceitil_acetilcisteina.png` | Defesa Respiratória, Fluidificação & Imunidade Fortalecida |
| **Pág. 35** | Complexo Prodiz Melatonina | Complexo Prodiz | `1600 x 500 px` | `#24296b` | `#111333` | `#dbdef9` | `p35_complexo_prodiz_melatonina.png` | Sono Reparador, Ciclo Circadiano & Relaxamento |
| **Pág. 36** | Epadose Colina | Epadose | `1600 x 500 px` | `#d1860a` | `#5e3c04` | `#f9eedb` | `p36_epadose_colina.png` | Metabolismo Lipídico, Saúde Hepática & Desintoxicação |
| **Pág. 37** | Laclaze Lactase 10.000 U.FCC | Laclaze | `1600 x 550 px` | `#5da1d0` | `#2a485d` | `#dbedf9` | `p37_laclaze_lactase_10_000_u_fcc.png` | Digestão Completa da Lactose & Conforto Digestivo |
| **Pág. 38** | Malosso Citrato Malato de Cálcio | Malosso | `1600 x 500 px` | `#075e8b` | `#032a3e` | `#dbeff9` | `p38_malosso_citrato_malato_de_calcio.png` | Absorção Otimizada de Cálcio com Alta Biodisponibilidade |
| **Pág. 39** | Naturedux Cromo | Naturedux | `1600 x 480 px` | `#aa683c` | `#4c2f1b` | `#f9e7db` | `p39_naturedux_cromo.png` | Controle Glicêmico & Metabolismo de Carboidratos e Gorduras |

---

## 3. Prompts Detalhados por Produto (PT-BR & EN)

### 01. [Pág. 06] Borg Cálcio 500mg
- **Linha:** Borg
- **Arquivo de Saída:** `imagens_ilustrativas/p06_borg_calcio_500mg.png`
- **Dimensão do Card:** `1600 x 500 px`
- **Conceito no Catálogo:** *Saúde Óssea, Fortalecimento Dental & Absorção Mineral*
- **Ativos Relacionados:** `Carbonato de Cálcio 500mg`
- **Paleta de Cores da Página:** Principal `#414795` • Escura `#1d2043` • Clara `#dbdef9` (Azul Índigo Profundo (#414795), Azul Noite (#1d2043) e Lavanda Gelo (#dbdef9))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 500 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Borg Cálcio 500mg" (Tema: Saúde Óssea, Fortalecimento Dental & Absorção Mineral). Fotografia editorial panorâmica de estilo de vida combinada com estética científica limpa: à esquerda, textura macro translúcida e luminosa remetendo à estrutura mineral óssea sadia e cristais puros de cálcio; à direita, em transição suave (bokeh), um adulto ativo caminhando ao ar livre sob luz matinal suave, transmitindo força estrutural, postura firme e saúde óssea. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Azul Índigo Profundo (#414795), Azul Noite (#1d2043) e Lavanda Gelo (#dbdef9). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 500 px aspect ratio) for "Borg Cálcio 500mg" (Theme: Saúde Óssea, Fortalecimento Dental & Absorção Mineral). Wide panoramic editorial lifestyle and clean scientific photography: on the left, luminous translucent macro mineral structure evoking strong bone matrix and pure calcium crystals; seamlessly blending on the right into a soft-focus active adult walking outdoors in gentle morning light, conveying structural strength, posture, and bone vitality. STRICT COLOR PALETTE GRADING: Deep Indigo Blue (#414795), Midnight Navy (#1d2043), and Ice Lavender (#dbdef9). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 02. [Pág. 07] Borg Feno Grego
- **Linha:** Borg
- **Arquivo de Saída:** `imagens_ilustrativas/p07_borg_feno_grego.png`
- **Dimensão do Card:** `1600 x 500 px`
- **Conceito no Catálogo:** *Vigor Físico, Força & Metabolismo Ativo*
- **Ativos Relacionados:** `Extrato de Semente de Feno Grego (Trigonella foenum-graecum L.) 300mg | Zinco Quelato • Vitamina B6`
- **Paleta de Cores da Página:** Principal `#968243` • Escura `#433a1e` • Clara `#f9f2db` (Dourado Oliva/Âmbar (#968243), Bronze Escuro (#433a1e) e Creme Dourado (#f9f2db))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 500 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Borg Feno Grego" (Tema: Vigor Físico, Força & Metabolismo Ativo). Composição panorâmica de alto padrão: close-up artístico de sementes naturais de feno-grego (Trigonella foenum-graecum) sobre superfície de pedra clara banhada por luz dourada quente, fundindo-se suavemente com a silhueta atlética e dinâmica de um adulto em treino funcional, simbolizando vigor físico, força muscular e metabolismo energético ativo. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Dourado Oliva/Âmbar (#968243), Bronze Escuro (#433a1e) e Creme Dourado (#f9f2db). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 500 px aspect ratio) for "Borg Feno Grego" (Theme: Vigor Físico, Força & Metabolismo Ativo). High-end wide panoramic composition: artistic macro close-up of natural fenugreek seeds (Trigonella foenum-graecum) on a warm stone surface bathed in golden light, blending smoothly into a dynamic athletic silhouette in functional training, symbolizing physical vigor, muscular strength, and active metabolism. STRICT COLOR PALETTE GRADING: Olive Gold / Warm Amber (#968243), Dark Bronze (#433a1e), and Golden Cream (#f9f2db). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 03. [Pág. 08] Borg Magnésio Dimalato
- **Linha:** Borg
- **Arquivo de Saída:** `imagens_ilustrativas/p08_borg_magnesio_dimalato.png`
- **Dimensão do Card:** `1600 x 500 px`
- **Conceito no Catálogo:** *Energia Muscular, Disposição & Redução do Cansaço*
- **Ativos Relacionados:** `Magnésio Dimalato 260mg`
- **Paleta de Cores da Página:** Principal `#146fb0` • Escura `#09324f` • Clara `#dbedf9` (Azul Oceano Vibrante (#146fb0), Azul Marinho Profundo (#09324f) e Azul Celeste Claro (#dbedf9))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 500 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Borg Magnésio Dimalato" (Tema: Energia Muscular, Disposição & Redução do Cansaço). Banner fotográfico panorâmico: adulto saudável em alongamento pós-treino ao amanhecer com expressão de energia renovada e zero fadiga, acompanhado por feixes sutis de luz azul-celeste e microcristais minerais translúcidos em primeiro plano, representando energia muscular, disposição diária e recuperação física. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Azul Oceano Vibrante (#146fb0), Azul Marinho Profundo (#09324f) e Azul Celeste Claro (#dbedf9). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 500 px aspect ratio) for "Borg Magnésio Dimalato" (Theme: Energia Muscular, Disposição & Redução do Cansaço). Wide panoramic photographic banner: healthy adult stretching post-workout at dawn with an expression of renewed energy and zero fatigue, accented by subtle sky-blue light trails and translucent mineral micro-crystals in the foreground, representing muscular energy, stamina, and physical recovery. STRICT COLOR PALETTE GRADING: Vibrant Ocean Blue (#146fb0), Deep Navy (#09324f), and Soft Sky Blue (#dbedf9). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 04. [Pág. 09] Borg Magnésio P.A.
- **Linha:** Borg
- **Arquivo de Saída:** `imagens_ilustrativas/p09_borg_magnesio_p_a.png`
- **Dimensão do Card:** `1600 x 500 px`
- **Conceito no Catálogo:** *Equilíbrio Eletrolítico & Funcionamento Neuromuscular*
- **Ativos Relacionados:** `Cloreto de Magnésio P.A. 260mg`
- **Paleta de Cores da Página:** Principal `#1d77b1` • Escura `#0d354f` • Clara `#dbeef9` (Azul Cobalto Médio (#1d77b1), Azul Petróleo Escuro (#0d354f) e Azul Gelo (#dbeef9))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 500 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Borg Magnésio P.A." (Tema: Equilíbrio Eletrolítico & Funcionamento Neuromuscular). Fotografia conceitual panorâmica de pureza mineral e equilíbrio: ondas fluidas de água cristalina e cristais puros de cloreto de magnésio refletindo luz azul-cobalto sobre fundo claro minimalista, com feixes sutis de impulsos luminosos que simbolizam o equilíbrio eletrolítico e o funcionamento neuromuscular perfeito. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Azul Cobalto Médio (#1d77b1), Azul Petróleo Escuro (#0d354f) e Azul Gelo (#dbeef9). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 500 px aspect ratio) for "Borg Magnésio P.A." (Theme: Equilíbrio Eletrolítico & Funcionamento Neuromuscular). Panoramic conceptual photography of mineral purity and balance: fluid waves of crystal-clear water and pure magnesium chloride crystals reflecting cobalt-blue light against a minimalist light background, with subtle luminous impulse trails symbolizing electrolyte balance and neuromuscular harmony. STRICT COLOR PALETTE GRADING: Medium Cobalt Blue (#1d77b1), Dark Teal Navy (#0d354f), and Ice Blue (#dbeef9). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 05. [Pág. 10] Borg Magnésio Treonato
- **Linha:** Borg
- **Arquivo de Saída:** `imagens_ilustrativas/p10_borg_magnesio_treonato.png`
- **Dimensão do Card:** `1600 x 480 px`
- **Conceito no Catálogo:** *Foco Cognitivo, Memória & Desempenho Mental*
- **Ativos Relacionados:** `Magnésio L-Treonato 260mg`
- **Paleta de Cores da Página:** Principal `#0969b4` • Escura `#042f51` • Clara `#dbecf9` (Azul Safira (#0969b4), Azul Profundo (#042f51) e Azul Claríssimo (#dbecf9))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 480 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Borg Magnésio Treonato" (Tema: Foco Cognitivo, Memória & Desempenho Mental). Composição panorâmica editorial de foco mental e neurociência: profissional moderno em ambiente arquitetônico iluminado e sereno, demonstrando alta concentração e clareza mental, integrado a uma delicada rede tridimensional translúcida de conexões sinápticas luminosas em tons de azul-safira (#0969b4). PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Azul Safira (#0969b4), Azul Profundo (#042f51) e Azul Claríssimo (#dbecf9). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 480 px aspect ratio) for "Borg Magnésio Treonato" (Theme: Foco Cognitivo, Memória & Desempenho Mental). Panoramic editorial composition of mental focus and neuroscience: modern professional in a serene, sunlit architectural space showing deep concentration and mental clarity, integrated with a delicate translucent 3D network of glowing sapphire-blue (#0969b4) synaptic connections. STRICT COLOR PALETTE GRADING: Sapphire Blue (#0969b4), Deep Prussian Blue (#042f51), and Pale Ice Blue (#dbecf9). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 06. [Pág. 11] Borg NAC 600mg
- **Linha:** Borg
- **Arquivo de Saída:** `imagens_ilustrativas/p11_borg_nac_600mg.png`
- **Dimensão do Card:** `1600 x 500 px`
- **Conceito no Catálogo:** *Ação Antioxidante, Defesa Celular & Saúde Respiratória*
- **Ativos Relacionados:** `N-Acetil L-Cisteína (NAC) 600mg | Vitamina C 45mg • Zinco Quelato 7mg`
- **Paleta de Cores da Página:** Principal `#32706b` • Escura `#163331` • Clara `#dbf9f7` (Verde-Azulado Esmeralda/Teal (#32706b), Verde Floresta Escuro (#163331) e Menta Glacial (#dbf9f7))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 500 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Borg NAC 600mg" (Tema: Ação Antioxidante, Defesa Celular & Saúde Respiratória). Fotografia panorâmica de bem-estar respiratório e proteção antioxidante: pessoa respirando ar puro profundamente em um cenário natural de manhã fresca com névoa suave iluminada em tons verde-azulados (#32706b), acompanhada por esferas translúcidas de proteção celular antioxidante flutuando suavemente. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Verde-Azulado Esmeralda/Teal (#32706b), Verde Floresta Escuro (#163331) e Menta Glacial (#dbf9f7). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 500 px aspect ratio) for "Borg NAC 600mg" (Theme: Ação Antioxidante, Defesa Celular & Saúde Respiratória). Panoramic respiratory wellness and antioxidant protection photography: person taking a deep breath of fresh air in a crisp morning setting with soft mist lit in emerald-teal (#32706b) tones, accompanied by gently floating translucent cellular shield spheres. STRICT COLOR PALETTE GRADING: Emerald Teal (#32706b), Deep Forest Teal (#163331), and Glacial Mint (#dbf9f7). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 07. [Pág. 15] Carti Master Colágeno Tipo II + Ácido Hialurônico
- **Linha:** Carti Master
- **Arquivo de Saída:** `imagens_ilustrativas/p15_carti_master_colageno_tipo_ii_acido_hialuronico.png`
- **Dimensão do Card:** `1600 x 480 px`
- **Conceito no Catálogo:** *Mobilidade Articular, Firmeza & Hidratação Tecidual*
- **Ativos Relacionados:** `Colágeno com Colágeno Tipo II Não Desnaturado 40mg | Hialuronato de Sódio (Ácido Hialurônico) 80mg`
- **Paleta de Cores da Página:** Principal `#064d7c` • Escura `#022237` • Clara `#dbeef9` (Azul Royal Escuro (#064d7c), Azul Abissal (#022237) e Azul Bruma (#dbeef9))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 480 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Carti Master Colágeno Tipo II + Ácido Hialurônico" (Tema: Mobilidade Articular, Firmeza & Hidratação Tecidual). Banner panorâmico de mobilidade articular e hidratação: gotas puras e viscosas de ácido hialurônico translúcido entrelaçadas a fibras helicoidais luminosas de colágeno tipo II à esquerda, fundindo-se à direita com um casal maduro ativo correndo levemente ao ar livre com total liberdade de movimento. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Azul Royal Escuro (#064d7c), Azul Abissal (#022237) e Azul Bruma (#dbeef9). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 480 px aspect ratio) for "Carti Master Colágeno Tipo II + Ácido Hialurônico" (Theme: Mobilidade Articular, Firmeza & Hidratação Tecidual). Panoramic joint mobility and hydration banner: pure viscous droplets of translucent hyaluronic acid intertwined with luminous Type II collagen triple-helix fibers on the left, blending on the right with an active mature couple jogging effortlessly outdoors with complete freedom of movement. STRICT COLOR PALETTE GRADING: Deep Royal Blue (#064d7c), Abyssal Navy (#022237), and Mist Blue (#dbeef9). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 08. [Pág. 16] Carti Master Condroitina + MSM
- **Linha:** Carti Master
- **Arquivo de Saída:** `imagens_ilustrativas/p16_carti_master_condroitina_msm.png`
- **Dimensão do Card:** `1600 x 500 px`
- **Conceito no Catálogo:** *Flexibilidade Articular, Conforto & Movimento Ativo*
- **Ativos Relacionados:** `Sulfato de Condroitina 400mg | Metilsulfonilmetano (MSM) 900mg | Colecalciferol (Vitamina D3) 2.000 UI`
- **Paleta de Cores da Página:** Principal `#b06637` • Escura `#4f2e18` • Clara `#f9e7db` (Terracota/Cobre Quente (#b06637), Marrom Café (#4f2e18) e Pêssego Suave (#f9e7db))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 500 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Carti Master Condroitina + MSM" (Tema: Flexibilidade Articular, Conforto & Movimento Ativo). Fotografia panorâmica de movimento ativo e flexibilidade articular: pessoa praticando atividade física ao ar livre sob luz dourada de fim de tarde (golden hour) em tons cobre e terracota (#b06637), combinada a elementos gráficos orgânicos translúcidos que remetem ao amortecimento, conforto e lubrificação das articulações. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Terracota/Cobre Quente (#b06637), Marrom Café (#4f2e18) e Pêssego Suave (#f9e7db). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 500 px aspect ratio) for "Carti Master Condroitina + MSM" (Theme: Flexibilidade Articular, Conforto & Movimento Ativo). Panoramic active movement and joint flexibility photography: person practicing outdoor physical activity in golden-hour light graded in warm copper and terracotta (#b06637), combined with translucent organic cushioning waves evoking joint comfort and flexibility. STRICT COLOR PALETTE GRADING: Warm Terracotta Copper (#b06637), Espresso Brown (#4f2e18), and Soft Peach (#f9e7db). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 09. [Pág. 17] Carti Master Ultra
- **Linha:** Carti Master
- **Arquivo de Saída:** `imagens_ilustrativas/p17_carti_master_ultra.png`
- **Dimensão do Card:** `1600 x 500 px`
- **Conceito no Catálogo:** *Proteção Articular Avançada & Alívio do Desconforto*
- **Ativos Relacionados:** `Colágeno Tipo II Não Desnaturado 40mg | Metilsulfonilmetano (MSM) • Vitamina E 10mg`
- **Paleta de Cores da Página:** Principal `#c25d24` • Escura `#572a10` • Clara `#f9e6db` (Laranja Queimado/Âmbar Intenso (#c25d24), Mogno Escuro (#572a10) e Areia Quente (#f9e6db))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 500 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Carti Master Ultra" (Tema: Proteção Articular Avançada & Alívio do Desconforto). Composição panorâmica de alta performance articular: corredor em movimento fluido sobre pista iluminada pelo sol nascente em tons âmbar e laranja queimado (#c25d24), com feixes dinâmicos de luz suave que destacam resistência, proteção articular avançada e vitalidade física. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Laranja Queimado/Âmbar Intenso (#c25d24), Mogno Escuro (#572a10) e Areia Quente (#f9e6db). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 500 px aspect ratio) for "Carti Master Ultra" (Theme: Proteção Articular Avançada & Alívio do Desconforto). High-performance joint protection panoramic composition: runner in fluid motion lit by rising sun in burnt orange and amber (#c25d24) tones, with dynamic smooth light trails highlighting endurance, advanced joint protection, and physical vitality. STRICT COLOR PALETTE GRADING: Burnt Orange / Intense Amber (#c25d24), Dark Mahogany (#572a10), and Warm Sand (#f9e6db). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 10. [Pág. 19] Cronovit Cálcio
- **Linha:** Cronovit
- **Arquivo de Saída:** `imagens_ilustrativas/p19_cronovit_calcio.png`
- **Dimensão do Card:** `1600 x 500 px`
- **Conceito no Catálogo:** *Saúde Óssea, Fortalecimento Dental & Absorção Mineral*
- **Ativos Relacionados:** `Carbonato de Cálcio 600mg | Colecalciferol (Vitamina D3) 200 UI`
- **Paleta de Cores da Página:** Principal `#149690` • Escura `#094340` • Clara `#dbf9f8` (Verde-Água/Turquesa (#149690), Verde Oceano Escuro (#094340) e Acqua Claro (#dbf9f8))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 500 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Cronovit Cálcio" (Tema: Saúde Óssea, Fortalecimento Dental & Absorção Mineral). Fotografia editorial panorâmica de saúde óssea e vitamina D3: ambiente ensolarado e arejado com elementos minerais brancos puros e gotas douradas translúcidas de colecalciferol (Vitamina D3) sobre fundo acqua suave (#dbf9f8) e detalhes em turquesa (#149690), transmitindo solidez óssea, dentes fortes e vitalidade. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Verde-Água/Turquesa (#149690), Verde Oceano Escuro (#094340) e Acqua Claro (#dbf9f8). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 500 px aspect ratio) for "Cronovit Cálcio" (Theme: Saúde Óssea, Fortalecimento Dental & Absorção Mineral). Panoramic editorial bone health and Vitamin D3 photography: sunlit airy setting featuring pure white mineral structures and golden translucent cholecalciferol (Vitamin D3) droplets over a soft aqua (#dbf9f8) and turquoise (#149690) backdrop, conveying bone solidity, strong teeth, and vitality. STRICT COLOR PALETTE GRADING: Turquoise Teal (#149690), Deep Ocean Green (#094340), and Pale Aqua (#dbf9f8). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 11. [Pág. 23] Cronovit Vitamina E 400 UI
- **Linha:** Cronovit
- **Arquivo de Saída:** `imagens_ilustrativas/p23_cronovit_vitamina_e_400_ui.png`
- **Dimensão do Card:** `1600 x 550 px`
- **Conceito no Catálogo:** *Proteção Celular Contra Danos dos Radicais Livres*
- **Ativos Relacionados:** `DL-Alfa-Tocoferol (Vitamina E) 400 UI (268mg)`
- **Paleta de Cores da Página:** Principal `#118379` • Escura `#073a36` • Clara `#dbf9f7` (Verde Esmeralda/Teal (#118379), Verde Profundo (#073a36) e Menta Suave (#dbf9f7))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 550 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Cronovit Vitamina E 400 UI" (Tema: Proteção Celular Contra Danos dos Radicais Livres). Banner panorâmico macro e lifestyle de ação antioxidante: cápsulas softgel translúcidas e gotas puras de vitamina E refletindo luz sobre fundo verde-esmeralda suave (#118379), formando uma barreira luminosa protetora ao redor de células estilizadas, simbolizando proteção contra radicais livres e renovação celular. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Verde Esmeralda/Teal (#118379), Verde Profundo (#073a36) e Menta Suave (#dbf9f7). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 550 px aspect ratio) for "Cronovit Vitamina E 400 UI" (Theme: Proteção Celular Contra Danos dos Radicais Livres). Panoramic macro and lifestyle antioxidant banner: translucent softgel pearls and pure vitamin E droplets reflecting light against a soft emerald-teal (#118379) background, forming a luminous protective barrier around stylized cells, symbolizing free-radical defense and cellular renewal. STRICT COLOR PALETTE GRADING: Emerald Teal (#118379), Deep Pine Teal (#073a36), and Soft Mint (#dbf9f7). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 12. [Pág. 24] Cronoliv Cabelo, Pele e Unhas
- **Linha:** Cronoliv
- **Arquivo de Saída:** `imagens_ilustrativas/p24_cronoliv_cabelo_pele_e_unhas.png`
- **Dimensão do Card:** `1600 x 500 px`
- **Conceito no Catálogo:** *Nutrição Capilar, Unhas Fortes & Pele Radiante*
- **Ativos Relacionados:** `Biotina (Vitamina B7) • Zinco Quelato | Vitaminas do Complexo B • Vitamina C`
- **Paleta de Cores da Página:** Principal `#a33681` • Escura `#49183a` • Clara `#f9dbf0` (Magenta/Framboesa Elegante (#a33681), Ameixa Escuro (#49183a) e Rosa Quartzo (#f9dbf0))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 500 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Cronoliv Cabelo, Pele e Unhas" (Tema: Nutrição Capilar, Unhas Fortes & Pele Radiante). Fotografia editorial de beleza e nutrição estética em formato panorâmico: retrato próximo (close-up) de mulher com pele radiante, cabelos sedosos com brilho natural e unhas impecáveis, iluminada por luz difusa de estúdio em paleta rosa-quartzo (#f9dbf0) e detalhes de seda fluida em tom magenta (#a33681). PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Magenta/Framboesa Elegante (#a33681), Ameixa Escuro (#49183a) e Rosa Quartzo (#f9dbf0). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 500 px aspect ratio) for "Cronoliv Cabelo, Pele e Unhas" (Theme: Nutrição Capilar, Unhas Fortes & Pele Radiante). Wide panoramic beauty and nutricosmetic editorial photography: close-up portrait of a woman with radiant skin, silky glossy hair, and flawless nails, lit by diffused studio lighting in a rose-quartz (#f9dbf0) palette with flowing magenta (#a33681) silk accents. STRICT COLOR PALETTE GRADING: Elegant Magenta Berry (#a33681), Deep Plum (#49183a), and Rose Quartz (#f9dbf0). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 13. [Pág. 25] Cronoliv Colágeno Verisol®
- **Linha:** Cronoliv
- **Arquivo de Saída:** `imagens_ilustrativas/p25_cronoliv_colageno_verisol.png`
- **Dimensão do Card:** `1600 x 480 px`
- **Conceito no Catálogo:** *Elasticidade da Pele, Síntese de Colágeno & Firmeza*
- **Ativos Relacionados:** `Peptídeos Bioativos de Colágeno Hidrolisado Verisol® 2,5g | Biotina • Vitamina C • Ácido Hialurônico`
- **Paleta de Cores da Página:** Principal `#604396` • Escura `#2b1e43` • Clara `#e6dbf9` (Roxo Violeta Real (#604396), Violeta Profundo (#2b1e43) e Lilás Lavanda (#e6dbf9))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 480 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Cronoliv Colágeno Verisol®" (Tema: Elasticidade da Pele, Síntese de Colágeno & Firmeza). Banner panorâmico de dermocosmética nutricional (Colágeno Verisol): composição sofisticada unindo ondas acetinadas de peptídeos bioativos de colágeno e gotas de ácido hialurônico em tons violeta (#604396) e lavanda (#e6dbf9) com o perfil elegante de uma pele jovem, firme, hidratada e elástica. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Roxo Violeta Real (#604396), Violeta Profundo (#2b1e43) e Lilás Lavanda (#e6dbf9). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 480 px aspect ratio) for "Cronoliv Colágeno Verisol®" (Theme: Elasticidade da Pele, Síntese de Colágeno & Firmeza). Panoramic nutricosmetic skin elasticity banner (Verisol Collagen): sophisticated composition blending satin waves of bioactive collagen peptides and hyaluronic acid droplets in royal violet (#604396) and lavender (#e6dbf9) with the elegant profile of firm, hydrated, elastic skin. STRICT COLOR PALETTE GRADING: Royal Violet Purple (#604396), Deep Violet (#2b1e43), and Lavender Lilac (#e6dbf9). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 14. [Pág. 26] Cronoliv Própolis
- **Linha:** Cronoliv
- **Arquivo de Saída:** `imagens_ilustrativas/p26_cronoliv_propolis.png`
- **Dimensão do Card:** `1600 x 550 px`
- **Conceito no Catálogo:** *Defesa Imunológica Natural & Proteção Diária*
- **Ativos Relacionados:** `Extrato de Própolis Verde Padronizado | Vitamina C 45mg • Vitamina E 10mg • Zinco 7mg`
- **Paleta de Cores da Página:** Principal `#c0880a` • Escura `#563d04` • Clara `#f9f0db` (Dourado Mel/Âmbar (#c0880a), Marrom Âmbar Escuro (#563d04) e Creme Mel (#f9f0db))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 550 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Cronoliv Própolis" (Tema: Defesa Imunológica Natural & Proteção Diária). Fotografia macro e conceitual panorâmica de imunidade natural: gotas densas e reluzentes de extrato de própolis verde brasileiro e favo geométrico sutil banhados em luz dourada de mel (#c0880a) com folhas botânicas frescas ao fundo, transmitindo defesa imunológica natural e proteção diária. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Dourado Mel/Âmbar (#c0880a), Marrom Âmbar Escuro (#563d04) e Creme Mel (#f9f0db). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 550 px aspect ratio) for "Cronoliv Própolis" (Theme: Defesa Imunológica Natural & Proteção Diária). Panoramic macro and conceptual natural immunity photography: rich glowing droplets of Brazilian green propolis extract and subtle geometric honeycomb bathed in honey-gold (#c0880a) light with fresh botanical leaves in soft focus, conveying natural immune defense and daily protection. STRICT COLOR PALETTE GRADING: Honey Gold Amber (#c0880a), Dark Amber Brown (#563d04), and Honey Cream (#f9f0db). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 15. [Pág. 27] Nutrivix Coenzima Q10
- **Linha:** Nutrivix
- **Arquivo de Saída:** `imagens_ilustrativas/p27_nutrivix_coenzima_q10.png`
- **Dimensão do Card:** `1600 x 450 px`
- **Conceito no Catálogo:** *Antioxidante Celular, Vitalidade & Energia Mitocondrial*
- **Ativos Relacionados:** `Coenzima Q10 100mg por porção | Vitamina E (DL-Alfa-Tocoferol) 10mg`
- **Paleta de Cores da Página:** Principal `#7a1c6b` • Escura `#360c30` • Clara `#f9dbf5` (Púrpura/Vinho Ametista (#7a1c6b), Bordô Profundo (#360c30) e Rosa Orquídea Claro (#f9dbf5))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 450 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Nutrivix Coenzima Q10" (Tema: Antioxidante Celular, Vitalidade & Energia Mitocondrial). Composição panorâmica de energia mitocondrial e vitalidade cardiovascular: esferas luminosas douradas de Coenzima Q10 e Vitamina E flutuando em um ambiente elegante de tons púrpura-ametista (#7a1c6b) e rosa-orquídea (#f9dbf5), com ondas de energia celular suave que simbolizam vitalidade, longevidade e proteção antioxidante. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Púrpura/Vinho Ametista (#7a1c6b), Bordô Profundo (#360c30) e Rosa Orquídea Claro (#f9dbf5). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 450 px aspect ratio) for "Nutrivix Coenzima Q10" (Theme: Antioxidante Celular, Vitalidade & Energia Mitocondrial). Panoramic mitochondrial energy and cardiovascular vitality composition: luminous golden Coenzyme Q10 and Vitamin E spheres floating in an elegant amethyst-purple (#7a1c6b) and pale-orchid (#f9dbf5) environment, with smooth cellular energy waves symbolizing vitality, longevity, and antioxidant defense. STRICT COLOR PALETTE GRADING: Amethyst Wine Purple (#7a1c6b), Deep Burgundy (#360c30), and Pale Orchid Pink (#f9dbf5). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 16. [Pág. 28] Nutrivix Magnésio Dimalato
- **Linha:** Nutrivix
- **Arquivo de Saída:** `imagens_ilustrativas/p28_nutrivix_magnesio_dimalato.png`
- **Dimensão do Card:** `1600 x 500 px`
- **Conceito no Catálogo:** *Energia Muscular, Disposição & Redução do Cansaço*
- **Ativos Relacionados:** `Magnésio Dimalato 260mg`
- **Paleta de Cores da Página:** Principal `#166d97` • Escura `#093143` • Clara `#dbf0f9` (Azul Petróleo Médio (#166d97), Azul Marinho Escuro (#093143) e Azul Gelo Suave (#dbf0f9))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 500 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Nutrivix Magnésio Dimalato" (Tema: Energia Muscular, Disposição & Redução do Cansaço). Banner panorâmico de energia muscular e disposição: adulto ativo praticando exercício ao ar livre sob céu limpo em gradação azul-petróleo (#166d97) e gelo (#dbf0f9), com cristais minerais puros de magnésio dimalato em primeiro plano desfocado, evocando vigor muscular e redução do cansaço. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Azul Petróleo Médio (#166d97), Azul Marinho Escuro (#093143) e Azul Gelo Suave (#dbf0f9). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 500 px aspect ratio) for "Nutrivix Magnésio Dimalato" (Theme: Energia Muscular, Disposição & Redução do Cansaço). Panoramic muscular energy and stamina banner: active adult exercising outdoors under a clean sky graded in cerulean teal (#166d97) and ice blue (#dbf0f9), with pure magnesium malate mineral crystals in soft foreground focus, evoking muscular vigor and reduced fatigue. STRICT COLOR PALETTE GRADING: Medium Cerulean Teal (#166d97), Dark Navy Teal (#093143), and Soft Ice Blue (#dbf0f9). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 17. [Pág. 29] Nutrivix Magnésio Treonato
- **Linha:** Nutrivix
- **Arquivo de Saída:** `imagens_ilustrativas/p29_nutrivix_magnesio_treonato.png`
- **Dimensão do Card:** `1600 x 480 px`
- **Conceito no Catálogo:** *Foco Cognitivo, Memória & Desempenho Mental*
- **Ativos Relacionados:** `Magnésio L-Treonato 260mg`
- **Paleta de Cores da Página:** Principal `#4d3b84` • Escura `#221a3b` • Clara `#e3dbf9` (Índigo/Roxo Ametista (#4d3b84), Roxo Noite (#221a3b) e Lavanda Suave (#e3dbf9))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 480 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Nutrivix Magnésio Treonato" (Tema: Foco Cognitivo, Memória & Desempenho Mental). Fotografia conceitual panorâmica de desempenho cognitivo e memória: ambiente contemporâneo sereno em tons lavanda (#e3dbf9) e índigo-ametista (#4d3b84), combinando uma mente focada em leitura/estratégia com filamentos luminosos elegantes que remetem à neuroplasticidade, foco e clareza mental. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Índigo/Roxo Ametista (#4d3b84), Roxo Noite (#221a3b) e Lavanda Suave (#e3dbf9). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 480 px aspect ratio) for "Nutrivix Magnésio Treonato" (Theme: Foco Cognitivo, Memória & Desempenho Mental). Panoramic conceptual photography of cognitive performance and memory: serene contemporary environment in soft lavender (#e3dbf9) and indigo-amethyst (#4d3b84), combining a focused mind in study/strategy with elegant glowing filaments evoking neuroplasticity, focus, and mental clarity. STRICT COLOR PALETTE GRADING: Indigo Amethyst Purple (#4d3b84), Night Purple (#221a3b), and Soft Lavender (#e3dbf9). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 18. [Pág. 32] Odessy Tempo
- **Linha:** Odessy
- **Arquivo de Saída:** `imagens_ilustrativas/p32_odessy_tempo.png`
- **Dimensão do Card:** `1600 x 480 px`
- **Conceito no Catálogo:** *Antienvelhecimento Celular & Renovação Vital*
- **Ativos Relacionados:** `Cafeína Anidra • Taurina | Vitaminas do Complexo B • Vitamina C`
- **Paleta de Cores da Página:** Principal `#b35f50` • Escura `#502b24` • Clara `#f9e0db` (Coral Terracota/Rosé Queimado (#b35f50), Marrom Avermelhado (#502b24) e Pêssego Rosado (#f9e0db))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 480 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Odessy Tempo" (Tema: Antienvelhecimento Celular & Renovação Vital). Banner panorâmico de energia, foco e renovação vital: ondas fluidas de energia luminosa e microesferas antioxidantes em paleta coral-terracota (#b35f50) e pêssego suave (#f9e0db), acompanhadas por uma pessoa com expressão radiante e desperta sob luz matinal revigorante, simbolizando disposição física, alerta mental e ação antioxidante. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Coral Terracota/Rosé Queimado (#b35f50), Marrom Avermelhado (#502b24) e Pêssego Rosado (#f9e0db). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 480 px aspect ratio) for "Odessy Tempo" (Theme: Antienvelhecimento Celular & Renovação Vital). Panoramic energy, alertness, and vital renewal banner: fluid waves of luminous energy and antioxidant microspheres in a terracotta-coral (#b35f50) and rosy-peach (#f9e0db) palette, paired with a radiant, energized person in invigorating morning light, symbolizing physical stamina, mental alertness, and antioxidant action. STRICT COLOR PALETTE GRADING: Terracotta Coral / Burnt Rose (#b35f50), Deep Russet (#502b24), and Rosy Peach (#f9e0db). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 19. [Pág. 33] Biomov Colágeno Tipo II + Ácido Hialurônico
- **Linha:** Biomov
- **Arquivo de Saída:** `imagens_ilustrativas/p33_biomov_colageno_tipo_ii_acido_hialuronico.png`
- **Dimensão do Card:** `1600 x 480 px`
- **Conceito no Catálogo:** *Mobilidade Articular, Firmeza & Hidratação Tecidual*
- **Ativos Relacionados:** `Colágeno Tipo II Não Desnaturado 40mg | Ácido Hialurônico 80mg`
- **Paleta de Cores da Página:** Principal `#3a1c6b` • Escura `#1c0d33` • Clara `#e7dbf9` (Roxo Profundo/Uva (#3a1c6b), Violeta Escuro (#1c0d33) e Lilás Claro (#e7dbf9))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 480 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Biomov Colágeno Tipo II + Ácido Hialurônico" (Tema: Mobilidade Articular, Firmeza & Hidratação Tecidual). Composição panorâmica de liberdade articular e função motora: estrutura artística translúcida de fibras de colágeno tipo II e gotas hidratantes de ácido hialurônico iluminadas em tons roxo-profundo (#3a1c6b) e lilás (#e7dbf9), integrada à silhueta fluida de movimento corporal sem dor e com flexibilidade plena. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Roxo Profundo/Uva (#3a1c6b), Violeta Escuro (#1c0d33) e Lilás Claro (#e7dbf9). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 480 px aspect ratio) for "Biomov Colágeno Tipo II + Ácido Hialurônico" (Theme: Mobilidade Articular, Firmeza & Hidratação Tecidual). Panoramic joint freedom and motor function composition: artistic translucent structure of Type II collagen fibers and hydrating hyaluronic acid droplets lit in deep purple (#3a1c6b) and pale lilac (#e7dbf9), integrated with a fluid silhouette of pain-free body movement and full flexibility. STRICT COLOR PALETTE GRADING: Deep Grape Purple (#3a1c6b), Dark Violet (#1c0d33), and Pale Lilac (#e7dbf9). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 20. [Pág. 34] Ceitil Acetilcisteína
- **Linha:** Ceitil
- **Arquivo de Saída:** `imagens_ilustrativas/p34_ceitil_acetilcisteina.png`
- **Dimensão do Card:** `1600 x 500 px`
- **Conceito no Catálogo:** *Defesa Respiratória, Fluidificação & Imunidade Fortalecida*
- **Ativos Relacionados:** `N-Acetil L-Cisteína (Acetilcisteína) 600mg | Vitamina C 45mg • Vitamina D 2.000 UI • Zinco 7mg`
- **Paleta de Cores da Página:** Principal `#274f82` • Escura `#11233a` • Clara `#dbe9f9` (Azul Aço/Marinho Clássico (#274f82), Azul Noite (#11233a) e Azul Bruma (#dbe9f9))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 500 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Ceitil Acetilcisteína" (Tema: Defesa Respiratória, Fluidificação & Imunidade Fortalecida). Fotografia panorâmica de saúde respiratória e imunidade fortalecida: brisa fresca de montanha e ondas translúcidas de ar puro em tons azul-aço (#274f82) e azul-bruma (#dbe9f9), com pessoa respirando profundamente ao ar livre e cristais luminosos de acetilcisteína, vitamina C, D e zinco simbolizando vias aéreas livres e defesa imunológica. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Azul Aço/Marinho Clássico (#274f82), Azul Noite (#11233a) e Azul Bruma (#dbe9f9). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 500 px aspect ratio) for "Ceitil Acetilcisteína" (Theme: Defesa Respiratória, Fluidificação & Imunidade Fortalecida). Panoramic respiratory health and strengthened immunity photography: fresh mountain breeze and translucent waves of pure air in steel-navy (#274f82) and mist-blue (#dbe9f9), with a person breathing deeply outdoors and luminous crystals of acetylcysteine, vitamin C, D, and zinc symbolizing clear airways and immune defense. STRICT COLOR PALETTE GRADING: Classic Steel Navy (#274f82), Midnight Blue (#11233a), and Mist Blue (#dbe9f9). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 21. [Pág. 35] Complexo Prodiz Melatonina
- **Linha:** Complexo Prodiz
- **Arquivo de Saída:** `imagens_ilustrativas/p35_complexo_prodiz_melatonina.png`
- **Dimensão do Card:** `1600 x 500 px`
- **Conceito no Catálogo:** *Sono Reparador, Ciclo Circadiano & Relaxamento*
- **Ativos Relacionados:** `Melatonina 0,21mg em Cápsula Softgel | Vitamina B6 (Piridoxina) 1,3mg`
- **Paleta de Cores da Página:** Principal `#24296b` • Escura `#111333` • Clara `#dbdef9` (Azul Índigo Noturno (#24296b), Azul Meia-Noite (#111333) e Lavanda Lunar (#dbdef9))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 500 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Complexo Prodiz Melatonina" (Tema: Sono Reparador, Ciclo Circadiano & Relaxamento). Fotografia panorâmica de sono reparador e ciclo circadiano: quarto minimalista e aconchegante banhado por luz luar suave em tons índigo noturno (#24296b) e lavanda lunar (#dbdef9), com pessoa dormindo serenamente em lençóis macios e delicadas partículas luminosas douradas/azuladas flutuando no ar, transmitindo relaxamento profundo e descanso restaurador. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Azul Índigo Noturno (#24296b), Azul Meia-Noite (#111333) e Lavanda Lunar (#dbdef9). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 500 px aspect ratio) for "Complexo Prodiz Melatonina" (Theme: Sono Reparador, Ciclo Circadiano & Relaxamento). Panoramic restful sleep and circadian rhythm photography: cozy minimalist bedroom bathed in soft moonlight in nocturnal indigo (#24296b) and lunar lavender (#dbdef9) tones, featuring a person sleeping peacefully in soft linens with delicate glowing particles floating in the air, conveying deep relaxation and restorative rest. STRICT COLOR PALETTE GRADING: Nocturnal Indigo Blue (#24296b), Midnight Blue (#111333), and Lunar Lavender (#dbdef9). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 22. [Pág. 36] Epadose Colina
- **Linha:** Epadose
- **Arquivo de Saída:** `imagens_ilustrativas/p36_epadose_colina.png`
- **Dimensão do Card:** `1600 x 500 px`
- **Conceito no Catálogo:** *Metabolismo Lipídico, Saúde Hepática & Desintoxicação*
- **Ativos Relacionados:** `Citrato de Colina • DL-Metionina | Vitaminas B1, B6 e B12`
- **Paleta de Cores da Página:** Principal `#d1860a` • Escura `#5e3c04` • Clara `#f9eedb` (Âmbar Dourado/Ocre (#d1860a), Marrom Dourado Escuro (#5e3c04) e Creme Solar (#f9eedb))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 500 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Epadose Colina" (Tema: Metabolismo Lipídico, Saúde Hepática & Desintoxicação). Banner panorâmico de saúde metabólica, equilíbrio lipídico e bem-estar digestivo/hepático: mesa iluminada por sol matinal com água fresca com limão, folhas botânicas naturais e gotas puras douradas (#d1860a) sobre fundo creme solar (#f9eedb), transmitindo leveza digestiva, desintoxicação e metabolismo lipídico saudável. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Âmbar Dourado/Ocre (#d1860a), Marrom Dourado Escuro (#5e3c04) e Creme Solar (#f9eedb). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 500 px aspect ratio) for "Epadose Colina" (Theme: Metabolismo Lipídico, Saúde Hepática & Desintoxicação). Panoramic metabolic health, lipid balance, and hepatic/digestive wellness banner: sunlit morning table with fresh lemon water, natural botanical leaves, and pure golden-amber (#d1860a) droplets against a solar-cream (#f9eedb) background, conveying digestive lightness, detoxification, and healthy lipid metabolism. STRICT COLOR PALETTE GRADING: Golden Amber Ochre (#d1860a), Dark Golden Brown (#5e3c04), and Solar Cream (#f9eedb). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 23. [Pág. 37] Laclaze Lactase 10.000 U.FCC
- **Linha:** Laclaze
- **Arquivo de Saída:** `imagens_ilustrativas/p37_laclaze_lactase_10_000_u_fcc.png`
- **Dimensão do Card:** `1600 x 550 px`
- **Conceito no Catálogo:** *Digestão Completa da Lactose & Conforto Digestivo*
- **Ativos Relacionados:** `Enzima Lactase de Aspergillus oryzae 10.000 U.FCC`
- **Paleta de Cores da Página:** Principal `#5da1d0` • Escura `#2a485d` • Clara `#dbedf9` (Azul Leite/Celeste Suave (#5da1d0), Azul Ardósia Escuro (#2a485d) e Branco Azulado (#dbedf9))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 550 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Laclaze Lactase 10.000 U.FCC" (Tema: Digestão Completa da Lactose & Conforto Digestivo). Fotografia editorial panorâmica de conforto digestivo e liberdade alimentar (Lactase): respingo artístico e leve de leite puro e cremoso (milk splash) iluminado sobre fundo azul-celeste suave (#5da1d0 e #dbedf9), integrado à direita com uma pessoa sorridente apreciando uma refeição/café com leite com total conforto e bem-estar digestivo. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Azul Leite/Celeste Suave (#5da1d0), Azul Ardósia Escuro (#2a485d) e Branco Azulado (#dbedf9). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 550 px aspect ratio) for "Laclaze Lactase 10.000 U.FCC" (Theme: Digestão Completa da Lactose & Conforto Digestivo). Panoramic editorial digestive comfort and food freedom photography (Lactase): artistic light splash of pure creamy milk lit against a soft sky-blue (#5da1d0 and #dbedf9) background, integrated on the right with a smiling person enjoying a latte/dairy meal with complete digestive comfort and well-being. STRICT COLOR PALETTE GRADING: Soft Sky Blue (#5da1d0), Dark Slate Blue (#2a485d), and Milky Ice Blue (#dbedf9). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 24. [Pág. 38] Malosso Citrato Malato de Cálcio
- **Linha:** Malosso
- **Arquivo de Saída:** `imagens_ilustrativas/p38_malosso_citrato_malato_de_calcio.png`
- **Dimensão do Card:** `1600 x 500 px`
- **Conceito no Catálogo:** *Absorção Otimizada de Cálcio com Alta Biodisponibilidade*
- **Ativos Relacionados:** `Citrato Malato de Cálcio 250mg | Colecalciferol (Vitamina D3) 200 UI`
- **Paleta de Cores da Página:** Principal `#075e8b` • Escura `#032a3e` • Clara `#dbeff9` (Azul Cerúleo Profundo (#075e8b), Azul Marinho Escuro (#032a3e) e Azul Gelo (#dbeff9))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 500 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Malosso Citrato Malato de Cálcio" (Tema: Absorção Otimizada de Cálcio com Alta Biodisponibilidade). Composição panorâmica de alta biodisponibilidade de cálcio e saúde óssea: estrutura cristalina branca e translúcida de citrato malato de cálcio banhada por feixes de luz solar (Vitamina D3) sobre fundo azul-cerúleo (#075e8b) e azul-gelo (#dbeff9), combinada à imagem de vitalidade física e sustentação óssea. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Azul Cerúleo Profundo (#075e8b), Azul Marinho Escuro (#032a3e) e Azul Gelo (#dbeff9). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 500 px aspect ratio) for "Malosso Citrato Malato de Cálcio" (Theme: Absorção Otimizada de Cálcio com Alta Biodisponibilidade). Panoramic high-bioavailability calcium and bone health composition: white translucent crystalline structure of calcium citrate malate bathed in warm sunlight rays (Vitamin D3) against a deep cerulean (#075e8b) and ice-blue (#dbeff9) background, combined with imagery of physical vitality and skeletal strength. STRICT COLOR PALETTE GRADING: Deep Cerulean Blue (#075e8b), Dark Marine Blue (#032a3e), and Ice Blue (#dbeff9). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---

### 25. [Pág. 39] Naturedux Cromo
- **Linha:** Naturedux
- **Arquivo de Saída:** `imagens_ilustrativas/p39_naturedux_cromo.png`
- **Dimensão do Card:** `1600 x 480 px`
- **Conceito no Catálogo:** *Controle Glicêmico & Metabolismo de Carboidratos e Gorduras*
- **Ativos Relacionados:** `Picolinato de Cromo 250mcg | Vitamina E 10mg • Zinco Quelato 7mg`
- **Paleta de Cores da Página:** Principal `#aa683c` • Escura `#4c2f1b` • Clara `#f9e7db` (Caramelo/Bronze Quente (#aa683c), Marrom Cacau (#4c2f1b) e Creme Amêndoa (#f9e7db))

**Prompt em Português (Gemini / Antigravity):**
```text
Banner fotográfico horizontal panorâmico (1600 x 480 px, proporção widescreen panorâmica) para catálogo farmacêutico premium do produto "Naturedux Cromo" (Tema: Controle Glicêmico & Metabolismo de Carboidratos e Gorduras). Fotografia editorial panorâmica de equilíbrio metabólico e nutrição inteligente (Picolinato de Cromo): composição clean de estilo de vida saudável com ingredientes naturais nobres (grãos integrais, amêndoas, especiarias quentes) e luz bronze-caramelo (#aa683c) sobre superfície creme (#f9e7db), simbolizando controle glicêmico e metabolismo equilibrado de proteínas, carboidratos e gorduras. PALETA DE CORES OBRIGATÓRIA DA PÁGINA: Caramelo/Bronze Quente (#aa683c), Marrom Cacau (#4c2f1b) e Creme Amêndoa (#f9e7db). Iluminação editorial suave de alto padrão, profundidade de campo cinematográfica (bokeh suave), texturas hiper-realistas 8k. PROIBIDO incluir qualquer texto, letras, números, tipografia, logotipos ou embalagens com rótulos na imagem.
```

**Prompt em Inglês (GPT Codex / Image API):**
```text
Ultra-wide panoramic editorial health and pharmaceutical catalog banner (1600 x 480 px aspect ratio) for "Naturedux Cromo" (Theme: Controle Glicêmico & Metabolismo de Carboidratos e Gorduras). Panoramic editorial metabolic balance and smart nutrition photography (Chromium Picolinate): clean healthy lifestyle composition featuring wholesome natural ingredients (whole grains, almonds, warm botanicals) and warm caramel-bronze (#aa683c) lighting over an almond-cream (#f9e7db) surface, symbolizing glycemic control and balanced metabolism of proteins, carbohydrates, and fats. STRICT COLOR PALETTE GRADING: Warm Caramel Bronze (#aa683c), Cocoa Brown (#4c2f1b), and Almond Cream (#f9e7db). High-end studio and natural editorial lighting, shallow depth of field, photorealistic 8k macro and lifestyle textures, clean luxury nutricosmetic aesthetic. NO text, NO letters, NO typography, NO numbers, NO watermarks, NO product bottles or labels.
```

---
