# Assifarma — Design System & Padrão Visual de Catálogo (2026)
**Formato Oficial:** Apresentação 1920x1080 (16:9 Paisagem) — 1 Produto por Página  
**Documento Base Analisado:** `Design padrão CATÁLOGO VITNUTRY - 2026.pdf`  
**Base Regulatória:** Resolução RDC nº 429/2020 e Instrução Normativa IN nº 28/2018 e IN nº 75/2020 (ANVISA)

---

## 1. Visão Geral da Análise do Arquivo Referência

O arquivo de referência (`CATÁLOGO VITNUTRY - 2026.pdf`) utilizava um formato A4 vertical dividindo 2 produtos por página. Na nova versão solicitada, faremos uma **evolução premium para tela cheia widescreen (1920x1080 px)**, conferindo:
1. **1 produto por página:** Espaço nobre para destaque comercial, leitura confortável da tabela nutricional e impacto fotográfico.
2. **Harmonia de 3 colunas:** Estrutura modular, escalável e de rápida edição via arquivos Markdown (`.md`) e automação HTML/CSS/PDF.
3. **Profundidade em camadas:** Imagem ilustrativa conceito/lifestyle cobrindo a largura da página em degradê contínuo, com área focal nítida na Coluna 3, enquanto o Packshot (Coluna 2) e a Tabela Nutricional (Coluna 1) sobrepõem-se com legibilidade perfeita.
4. **Ritmo de Leitura Dinâmico (Página A e B):** Alternância espelhada da ordem das colunas para evitar monotonia na leitura sequencial do catálogo.

---

## 2. Estrutura Bipartida Meio-a-Meio (50% Imagem / 50% Fundo Branco)

O layout Widescreen 1920x1080 (16:9) adota uma divisão vertical equilibrada:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ 50% SUPERIOR (Altura: 540px)                                                                │
│ [Aba da Marca] ──── Fotografia Conceito / Atletas / Lifestyle ───────────────────────────── │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│ ──── FAIXA VETORIAL DIVISÓRIA (32px) COM BARRAS INCLINADAS PARALELAS (///) ───────────────── │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│ 50% INFERIOR (Altura: 540px) — FUNDO BRANCO PURO (#FFFFFF)                                  │
│                                                                                             │
│  [COLUNA 1]                [COLUNA 2]                    [DIVISOR]      [COLUNA 3]          │
│  Tabela Nutricional        Packshot Hero Gigante (440px)     │          Frase de Efeito     │
│  Oficial (ANVISA)          (sobrepõe o meio-a-meio)          │          "Completo com 22"   │
│  com borda preta nítida    Categoria + Nome Bold             │                              │
│                            Benefícios IN 28 com Ícones       │          4 Badges Pílula     │
│                                                              │          Azul Escuro         │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Proporções e Espaçamentos Oficiais:
- **Resolução de Tela:** `1920px` de largura × `1080px` de altura (16:9 paisagem).
- **Divisão Vertical (50% / 50%):**
  - **Topo (0 a 540px):** Imagem ilustrativa/lifestyle fotográfica. Na Página A fica à direita com degradê para cinza claro à esquerda; na Página B fica à esquerda com degradê para a direita.
  - **Base (540px a 1080px):** Branco puro (`#ffffff`), proporcionando contraste e clareza para leitura técnica e comercial.
- **Espaçamento Lateral (Centralização do Conteúdo):**
  - Margem lateral generosa de **140px de cada lado** (`padding: 0 140px`), garantindo que os elementos fiquem centralizados e harmônicos na tela.
- **Elementos Vetoriais de Identidade:**
  1. **Aba Superior da Marca (Brand Tab):** Trapézio inclinado a ~60° no topo (canto superior esquerdo na Página A; canto superior direito na Página B) com o nome da linha em branco.
  2. **Faixa Divisória Horizontal com Barras Inclinadas:** Faixa em azul (`#175da9`) posicionada na linha dos 540px, com **4 barras paralelas inclinadas (paralelogramos esportivos)** logo abaixo da área fotográfica.
  3. **Divisor Vertical Timeline:** Linha vertical azul (`#175da9`, 1.5px) com círculos sólidos nas extremidades separando a Coluna 2 e a Coluna 3.
- **Packshot do Produto Hero:**
  - Altura expressiva de **420px a 440px**, posicionado de forma a **cruzar a linha divisória de 50%**, projetando sombra natural de contato sobre a base branca.

---

## 3. Anatomia Detalhada dos Elementos por Coluna

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ PÁGINA A (PADRÃO NORMAL)                                                                    │
├──────────────────────────┬─────────────────────────────┬────────────────────────────────────┤
│ COLUNA 1                 │ COLUNA 2                    │ COLUNA 3                           │
│ • Nome da Linha / Logo   │ • Imagem do Produto         │ • Frase Criativa de Efeito         │
│ • Tabela Nutricional     │ • Nome Comercial em Destaque│ • Destaques (Glúten, Açúcar, etc.) │
│   (RDC 429 / IN 75)      │ • Benefícios com Ícones     │ • Ponto Focal da Imagem Conceito   │
│                          │   (Ordem de Importância)    │   (Imagem de fundo em 3 colunas)   │
└──────────────────────────┴─────────────────────────────┴────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ PÁGINA B (ORDEM INVERTIDA)                                                                  │
├──────────────────────────┬─────────────────────────────┬────────────────────────────────────┤
│ COLUNA 3 (INVERTIDA)     │ COLUNA 2                    │ COLUNA 1 (INVERTIDA)               │
│ • Ponto Focal Conceito   │ • Imagem do Produto         │ • Nome da Linha / Logo             │
│ • Frase Criativa         │ • Nome Comercial em Destaque│ • Tabela Nutricional               │
│ • Destaques (Badges)     │ • Benefícios com Ícones     │   (RDC 429 / IN 75)                │
└──────────────────────────┴─────────────────────────────┴────────────────────────────────────┘
```

### # Coluna 1: Linha & Tabela Nutricional
* **Header da Linha:** Nome da Linha com tracking elegante (`letter-spacing: 0.12em`), caixa alta e peso regular/médio (ex: `BORG`, `CARTI MASTER`, `CRONOVIT`), acompanhado de um indicador sutil da marca.
* **Tabela Nutricional Oficial:**
  - Segue estritamente as normas da ANVISA (RDC 429/2020 e IN 75/2020).
  - Título em destaque: **INFORMAÇÃO NUTRICIONAL** (caixa alta, negrito).
  - Porções por Embalagem e Medida Usual (ex: *Porção: 1 g (2 cápsulas)*).
  - Colunas alinhadas: *Item Nutricional*, *Quantidade por porção* e *%VD\**.
  - Nota de rodapé regulatória: *"Não contém quantidades significativas de..."* e *"\* Percentual de valores diários fornecidos pela porção"*.
* **Tratamento de Fundo:** Fundo em card translúcido tipo *Glassmorphism Suave* (`rgba(255, 255, 255, 0.94)` com `backdrop-filter: blur(12px)` e borda sutil `rgba(255,255,255,0.6)` ou fundo escuro suave para temas noturnos), permitindo que a imagem ampla do fundo passe por trás sem prejudicar a leitura precisa dos dados da tabela.

### # Coluna 2: Produto & Benefícios Funcionais (IN 28)
* **Imagem do Produto (Packshot):**
  - Render ou foto do frasco/blister/embalagem em altíssima resolução com fundo transparente (`.png`).
  - Sombra projetada realista e suave de contato na base (`box-shadow` e reflexo suave).
  - Posicionamento de destaque hero, sobrepondo ligeiramente a transição com a imagem de fundo.
* **Nome do Produto em Destaque:**
  - Subtítulo da Categoria: `Sora Regular`, 18–20px, cor secundária (ex: *Polivitamínico*).
  - Nome Principal: `Sora ExtraBold`, 46–54px, cor de destaque da linha (ex: **AZ**, **ENERGY**, **COENZIMA Q10**, **PEA**).
  - Apresentação / Embalagem: `Sora Medium`, 16–18px, cor de apoio (ex: *60 Cápsulas softgel*, *30 Sachês sabor limão*).
* **Benefícios conforme IN 28 (com Ícones Temáticos):**
  - **Hierarquia de Importância:** O benefício carro-chefe do produto sempre encabeça a lista, seguido pelos benefícios secundários.
  - **Destaque Tipográfico:** Sujeito/Nutriente em texto regular/médio (`Sora 400/500`) e a **ação funcional em negrito destacado** (`Sora 700/800`) — exatamente como verificado na referência:
    - Ex: *As vitaminas C e E, o cobre e o zinco **são antioxidantes que auxiliam na proteção dos danos causados pelos radicais livres**.*
  - **Ícones Temáticos:** Cada alegação recebe um ícone vetorial exclusivo posicionado em um círculo estilizado com a cor da linha.

### # Coluna 3: Conceito Criativo, Badges & Imagem Ilustrativa
* **Frase de Efeito Criativa (Punchline):**
  - Tipografia expressiva com números ou palavras-chave ampliadas:
    - Ex: *Completo com **22** vitaminas e minerais.*
    - Ex: *Saúde e energia para **aproveitar o melhor da vida após os 50**.*
* **Destaques / Selos de Formulação (Badges):**
  - Pílulas com ícones de verificação (Checkmarks) para claims rápidos:
    - `Zero Açúcar`
    - `Não contém Glúten`
    - `Não contém Lactose`
    - `Não contém Carboidratos`
    - `Não contém Sódio`
* **Imagem Ilustrativa (Conceito / Lifestyle):**
  - A imagem ocupa a largura total da página ou estende-se cobrindo o plano de fundo.
  - O ponto de maior clareza visual e impacto fotográfico é revelado nesta Coluna 3.
  - Nas Colunas 2 e 1, a imagem recebe um degradê progressivo para a cor de fundo (branco/cinza neutro ou azul escuro) para dar suporte à embalagem e à tabela nutricional.
  - Texto legal obrigatório: *"Imagens ilustrativas"* em corpo discreto (12px).

---

## 4. Família de Ícones Rápida e Simples: Lucide Icons

Para garantir carregamento instantâneo, leveza e facilidade de manutenção em código HTML/SVG e Markdown, a biblioteca recomendada é a **Lucide Icons** (moderna, traço consistente de 1.75px–2px, 100% SVG vetorial nativo).

### Mapeamento Direto: Benefício IN 28 vs Ícone Lucide

| Benefício / Área de Ação (IN 28) | Ícone Lucide | Classe / SVG | Representação Visual |
| :--- | :--- | :--- | :--- |
| **Metabolismo Energético / Energia** | `zap` | `<i data-lucide="zap"></i>` | Raio / Energia celular |
| **Sistema Imunológico / Defesa** | `shield-check` | `<i data-lucide="shield-check"></i>` | Escudo de proteção com visto |
| **Ação Antioxidante / Radicais Livres** | `sparkles` | `<i data-lucide="sparkles"></i>` | Brilho molecular estelar |
| **Articulações / Cartilagens / Ossos** | `bone` / `activity` | `<i data-lucide="bone"></i>` | Estrutura óssea e mobilidade |
| **Coração / Triglicerídeos / Ômega** | `heart-pulse` | `<i data-lucide="heart-pulse"></i>` | Coração com pulsação |
| **Cérebro / Memória / Cognição** | `brain` | `<i data-lucide="brain"></i>` | Cérebro / Conexão neural |
| **Cabelo, Pele e Unhas** | `feather` / `sparkle` | `<i data-lucide="feather"></i>` | Leveza, beleza e vitalidade |
| **Visão / Saúde Ocular** | `eye` | `<i data-lucide="eye"></i>` | Olho com foco |
| **Músculos / Desempenho Físico** | `biceps-flexed` / `dumbbell` | `<i data-lucide="dumbbell"></i>` | Força e recuperação muscular |
| **Sono / Melatonina / Relaxamento** | `moon` | `<i data-lucide="moon"></i>` | Lua / Repouso noturno |
| **Metabolismo Lipídico / Fígado (Colina)** | `droplets` | `<i data-lucide="droplets"></i>` | Equilíbrio lipídico e fluidez |
| **Digestão / Enzimas (Lactase)** | `check-circle-2` | `<i data-lucide="check-circle-2"></i>` | Conforto digestivo |

---

## 5. Tipografia & Paleta de Cores do Design System

### Tipografia Oficial
- **Família Primária:** `Sora` (Google Fonts: 300, 400, 500, 600, 700, 800)
  - Textos institucionais, nomes de produtos, títulos, chamadas e benefícios.
- **Família Técnica (Tabela):** `Arial, Helvetica, sans-serif` ou `Inter`
  - Utilizada na tabela de Informação Nutricional para rigor de conformidade ANVISA.

### Paleta de Cores por Linha do Catálogo

#### 1. Linha BORG (Alta Performance & Nutracêuticos Premium)
- **Azul BORG Principal:** `#0F2C59` (Navy Profundo Sofisticado)
- **Azul Real:** `#175DA9` (Acento e Ícones)
- **Dourado Nobre:** `#D4AF37` / `#C5A059` (Destaque e badges nobres)
- **Grafite Neutro:** `#2D3748`
- **Fundo Base:** `#F8FAFC` com degradê para `#EEF2F6`

#### 2. Linha CARTI MASTER (Saúde Articular, Cartilagem & Ossos)
- **Verde Petróleo / Ciano:** `#006D77` (Identidade Articular)
- **Turquesa Saúde:** `#83C5BE` (Acento de fluidez)
- **Azul Clínico:** `#1D3557` (Tipografia)
- **Laranja Ativo (Variantes PEA/Limão):** `#E76F51`
- **Fundo Base:** `#F6FAF9`

#### 3. Linha CRONOVIT (Vitalidade, Família & Polivitamínicos)
- **Azul Vitalidade:** `#1E3A8A` (Header e Títulos)
- **Amarelo / Dourado Sol:** `#F59E0B` (AZ e Energia)
- **Coral / Laranja Imune:** `#EA580C` (Vitamina C e CDZ)
- **Rosa Mulher:** `#DB2777` (Cronovit Mulher e Crono Mater)
- **Roxo / Uva Kids:** `#7C3AED` (Cronovit BC Kids)
- **Fundo Base:** `#F9FAFB`

#### 4. MARCAS ÚNICAS (Especialidades Clínicas)
- **Complexo Prodiz (Melatonina):** Azul Noite / Índigo Profundo (`#1E1B4B`) + Lavanda (`#C7D2FE`)
- **Epadose (Colina):** Verde Sálvia / Esmeralda Hepático (`#065F46`)
- **Laclaze (Lactase):** Azul Céu Suave (`#0284C7`)
- **Naturedux (Cromo & Quitosana):** Verde Botânico (`#15803D`) + Ouro Queimado (`#B45309`)
- **Malosso & Odessy:** Tons Clínicos Neutros e Dourado

---

## 6. Mapeamento dos 45 Produtos da Planilha por Linha

### Linha BORG (14 Produtos)
1. `514141` — BORG AZ + OMEGA 3 60 CAPS SOFTGEL
2. `521774` — BORG CALCIO 500MG 60 COMPRIMIDOS
3. `500342` — BORG COENZIMA Q10 60 CAPS SOFTGEL
4. `515520` — BORG COG MEMO 60 CAPS SOFTGEL
5. `514554` — BORG FENO GREGO 60 CAPS DURA
6. `503602` — BORG MAGNESIO DIMALATO 60 CAPS DURA
7. `004524` — BORG MAGNESIO PA 60 CAPS DURA
8. `512963` — BORG MAGNESIO TREONATO 60 CAPS DURA
9. `521217` — BORG NAC 60 CAPS DURA
10. `513953` — BORG OMEGA 3 120 CAPS SOFTGEL
11. `513960` — BORG OMEGA 3 240 CAPS SOFTGEL
12. `513977` — BORG OMEGA 3 300 CAPS SOFTGEL
13. `513946` — BORG OMEGA 3 60 CAPS SOFTGEL
14. `950338` — BORG OMEGA 369 60 CAPS SOFTGEL

### Linha CARTI MASTER (6 Produtos)
15. `508737` — CARTI MASTER COL TIPO II + HA 60 CAPS SOFTGEL
16. `509932` — CARTI MASTER COLAG TIPO II+HA 30 CAPS SOFTGEL
17. `508232` — CARTI MASTER CONDROITINA+MSM 60 CAPS DURA
18. `515513` — CARTI MASTER PEA 60 CAPS DURA
19. `504456` — CARTI MASTER SABOR LIMAO 30 SACHES
20. `503725` — CARTI MASTER ULTRA 60 CAPS SOFTGEL

### Linha CRONOVIT (18 Produtos)
21. `503787` — CRONOVIT ARGININA + VIT C 30 CAPS SOFTGEL
22. `001554` — CRONOVIT AZ 60 COMPRIMIDOS
23. `003374` — CRONOVIT BC KIDS 240 ML
24. `001530` — CRONOVIT CALCIO 60 COMPRIMIDOS
25. `515544` — CRONOVIT CDZ SABOR LIMAO+MEL 10 SACHES
26. `515537` — CRONOVIT CDZ SABOR LIMAO+MEL 30 SACHES
27. `001332` — CRONOVIT CRONO MATER 60 CAPS SOFTGEL
28. `001561` — CRONOVIT ENERGY 60 COMPRIMIDOS
29. `505514` — CRONOVIT IMUNE 30 COMPRIMIDOS
30. `505507` — CRONOVIT IMUNE 60 COMPRIMIDOS
31. `001523` — CRONOVIT MULHER 60 COMPRIMIDOS
32. `001547` — CRONOVIT SENIOR 60 COMPRIMIDOS
33. `515568` — CRONOVIT VIT C SABOR LARANJA 10 SACHES
34. `515551` — CRONOVIT VIT C SABOR LARANJA 30 SACHES
35. `503756` — CRONOVIT VITAMINA C 30 CAPS SOFTGEL
36. `503770` — CRONOVIT VITAMINA D 60 CAPS SOFTGEL
37. `503732` — CRONOVIT VITAMINA E 60 CAPS SOFTGEL
38. `503749` — CRONOVIT ZINCO E SELENIO 30 CAPS SOFTGEL

### Marcas Únicas & Outros (7 Produtos)
39. `509567` — COMPLEXO PRODIZ MELATONINA 30 CAPS SOFTGEL
40. `509925` — EPADOSE COLINA 30 COMPRIMIDOS
41. `503817` — LACLAZE 30 CAPS DURA
42. `503763` — MALOSSO 30 COMPRIMIDOS
43. `503503` — NATUREDUX CROMO 60 CAPS SOFTGEL
44. `034579` — NATUREDUX QUITOSANA 60 CAPS DURA
45. `509673` — ODESSY DUO D 30 CAPS SOFTGEL

---

## 7. Próximo Passo: Fluxo de Alimentação Produto a Produto

Assim como realizado na linha VitaMaiz, cada produto terá seu arquivo `.md` estruturado (ex: `data/produtos/514141_borg_az_omega3.md`) contendo:
- Metadados do produto (Código, EAN, Nome da Linha, Nome Comercial, Apresentação)
- Frase de Efeito comercial
- Badges de Destaque
- Benefícios formatados com o nutriente e a ação IN 28 grifada
- Informação Nutricional em tabela padronizada
- Caminho da Imagem do Packshot e da Imagem Conceito
O gerador automatizado converterá cada `.md` em páginas 1920x1080 com a alternância automática entre Página A e Página B!
