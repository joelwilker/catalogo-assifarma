from editor_assets import EDITOR_CSS, EDITOR_BODY_START, EDITOR_BODY_END
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador Automatizado do Catálogo Oficial Assifarma 2026 — Modelo Retrato A4 (210×297mm)
====================================================================================
Lê os 37 arquivos Markdown de rotulagem em:
  /Users/joel/Documents/CATÁLOGO PDF/ASSIFARMA - CATÁLOGO/produtos/md_embalagens
Com agrupamento por Linha de Produto e conformidade integral com a IN 28/2018 (Anvisa).

Atualizações:
  - Alérgenos na cor padrão institucional (sem vermelho)
  - Alegações estritamente conforme a IN 28 na íntegra
  - Padding ampliado na seção de cabeçalho
  - Borg Ômega 3:
      * Palco panorâmico em largura total (2 colunas) com as 3 apresentações (20, 40 e 80 porções)
      * Tabela nutricional com "Porções por Embalagem: 20, 40, 80"
  - Recomendações de uso padronizadas (ex: "02 comprimidos ao dia.")
  - Destaques rápidos padronizados: "Zero Açúcar", "Não contém Glúten", "Não contém Sódio"
  - Ingredientes e ativos importantes destacados em blocos preenchidos com texto branco
  - Rodapé oficial com "INTERCRON / FORHEALTH" e número real de Notificação ANVISA
"""

import os
import re
import sys
import shutil
import colorsys
import unicodedata
from pathlib import Path
from typing import Dict, List, Any, Tuple
from PIL import Image

# ==============================================================================
# 1. DIRETÓRIOS E CAMINHOS DO PROJETO
# ==============================================================================
WORKSPACE_DIR = Path("/Users/joel/Documents/CATÁLOGO PDF/ASSIFARMA - CATÁLOGO")
MD_DIR = WORKSPACE_DIR / "produtos" / "md_embalagens"
OUTPUT_HTML = WORKSPACE_DIR / "catalogo_completo.html"

DRIVE_ASSIFARMA = Path(
    "/Users/joel/Library/CloudStorage/GoogleDrive-forhealth.mkt@gmail.com/"
    "Meu Drive/EMBALAGENS/EMBALAGENS VIGENTES/ASSIFARMA"
)
DRIVE_APRESENTACOES = Path(
    "/Users/joel/Library/CloudStorage/GoogleDrive-forhealth.mkt@gmail.com/"
    "Meu Drive/APRESENTAÇÕES/ASSIFARMA TREINAMENTO/2023 - Assifarma/PÁGINAS/imagens produtos Assifarma/IMAGENS PNG"
)
LOCAL_AMOSTRAS = WORKSPACE_DIR / "Design padrão" / "amostras_design"
LOCAL_EXTRACTED = WORKSPACE_DIR / "Design padrão" / "extracted_assets"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    s = re.sub(r"[\u0300-\u036f]", "", s)
    s = re.sub(r"[^a-zA-Z0-9]+", " ", s).lower().strip()
    return s


# ==============================================================================
# 2. ÍNDICE DE IMAGENS E MOCKUPS
# ==============================================================================
print("Indexando imagens em alta resolução...")
ALL_IMAGES: List[Path] = []
for d in [DRIVE_ASSIFARMA, DRIVE_APRESENTACOES, LOCAL_AMOSTRAS, LOCAL_EXTRACTED]:
    if d.exists():
        for p in d.rglob("*.png"):
            if not p.name.startswith("._") and p.stat().st_size > 15000:
                ALL_IMAGES.append(p)

print(f"Total de imagens candidatas indexadas: {len(ALL_IMAGES)}")

EXACT_IMAGE_MAP: Dict[str, str] = {
    # Borg
    "pagina_01": "BORG/_IMAGENS MOCKUP/CÁLCIO 500MG.png",
    "pagina_02": "BORG/_IMAGENS MOCKUP/COENZIMA Q10.png",
    "pagina_03": "BORG/_IMAGENS MOCKUP/COGMEMO.png",
    "pagina_04": "BORG/_IMAGENS MOCKUP/FENO GREGO -.png",
    "pagina_05": "BORG/_IMAGENS MOCKUP/MAGNÉSIO DIMALATO -.png",
    "pagina_06": "BORG/_IMAGENS MOCKUP/MAGNÉSIO PA -.png",
    "pagina_07": "BORG/_IMAGENS MOCKUP/MAGNÉSIO TREONATO -.png",
    "pagina_08": "BORG/_IMAGENS MOCKUP/NAC.png",
    "pagina_09": "Design padrão/extracted_assets/borg_omega_3_trio.png",
    "pagina_10": "BORG/_IMAGENS MOCKUP/OMEGA 369.png",
    "pagina_11": "BORG/_IMAGENS MOCKUP/ÔMEGA AZ.png",
    # Carti Master
    "pagina_12": "Design padrão/extracted_assets/cartimaster_hialuronico_duo.png",
    "pagina_14": "CARTIMASTER/CARTIMASTER Colágeno Hidrolisado Sachê.png",
    "pagina_15": "CARTIMASTER/CARTIMASTER ULTRA.png",
    "pagina_16": "CARTIMASTER/CARTIMASTER - CONDROITINA + MSM/CARTIMASTER - CONDROITINA + MSM.png",
    # Ceitil
    "pagina_17": "CEITIL 600/CEITIL 600.png",
    # Cronovit
    "pagina_18": "CRONOVIT/Cronocálcio.png",
    "pagina_19": "CRONOVIT/Cronomater.png",
    "pagina_20": "CRONOVIT/CRONOVIT AZ.png",
    "pagina_21": "CRONOVIT/CRONOVIT Mulher.png",
    "pagina_22": "CRONOVIT/CRONOVIT Senior.png",
    "pagina_23": "VITAMINA E@2000x.png",
    # Cronoliv
    "pagina_24": "CRONOLIV/CRONOLIV CABELOS E UNHAS/ANTERIOR II/CRONOLIV CABELOS PELE E UNHAS.png",
    "pagina_25": "CRONOLIV/CRONOLIV COLÁGENO VERISOL/ANTERIOR/CRONOLIV COLÁGENO VERISOL.png",
    "pagina_26": "CRONOLIV/CRONOLIV PRÓPOLIS/ANTERIOR/Cronoliv Propolis.png",
    # Especiais
    "pagina_27": "EPADOSE/COMPRIMIDOS - NOVO/MOCKUP EPADOSE.png",
    "pagina_28": "LACLAZE/ANTERIOR/Laclaze.png",
    "pagina_29": "MALOSSO/ANTERIOR/Malosso.png",
    "pagina_30": "NATUREDUX/NATUREDUX CROMO/ANTERIOR/naturedux cromo.png",
    # Odessy
    "pagina_31": "ODESSY/Odessy Duo D/ODESSY - DUO D.png",
    "pagina_32": "ODESSY/Odessy Fort/ODESSY - FORT.png",
    "pagina_33": "ODESSY/Odessy Tempo/ODESSY - TEMPO.png",
    # Prodiz
    "pagina_34": "PRODIZ/ANTERIOR/PRODIZ.png",
    # Nutrivix
    "pagina_35": "NUTRIVIX/Nutrivix - Coenzima Q10.png",
    "pagina_36": "NUTRIVIX/Nutrivix - Magnésio dimalato.png",
    "pagina_37": "NUTRIVIX/Nutrivix - Magnésio treonato.png",
    # Biomov
    "pagina_38": "BIOMOV/BIOMOV COLÁGENO + AC. HIALURONICO.png",
}


def find_best_image(prefix: str, prod_name: str) -> str:
    pn = norm(prod_name)

    # Caso especial trio Borg Ômega 3
    if "omega 3" in pn and "borg" in pn and "6" not in pn and "az" not in pn:
        trio = WORKSPACE_DIR / "Design padrão" / "extracted_assets" / "borg_omega_3_trio.png"
        if trio.exists():
            return str(trio.resolve())

    # Caso especial Cartimaster + Ácido Hialurônico (duo 30 e 60 cápsulas)
    if "carti" in pn and "hialuronico" in pn:
        duo = WORKSPACE_DIR / "Design padrão" / "extracted_assets" / "cartimaster_hialuronico_duo.png"
        if duo.exists():
            return str(duo.resolve())

    # Casos diretos da linha Cronovit (IMAGENS PNG)
    if "cronovit" in pn and DRIVE_APRESENTACOES.exists():
        crono_png_map = [
            ("arginina", "ARGININA@2000x.png"),
            ("bc kids", "BC KIDS@2000x.png"),
            ("imune", "IMUNE1@2000x.png"),
            ("zinco", "C ZN SEL@2000x.png"),
            ("vitamina d", "VITAMINA D@2000x.png"),
            ("vitamina c", "VITAMINA C1@2000x.png"),
        ]
        for kw, fname in crono_png_map:
            if kw in pn:
                cand = DRIVE_APRESENTACOES / fname
                if cand.exists():
                    return str(cand.resolve())

    # Imagens da Linha Borg (pasta _IMAGENS MOCKUP)
    if "borg" in pn:
        borg_local = WORKSPACE_DIR / "Design padrão" / "extracted_assets" / "borg"
        borg_drive = DRIVE_ASSIFARMA / "BORG" / "_IMAGENS MOCKUP"
        for bdir in [borg_local, borg_drive]:
            if bdir.exists():
                for p in bdir.glob("*.png"):
                    p_stem = norm(p.stem)
                    if "calcio" in pn and "calcio" in p_stem:
                        return str(p.resolve())
                    if "coenzima" in pn and "coenzima" in p_stem:
                        return str(p.resolve())
                    if "cog" in pn and "cog" in p_stem:
                        return str(p.resolve())
                    if "feno" in pn and "feno" in p_stem:
                        return str(p.resolve())
                    if "dimalato" in pn and "dimalato" in p_stem:
                        return str(p.resolve())
                    if ("magnesio pa" in pn or "magnesio p a" in pn) and "pa" in p_stem:
                        return str(p.resolve())
                    if "treonato" in pn and "treonato" in p_stem:
                        return str(p.resolve())
                    if ("nac" in pn or "n a c" in pn) and "nac" in p_stem:
                        return str(p.resolve())
                    if ("3 6 9" in pn or "369" in pn) and "369" in p_stem:
                        return str(p.resolve())
                    if "az" in pn and "az" in p_stem:
                        return str(p.resolve())

    if prefix in EXACT_IMAGE_MAP:
        sub = EXACT_IMAGE_MAP[prefix]
        p_direct = WORKSPACE_DIR / sub
        if p_direct.exists():
            return str(p_direct.resolve())
        p1 = DRIVE_ASSIFARMA / sub
        if p1.exists():
            return str(p1.resolve())
        sub_norm = norm(Path(sub).name)
        for img in ALL_IMAGES:
            if norm(img.name) == sub_norm:
                return str(img.resolve())

    tokens = [t for t in pn.split() if len(t) > 2 and t not in ["capsulas", "comprimidos", "softgel", "dura"]]
    for p in ALL_IMAGES:
        p_norm = norm(p.stem)
        if all(t in p_norm for t in tokens):
            return str(p.resolve())

    return str((LOCAL_AMOSTRAS / "hi_packshot_az_transparent.png").resolve())


# ==============================================================================
# 3. CONHECIMENTO REGULATÓRIO OFICIAL: ATIVOS E ALEGAÇÕES DA IN 28/2018
# ==============================================================================
PRODUCT_KNOWLEDGE = {
    "Borg AZ Ômega": {
        "key_actives": [
            "22 Vitaminas e Minerais Essenciais",
            "Ômega 3 Concentrado (EPA e DHA)",
        ],
        "in28_claims": [
            "Os ácidos graxos ômega 3 EPA e DHA auxiliam na redução dos triglicerídeos.",
            "As vitaminas A, B6, B12, C, D, o ácido fólico, cobre, ferro, selênio e zinco auxiliam no funcionamento do sistema imune.",
            "As vitaminas do complexo B, ferro, magnésio e manganês auxiliam no metabolismo energético.",
            "As vitaminas B2, C, E, cobre, manganês, selênio e zinco são antioxidantes que auxiliam na proteção dos danos causados pelos radicais livres.",
        ],
    },
    "Borg Coenzima Q10": {
        "key_actives": [
            "Coenzima Q10 100mg por porção",
            "Licopeno 5mg • Óleo de Semente de Uva",
            "Vitaminas A, C, E e Zinco Quelato",
        ],
        "in28_claims": [
            "A vitamina E, a vitamina C e o zinco são antioxidantes que auxiliam na proteção dos danos causados pelos radicais livres.",
            "O zinco, a vitamina C e a vitamina A auxiliam no funcionamento do sistema imune.",
            "A vitamina A contribui para a manutenção da pele.",
            "O zinco contribui para a manutenção do cabelo, da pele e das unhas.",
        ],
    },
    "Borg Cog Memo": {
        "key_actives": [
            "Fosfatidilserina • Cafeína Anidra",
            "Colina • Vitaminas B1, B6 e B12",
        ],
        "in28_claims": [
            "A cafeína auxilia no aumento do estado de alerta e na melhora da concentração.",
            "A colina contribui para o metabolismo lipídico e para o metabolismo da homocisteína.",
            "As vitaminas B1, B6 e B12 auxiliam no metabolismo energético e na função normal do sistema nervoso.",
            "A vitamina B6 e a vitamina B12 auxiliam na formação das células vermelhas do sangue.",
        ],
    },
    "Borg Cálcio 500mg": {
        "key_actives": [
            "Carbonato de Cálcio 500mg",
        ],
        "in28_claims": [
            "O cálcio auxilia na formação e manutenção de ossos e dentes.",
            "O cálcio auxilia no funcionamento muscular e neuromuscular.",
            "O cálcio auxilia no metabolismo energético.",
            "O cálcio auxilia no processo de divisão celular.",
        ],
    },
    "Borg Feno Grego": {
        "key_actives": [
            "Extrato de Semente de Feno Grego (Trigonella foenum-graecum L.) 300mg",
            "Zinco Quelato • Vitamina B6",
        ],
        "in28_claims": [
            "O zinco auxilia na síntese de proteínas e no metabolismo de proteínas, carboidratos e gorduras.",
            "O zinco auxilia no funcionamento do sistema imune.",
            "A vitamina B6 auxilia no metabolismo energético e no metabolismo de proteínas e do glicogênio.",
        ],
    },
    "Borg Magnésio Dimalato": {
        "key_actives": [
            "Magnésio Dimalato 260mg",
        ],
        "in28_claims": [
            "O magnésio auxilia no funcionamento muscular e neuromuscular.",
            "O magnésio auxilia no metabolismo energético e no equilíbrio dos eletrólitos.",
            "O magnésio auxilia no metabolismo de proteínas, carboidratos e gorduras.",
            "O magnésio auxilia na formação de ossos e dentes e no processo de divisão celular.",
        ],
    },
    "Borg Magnésio P.A.": {
        "key_actives": [
            "Cloreto de Magnésio P.A. 260mg",
        ],
        "in28_claims": [
            "O magnésio auxilia no funcionamento muscular e neuromuscular.",
            "O magnésio auxilia no metabolismo energético e no equilíbrio dos eletrólitos.",
            "O magnésio auxilia no metabolismo de proteínas, carboidratos e gorduras.",
            "O magnésio auxilia na formação de ossos e dentes.",
        ],
    },
    "Borg Magnésio Treonato": {
        "key_actives": [
            "Magnésio L-Treonato 260mg",
        ],
        "in28_claims": [
            "O magnésio auxilia no funcionamento neuromuscular.",
            "O magnésio auxilia no funcionamento muscular.",
            "O magnésio auxilia no metabolismo energético e no equilíbrio dos eletrólitos.",
            "O magnésio auxilia no processo de divisão celular.",
        ],
    },
    "Borg NAC 600mg": {
        "key_actives": [
            "N-Acetil L-Cisteína (NAC) 600mg",
            "Vitamina C 45mg • Zinco Quelato 7mg",
        ],
        "in28_claims": [
            "A vitamina C e o zinco são antioxidantes que auxiliam na proteção dos danos causados pelos radicais livres.",
            "A vitamina C e o zinco auxiliam no funcionamento do sistema imune.",
            "O zinco auxilia no metabolismo de proteínas, carboidratos e gorduras.",
            "A vitamina C auxilia no metabolismo energético.",
        ],
    },
    "Borg Ômega 3": {
        "key_actives": [
            "Óleo de Peixe 1000mg por cápsula (Certificação MEG-3®)",
            "EPA 540mg • DHA 360mg (porção de 3 cápsulas)",
        ],
        "in28_claims": [
            "Os ácidos graxos ômega 3 EPA e DHA auxiliam na redução dos triglicerídeos.",
            "O EPA e o DHA contribuem para o normal funcionamento do coração.",
        ],
    },
    "Borg Ômega 3, 6, 9": {
        "key_actives": [
            "Óleo de Peixe (Ômega 3) • Óleo de Linhaça (Ômega 6) • Óleo de Borragem (Ômega 9)",
            "Vitamina E (DL-Alfa-Tocoferol) 10mg",
        ],
        "in28_claims": [
            "Os ácidos graxos ômega 3 EPA e DHA auxiliam na redução dos triglicerídeos.",
            "A vitamina E é um antioxidante que auxilia na proteção dos danos causados pelos radicais livres.",
        ],
    },
    "Carti Master Colágeno Hidrolisado Sabor Limão": {
        "key_actives": [
            "Colágeno Hidrolisado 9g por sachê",
            "Vitamina C 45mg • Sabor Limão",
        ],
        "in28_claims": [
            "A vitamina C auxilia na formação do colágeno.",
            "A vitamina C é um antioxidante que auxilia na proteção dos danos causados pelos radicais livres.",
            "A vitamina C auxilia no metabolismo energético e no funcionamento do sistema imune.",
        ],
    },
    "Carti Master Colágeno Tipo II + Ácido Hialurônico": {
        "key_actives": [
            "Colágeno com Colágeno Tipo II Não Desnaturado 40mg",
            "Hialuronato de Sódio (Ácido Hialurônico) 80mg",
        ],
        "in28_claims": [
            "O colágeno tipo II não desnaturado auxilia na manutenção da função articular.",
        ],
    },
    "Carti Master Condroitina + MSM": {
        "key_actives": [
            "Sulfato de Condroitina 400mg",
            "Metilsulfonilmetano (MSM) 900mg",
            "Colecalciferol (Vitamina D3) 2.000 UI",
        ],
        "in28_claims": [
            "A vitamina D auxilia na absorção de cálcio e fósforo e na manutenção de níveis de cálcio no sangue.",
            "A vitamina D auxilia na formação de ossos e dentes.",
            "A vitamina D auxilia no funcionamento muscular e no funcionamento do sistema imune.",
        ],
    },
    "Carti Master Ultra": {
        "key_actives": [
            "Colágeno Tipo II Não Desnaturado 40mg",
            "Metilsulfonilmetano (MSM) • Vitamina E 10mg",
        ],
        "in28_claims": [
            "O colágeno tipo II não desnaturado auxilia na manutenção da função articular.",
            "A vitamina E é um antioxidante que auxilia na proteção dos danos causados pelos radicais livres.",
        ],
    },
    "Ceitil Acetilcisteína": {
        "key_actives": [
            "N-Acetil L-Cisteína (Acetilcisteína) 600mg",
            "Vitamina C 45mg • Vitamina D 2.000 UI • Zinco 7mg",
        ],
        "in28_claims": [
            "A vitamina C e o zinco são antioxidantes que auxiliam na proteção dos danos causados pelos radicais livres.",
            "As vitaminas C, D e o zinco auxiliam no funcionamento do sistema imune.",
            "A vitamina D auxilia no funcionamento muscular.",
        ],
    },
    "Cronovit Cálcio": {
        "key_actives": [
            "Carbonato de Cálcio 600mg",
            "Colecalciferol (Vitamina D3) 200 UI",
        ],
        "in28_claims": [
            "O cálcio e a vitamina D auxiliam na formação e manutenção de ossos e dentes.",
            "A vitamina D auxilia na absorção de cálcio e fósforo.",
            "O cálcio e a vitamina D auxiliam no funcionamento muscular e neuromuscular.",
            "A vitamina D auxilia no funcionamento do sistema imune.",
        ],
    },
    "Cronovit Crono Mater": {
        "key_actives": [
            "Ácido Fólico (L-Metilfolato de Cálcio) 400mcg",
            "Ferro Bisglicinato 27mg • Ômega 3 (DHA 200mg)",
            "Polivitamínico e Polimineral Gestacional",
        ],
        "in28_claims": [
            "O ácido fólico auxilia na formação do tubo neural do feto durante a gravidez.",
            "O ácido fólico, o ferro e as vitaminas B6 e B12 auxiliam na formação das células vermelhas do sangue.",
            "O ferro auxilia no transporte do oxigênio no organismo.",
            "As vitaminas B6, B12, C, D e o zinco auxiliam no funcionamento do sistema imune.",
        ],
    },
    "Cronovit de A-Z": {
        "key_actives": [
            "Polivitamínico e Polimineral com 22 Nutrientes",
        ],
        "in28_claims": [
            "As vitaminas A, B6, B12, C, D, o ácido fólico, cobre, ferro, selênio e zinco auxiliam no funcionamento do sistema imune.",
            "As vitaminas B1, B2, B3, B5, B6, B12, C, cobre, ferro, iodo, magnésio e manganês auxiliam no metabolismo energético.",
            "As vitaminas B2, C, E, cobre, manganês, selênio e zinco são antioxidantes que auxiliam na proteção dos danos causados pelos radicais livres.",
        ],
    },
    "Cronovit Mulher": {
        "key_actives": [
            "Fórmula Feminina com Biotina e Ácido Fólico",
            "Ferro Quelato • Zinco • Complexo B",
        ],
        "in28_claims": [
            "A biotina e o zinco contribuem para a manutenção do cabelo e da pele.",
            "O ácido fólico e o ferro auxiliam na formação das células vermelhas do sangue.",
            "As vitaminas A, B6, B12, C, D e o zinco auxiliam no funcionamento do sistema imune.",
            "As vitaminas B1, B2, B3, B5, B6, B12 e o ferro auxiliam no metabolismo energético.",
        ],
    },
    "Cronovit Sênior": {
        "key_actives": [
            "Fórmula Especial 50+ com Luteína",
            "Cálcio • Vitamina D3 • Selênio • Zinco",
        ],
        "in28_claims": [
            "O cálcio e a vitamina D auxiliam na manutenção de ossos e dentes e no funcionamento muscular.",
            "A vitamina A, a riboflavina e o zinco auxiliam na visão.",
            "As vitaminas C, E, o selênio e o zinco são antioxidantes que auxiliam na proteção dos danos causados pelos radicais livres.",
            "As vitaminas B6, B12, C, D e o zinco auxiliam no funcionamento do sistema imune.",
        ],
    },
    "Cronovit Vitamina E 400 UI": {
        "key_actives": [
            "DL-Alfa-Tocoferol (Vitamina E) 400 UI (268mg)",
        ],
        "in28_claims": [
            "A vitamina E é um antioxidante que auxilia na proteção dos danos causados pelos radicais livres.",
        ],
    },
    "Cronoliv Cabelo, Pele e Unhas": {
        "key_actives": [
            "Biotina (Vitamina B7) • Zinco Quelato",
            "Vitaminas do Complexo B • Vitamina C",
        ],
        "in28_claims": [
            "A biotina contribui para a manutenção do cabelo e da pele.",
            "O zinco contribui para a manutenção do cabelo, da pele e das unhas.",
            "A vitamina C e o zinco são antioxidantes que auxiliam na proteção dos danos causados pelos radicais livres.",
            "A vitamina C auxilia na formação do colágeno e no metabolismo energético.",
        ],
    },
    "Cronoliv Colágeno Verisol®": {
        "key_actives": [
            "Peptídeos Bioativos de Colágeno Hidrolisado Verisol® 2,5g",
            "Biotina • Vitamina C • Ácido Hialurônico",
        ],
        "in28_claims": [
            "Os peptídeos bioativos de colágeno hidrolisado com peso molecular médio de 2kDa auxiliam na manutenção da saúde da pele.",
            "A vitamina C auxilia na formação do colágeno.",
            "A biotina contribui para a manutenção do cabelo e da pele.",
            "A vitamina C é um antioxidante que auxilia na proteção dos danos causados pelos radicais livres.",
        ],
    },
    "Cronoliv Própolis": {
        "key_actives": [
            "Extrato de Própolis Verde Padronizado",
            "Vitamina C 45mg • Vitamina E 10mg • Zinco 7mg",
        ],
        "in28_claims": [
            "A vitamina C, a vitamina E e o zinco são antioxidantes que auxiliam na proteção dos danos causados pelos radicais livres.",
            "A vitamina C e o zinco auxiliam no funcionamento do sistema imune.",
        ],
    },
    "Nutrivix Coenzima Q10": {
        "key_actives": [
            "Coenzima Q10 100mg por porção",
            "Vitamina E (DL-Alfa-Tocoferol) 10mg",
        ],
        "in28_claims": [
            "A vitamina E é um antioxidante que auxilia na proteção dos danos causados pelos radicais livres.",
        ],
    },
    "Nutrivix Magnésio Dimalato": {
        "key_actives": [
            "Magnésio Dimalato 260mg",
        ],
        "in28_claims": [
            "O magnésio auxilia no funcionamento muscular e neuromuscular.",
            "O magnésio auxilia no metabolismo energético e no equilíbrio dos eletrólitos.",
            "O magnésio auxilia no metabolismo de proteínas, carboidratos e gorduras.",
            "O magnésio auxilia na formação de ossos e dentes e no processo de divisão celular.",
        ],
    },
    "Nutrivix Magnésio Treonato": {
        "key_actives": [
            "Magnésio L-Treonato 260mg",
        ],
        "in28_claims": [
            "O magnésio auxilia no funcionamento neuromuscular.",
            "O magnésio auxilia no funcionamento muscular.",
            "O magnésio auxilia no metabolismo de proteínas, carboidratos e gorduras.",
            "O magnésio auxilia no processo de divisão celular.",
        ],
    },
    "Odessy Duo D": {
        "key_actives": [
            "Colecalciferol (Vitamina D3) 2.000 UI",
            "Menaquinona-7 (Vitamina K2 / MK-7) 65mcg",
        ],
        "in28_claims": [
            "A vitamina D auxilia na formação de ossos e dentes e na absorção de cálcio e fósforo.",
            "A vitamina D auxilia no funcionamento do sistema imune e no funcionamento muscular.",
            "A vitamina K auxilia na coagulação do sangue e na manutenção dos ossos.",
        ],
    },
    "Odessy Fort": {
        "key_actives": [
            "Complexo Fortificante com Silício Quelato",
            "Biotina • Zinco Quelato • Vitaminas C e E",
        ],
        "in28_claims": [
            "A biotina e o zinco contribuem para a manutenção do cabelo e da pele.",
            "O zinco contribui para a manutenção das unhas.",
            "As vitaminas C, E e o zinco são antioxidantes que auxiliam na proteção dos danos causados pelos radicais livres.",
            "A vitamina C auxilia na formação do colágeno e no metabolismo energético.",
        ],
    },
    "Odessy Tempo": {
        "key_actives": [
            "Cafeína Anidra • Taurina",
            "Vitaminas do Complexo B • Vitamina C",
        ],
        "in28_claims": [
            "A cafeína auxilia no aumento do estado de alerta e na melhora da concentração.",
            "As vitaminas B1, B2, B3, B6 e B12 auxiliam no metabolismo energético.",
            "A vitamina C é um antioxidante que auxilia na proteção dos danos causados pelos radicais livres.",
        ],
    },
    "Biomov Colágeno Tipo II + Ácido Hialurônico": {
        "key_actives": [
            "Colágeno Tipo II Não Desnaturado 40mg",
            "Ácido Hialurônico 80mg",
        ],
        "in28_claims": [
            "O colágeno tipo II não desnaturado auxilia na manutenção da função articular.",
        ],
    },
    "Complexo Prodiz Melatonina": {
        "key_actives": [
            "Melatonina 0,21mg em Cápsula Softgel",
            "Vitamina B6 (Piridoxina) 1,3mg",
        ],
        "in28_claims": [
            "A vitamina B6 auxilia no funcionamento do sistema imune e no metabolismo energético.",
            "A vitamina B6 auxilia no metabolismo de proteínas, carboidratos e gorduras.",
            "A vitamina B6 auxilia no metabolismo de proteínas e do glicogênio.",
        ],
    },
    "Epadose Colina": {
        "key_actives": [
            "Citrato de Colina • DL-Metionina",
            "Vitaminas B1, B6 e B12",
        ],
        "in28_claims": [
            "A colina contribui para o metabolismo lipídico.",
            "A colina contribui para o metabolismo da homocisteína.",
            "As vitaminas B1, B6 e B12 auxiliam no metabolismo energético e na função normal do sistema nervoso.",
        ],
    },
    "Laclaze Lactase 10.000 U.FCC": {
        "key_actives": [
            "Enzima Lactase de Aspergillus oryzae 10.000 U.FCC",
        ],
        "in28_claims": [
            "A lactase auxilia na digestão da lactose.",
        ],
    },
    "Malosso Citrato Malato de Cálcio": {
        "key_actives": [
            "Citrato Malato de Cálcio 250mg",
            "Colecalciferol (Vitamina D3) 200 UI",
        ],
        "in28_claims": [
            "O cálcio auxilia na formação e manutenção de ossos e dentes.",
            "A vitamina D auxilia na absorção de cálcio e fósforo e na manutenção de níveis de cálcio no sangue.",
            "O cálcio e a vitamina D auxiliam no funcionamento muscular e neuromuscular.",
            "A vitamina D auxilia no funcionamento do sistema imune.",
        ],
    },
    "Naturedux Cromo": {
        "key_actives": [
            "Picolinato de Cromo 250mcg",
            "Vitamina E 10mg • Zinco Quelato 7mg",
        ],
        "in28_claims": [
            "O cromo auxilia no metabolismo de proteínas, carboidratos e gorduras.",
            "O zinco e a vitamina E são antioxidantes que auxiliam na proteção dos danos causados pelos radicais livres.",
            "O zinco auxilia no funcionamento do sistema imune.",
        ],
    },
}


# ==============================================================================
# 4. EXTRAÇÃO DINÂMICA DE CORES DA IMAGEM DO PRODUTO (PIL)
# ==============================================================================
def extract_palette_from_image(img_path: str, linha: str) -> Dict[str, str]:
    r, g, b = 23, 93, 169
    try:
        im = Image.open(img_path).convert("RGBA")
        im.thumbnail((120, 120))
        pixels = list(im.getdata())

        candidates = []
        for pr, pg, pb, pa in pixels:
            if pa < 120:
                continue
            h, s, v = colorsys.rgb_to_hsv(pr / 255.0, pg / 255.0, pb / 255.0)
            if s < 0.22 or v < 0.16 or (v > 0.94 and s < 0.26):
                continue
            weight = s * (v ** 0.5)
            candidates.append(((pr, pg, pb), weight, h))

        if candidates:
            buckets: Dict[int, Dict[str, Any]] = {}
            for (pr, pg, pb), weight, h in candidates:
                b_idx = int(h * 24) % 24
                if b_idx not in buckets:
                    buckets[b_idx] = {"weight": 0.0, "r": 0, "g": 0, "b": 0, "cnt": 0}
                buckets[b_idx]["weight"] += weight
                buckets[b_idx]["r"] += pr
                buckets[b_idx]["g"] += pg
                buckets[b_idx]["b"] += pb
                buckets[b_idx]["cnt"] += 1

            best = max(buckets.values(), key=lambda x: x["weight"])
            r = int(best["r"] / best["cnt"])
            g = int(best["g"] / best["cnt"])
            b = int(best["b"] / best["cnt"])
    except Exception:
        pass

    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    s_adj = max(0.55, min(0.95, s * 1.15))
    v_adj = max(0.42, min(0.82, v))
    r_adj, g_adj, b_adj = colorsys.hsv_to_rgb(h, s_adj, v_adj)
    r_main, g_main, b_main = int(r_adj * 255), int(g_adj * 255), int(b_adj * 255)

    v_dark = max(0.20, v_adj * 0.45)
    r_d, g_d, b_d = colorsys.hsv_to_rgb(h, s_adj, v_dark)
    r_dark, g_dark, b_dark = int(r_d * 255), int(g_d * 255), int(b_d * 255)

    v_darker = max(0.10, v_dark * 0.55)
    r_dr, g_dr, b_dr = colorsys.hsv_to_rgb(h, s_adj, v_darker)
    r_darker, g_darker, b_darker = int(r_dr * 255), int(g_dr * 255), int(b_dr * 255)

    v_light = 0.98
    s_light = 0.12
    r_l, g_l, b_l = colorsys.hsv_to_rgb(h, s_light, v_light)
    r_light, g_light, b_light = int(r_l * 255), int(g_l * 255), int(b_l * 255)

    hex_main = f"#{r_main:02x}{g_main:02x}{b_main:02x}"
    hex_dark = f"#{r_dark:02x}{g_dark:02x}{b_dark:02x}"
    hex_darker = f"#{r_darker:02x}{g_darker:02x}{b_darker:02x}"
    hex_light = f"#{r_light:02x}{g_light:02x}{b_light:02x}"

    header_grad = f"linear-gradient(135deg, {hex_darker} 0%, {hex_dark} 45%, {hex_main} 100%)"
    page_bg = f"linear-gradient(160deg, rgba({r_main}, {g_main}, {b_main}, 0.04) 0%, #ffffff 45%, rgba({r_main}, {g_main}, {b_main}, 0.08) 100%)"
    stage_grad = (
        f"radial-gradient(circle at 50% 42%, rgba(255, 255, 255, 0.98) 0%, "
        f"rgba({r_light}, {g_light}, {b_light}, 0.6) 58%, rgba({r_main}, {g_main}, {b_main}, 0.22) 100%)"
    )
    glass_border = f"rgba({r_main}, {g_main}, {b_main}, 0.24)"
    box_grad = (
        f"linear-gradient(135deg, rgba({r_main}, {g_main}, {b_main}, 0.12) 0%, "
        f"rgba({r_light}, {g_light}, {b_light}, 0.65) 100%)"
    )

    return {
        "theme_color": hex_main,
        "theme_dark": hex_dark,
        "theme_light": hex_light,
        "page_bg": page_bg,
        "header_grad": header_grad,
        "stage_grad": stage_grad,
        "glass_border": glass_border,
        "box_grad": box_grad,
    }


# ==============================================================================
# 5. PARSER DOS ARQUIVOS MARKDOWN E NORMALIZAÇÃO DE RECOMENDAÇÃO
# ==============================================================================
def clean_recommendation(rec: str) -> str:
    """Padroniza a recomendação de uso (ex: 02 comprimidos ao dia.)."""
    rec = re.sub(r"^(?:recomenda-se a ingest[aã]o de|tomar|ingerir|consumir)\s*", "", rec, flags=re.IGNORECASE)
    rec = re.sub(
        r",?\s*(?:para\s+pessoas\s+com\s+idade|para\s+adultos?|para\s+pessoas|adultos?|com\s+idade\s+igual\s+ou\s+superior\s+a\s+19\s+anos|pessoas\s+com\s+idade\s+igual\s+ou\s+superior\s+a\s+19\s+anos|maiores\s+de\s+19\s+anos|≥\s*19\s*anos)[^.]*",
        "",
        rec,
        flags=re.IGNORECASE,
    ).strip()
    rec = re.sub(r"^[,\s\-\.]+", "", rec).strip()
    rec = re.sub(r",?\s*para$", "", rec, flags=re.IGNORECASE).strip()

    rec = re.sub(r"0?1\s*\((?:um|uma)\)", "01", rec, flags=re.IGNORECASE)
    rec = re.sub(r"0?2\s*\((?:dois|duas)\)", "02", rec, flags=re.IGNORECASE)
    rec = re.sub(r"0?3\s*\((?:tr[eê]s)\)", "03", rec, flags=re.IGNORECASE)
    rec = re.sub(r"0?4\s*\((?:quatro)\)", "04", rec, flags=re.IGNORECASE)
    rec = re.sub(r"\b1\b(?=\s*(?:comprimido|c[aá]psula|sach[eê]))", "01", rec)
    rec = re.sub(r"\b2\b(?=\s*(?:comprimido|c[aá]psula|sach[eê]))", "02", rec)
    rec = re.sub(r"\b3\b(?=\s*(?:comprimido|c[aá]psula|sach[eê]))", "03", rec)
    rec = re.sub(r"\b4\b(?=\s*(?:comprimido|c[aá]psula|sach[eê]))", "04", rec)
    rec = re.sub(r"uma\s+c[aá]psula", "01 cápsula", rec, flags=re.IGNORECASE)
    rec = re.sub(r"duas\s+vezes\s+ao\s+dia", "2 vezes ao dia", rec, flags=re.IGNORECASE)

    if "lactose" in rec.lower():
        rec = "01 cápsula antes de cada refeição com lactose"
    elif "dormir" in rec.lower():
        rec = "01 cápsula ao dia, antes de dormir"

    rec = rec.rstrip(".") + "."
    if len(rec) > 1:
        rec = rec[0].upper() + rec[1:]
    return rec


def parse_md(path: Path) -> Dict[str, Any]:
    txt = path.read_text(encoding="utf-8")
    fm: Dict[str, str] = {}
    body = txt
    if txt.startswith("---"):
        parts = txt.split("---", 2)
        if len(parts) >= 3:
            for l in parts[1].strip().splitlines():
                if ":" in l:
                    k, v = l.split(":", 1)
                    fm[k.strip()] = v.strip().strip('"').strip("'")
            body = parts[2]

    denominacao = ""
    m_den = re.search(r"-\s*Denominação de venda:\s*(.+)", body, re.IGNORECASE)
    if m_den:
        denominacao = m_den.group(1).strip().upper()

    destaques: List[str] = []
    m_dest = re.search(r"-\s*Destaques frontais:\s*(.+)", body, re.IGNORECASE)
    if m_dest:
        destaques = [d.strip() for d in m_dest.group(1).split(",") if d.strip()]

    via_uso = "Via Oral • Uso Adulto (≥ 19 anos)"
    m_via = re.search(r"-\s*Via e uso:\s*(.+)", body, re.IGNORECASE)
    if m_via:
        via_uso = m_via.group(1).strip()

    porcoes_emb = "60 porções"
    m_pe = re.search(r"Porções por embalagem:\s*(.+)", body, re.IGNORECASE)
    if m_pe:
        porcoes_emb = m_pe.group(1).strip()

    porcao = "1 comprimido"
    m_p = re.search(r"Porção:\s*(.+)", body, re.IGNORECASE)
    if m_p:
        porcao = m_p.group(1).strip()

    table_rows: List[List[str]] = []
    lines = body.splitlines()
    in_table = False
    for l in lines:
        if l.strip().startswith("|") and ("---" not in l):
            cells = [c.strip() for c in l.strip("|").split("|")]
            if len(cells) >= 2:
                if not in_table and ("informação" in cells[0].lower() or "nutriente" in cells[0].lower()):
                    in_table = True
                    continue
                if in_table:
                    c0 = cells[0]
                    c1 = cells[1] if len(cells) > 1 else ""
                    c2 = cells[2] if len(cells) > 2 else "0"
                    table_rows.append([c0, c1, c2])
        elif in_table and not l.strip().startswith("|"):
            in_table = False

    insignificant = (
        "Não contém quantidades significativas de Valor energético, Carboidratos, "
        "Açúcares totais, Açúcares adicionados, Proteínas, Gorduras totais, "
        "Gorduras saturadas, Gorduras trans, Fibras alimentares e Sódio."
    )
    m_ins = re.search(r"(Não contém quantidades significativas[^.\n]+\.?)", body, re.IGNORECASE)
    if m_ins:
        insignificant = m_ins.group(1).strip()

    ingredientes = ""
    m_ing = re.search(r"\*\*INGREDIENTES:\*\*\s*(.+?)(?=\n\n\*\*|\n\*\*ALÉRGICOS|$)", body, re.DOTALL | re.IGNORECASE)
    if m_ing:
        ingredientes = " ".join(m_ing.group(1).split())

    alergicos = ""
    m_ale = re.search(r"\*\*ALÉRGICOS:\*\*\s*(.+?)(?=\n\n\*\*|\n\*\*RECOMENDAÇÃO|$)", body, re.DOTALL | re.IGNORECASE)
    if m_ale:
        alergicos = " ".join(m_ale.group(1).split())

    recomendacao = "01 comprimido ao dia."
    m_rec = re.search(r"\*\*RECOMENDAÇÃO DE USO:\*\*\s*(.+?)(?=\n\n\*\*|\n\*\*ADVERTÊNCIAS|$)", body, re.DOTALL | re.IGNORECASE)
    if m_rec:
        rec_text = " ".join(m_rec.group(1).split())
        recomendacao = clean_recommendation(rec_text.replace("Recomendações de uso:", "").replace("Recomendação de uso:", "").strip())

    advertencias = (
        "ESTE PRODUTO NÃO É UM MEDICAMENTO. NÃO EXCEDER A RECOMENDAÇÃO DIÁRIA DE CONSUMO "
        "INDICADA NA EMBALAGEM. MANTENHA FORA DO ALCANCE DE CRIANÇAS."
    )
    conservacao = (
        "Conservar ao abrigo da luz, calor e umidade. Após aberto, consumir em até 60 dias."
    )
    m_adv = re.search(r"\*\*ADVERTÊNCIAS E CONSERVAÇÃO:\*\*\s*(.+?)(?=\n\n\*\*|\n\*\*ALEGAÇÕES|$)", body, re.DOTALL | re.IGNORECASE)
    if m_adv:
        adv_text = " ".join(m_adv.group(1).split())
        if "CUIDADOS DE CONSERVAÇÃO:" in adv_text:
            p1, p2 = adv_text.split("CUIDADOS DE CONSERVAÇÃO:", 1)
            advertencias = p1.strip()
            conservacao = p2.strip()
        else:
            advertencias = adv_text.strip()

    # Remover frase redundante de público-alvo no início do corpo de advertências (já consta no topo da página)
    advertencias = re.sub(
        r"^PRODUTO\s+(?:DESTINADO|INDICADO)\s+A\s+[^\.]+\.\s*",
        "",
        advertencias,
        flags=re.IGNORECASE,
    ).strip()

    alegacoes: List[str] = []
    m_aleg = re.search(r"\*\*ALEGAÇÕES DO RÓTULO:\*\*\s*(.+?)(?=\n## 4|$)", body, re.DOTALL | re.IGNORECASE)
    if m_aleg:
        for al in m_aleg.group(1).splitlines():
            al_s = al.strip()
            if al_s.startswith("-") or al_s.startswith("*"):
                alegacoes.append(al_s.lstrip("-* ").strip())

    return {
        "fm": fm,
        "denominacao": denominacao,
        "destaques": destaques,
        "via_uso": via_uso,
        "porcoes_emb": porcoes_emb,
        "porcao": porcao,
        "table_rows": table_rows,
        "insignificant": insignificant,
        "ingredientes": ingredientes,
        "alergicos": alergicos,
        "recomendacao": recomendacao,
        "advertencias": advertencias,
        "conservacao": conservacao,
        "alegacoes": alegacoes,
    }


# ==============================================================================
# 6. IDENTIFICAÇÃO E NOTIFICAÇÃO SANITÁRIA ANVISA
# ==============================================================================
NOTIF_SPECIFIC_MAP = {
    "Borg Cog Memo": "25351.146915/2026-59",
    "Cronovit de A-Z": "25351.165967/2026-24",
    "Cronovit Sênior": "25351.165967/2026-24",
    "Cronoliv Própolis": "25351.189958/2025-48",
}


def format_notification(pname: str, pdata: Dict[str, Any]) -> Tuple[str, str]:
    """Retorna (título_notificação, valor_formatado) para o rodapé oficial."""
    for k, v in NOTIF_SPECIFIC_MAP.items():
        if k.lower() in pname.lower():
            return ("Notificação ANVISA", f"Nº {v}")

    full_text = str(pdata)
    nums = re.findall(r"25351[0-9.\/\-]+", full_text)
    if nums:
        raw_num = nums[0].rstrip(".")
        clean = re.sub(r"[^0-9]", "", raw_num)
        if len(clean) == 17:
            formatted = f"{clean[:5]}.{clean[5:11]}/{clean[11:15]}-{clean[15:]}"
            return ("Notificação ANVISA", f"Nº {formatted}")
        elif len(clean) == 15 and clean.startswith("253510548202584"):
            return ("Notificação ANVISA", "Nº 25351.054820/2025-84")
        elif "/" in raw_num and "." in raw_num:
            return ("Notificação ANVISA", f"Nº {raw_num}")

    return ("Notificação ANVISA", "RDC nº 240/2018")


# ==============================================================================
# 7. ORDENAÇÃO POR LINHA DE PRODUTO
# ==============================================================================
LINE_ORDER = [
    "borg",
    "cronovit",
    "cronoliv",
    "carti master",
    "nutrivix",
    "biomov",
    "ceitil",
    "complexo prodiz",
    "prodiz",
    "epadose",
    "laclaze",
    "malosso",
    "naturedux",
]


def get_product_sort_key(f: Path) -> Tuple[int, str, str]:
    txt = f.read_text(encoding="utf-8")
    l_m = re.search(r'linha:\s*"([^"]+)"', txt)
    p_m = re.search(r'produto:\s*"([^"]+)"', txt)
    linha = l_m.group(1).lower().strip() if l_m else ""
    produto = p_m.group(1).lower().strip() if p_m else f.name.lower()

    line_idx = 99
    for idx, lo in enumerate(LINE_ORDER):
        if lo in linha or lo in produto:
            line_idx = idx
            break

    return (line_idx, produto, f.name)


def get_placeholder_spec(prod_name: str) -> Tuple[str, str]:
    pn = norm(prod_name)
    if "malosso" in pn:
        return ("1600 x 500 px", "Absorção Otimizada de Cálcio com Alta Biodisponibilidade")
    if "calcio" in pn:
        return ("1600 x 500 px", "Saúde Óssea, Fortalecimento Dental & Absorção Mineral")
    if "feno" in pn:
        return ("1600 x 500 px", "Vigor Físico, Força & Metabolismo Ativo")
    if "dimalato" in pn:
        return ("1600 x 500 px", "Energia Muscular, Disposição & Redução do Cansaço")
    if ("pa" in pn or "p a" in pn) and "magnesio" in pn:
        return ("1600 x 500 px", "Equilíbrio Eletrolítico & Funcionamento Neuromuscular")
    if "treonato" in pn:
        return ("1600 x 480 px", "Foco Cognitivo, Memória & Desempenho Mental")
    if "nac" in pn or "n a c" in pn:
        return ("1600 x 500 px", "Ação Antioxidante, Defesa Celular & Saúde Respiratória")
    if "omega 3" in pn and "6" not in pn and "az" not in pn:
        return ("1600 x 450 px", "Saúde Cardiovascular, Vitalidade & Longevidade")
    if "3 6 9" in pn or "369" in pn:
        return ("1600 x 450 px", "Equilíbrio Lipídico, Ômegas Essenciais 3-6-9 & Vitalidade")
    if "hidrolisado" in pn or "limao" in pn:
        return ("1600 x 450 px", "Síntese de Colágeno, Vitalidade Articular & Pele Firme")
    if "hialuronico" in pn:
        return ("1600 x 480 px", "Mobilidade Articular, Firmeza & Hidratação Tecidual")
    if "condroitina" in pn or "msm" in pn:
        return ("1600 x 500 px", "Flexibilidade Articular, Conforto & Movimento Ativo")
    if "ultra" in pn:
        return ("1600 x 500 px", "Proteção Articular Avançada & Alívio do Desconforto")
    if "vitamina e" in pn:
        return ("1600 x 550 px", "Proteção Celular Contra Danos dos Radicais Livres")
    if "cabelo" in pn:
        return ("1600 x 500 px", "Nutrição Capilar, Unhas Fortes & Pele Radiante")
    if "verisol" in pn:
        return ("1600 x 480 px", "Elasticidade da Pele, Síntese de Colágeno & Firmeza")
    if "propolis" in pn:
        return ("1600 x 550 px", "Defesa Imunológica Natural & Proteção Diária")
    if "coenzima" in pn:
        return ("1600 x 450 px", "Antioxidante Celular, Vitalidade & Energia Mitocondrial")
    if "tempo" in pn:
        return ("1600 x 480 px", "Antienvelhecimento Celular & Renovação Vital")
    if "biomov" in pn:
        return ("1600 x 500 px", "Liberdade Articular & Manutenção da Função Motora")
    if "ceitil" in pn:
        return ("1600 x 500 px", "Defesa Respiratória, Fluidificação & Imunidade Fortalecida")
    if "prodiz" in pn or "melatonina" in pn:
        return ("1600 x 500 px", "Sono Reparador, Ciclo Circadiano & Relaxamento")
    if "epadose" in pn or "colina" in pn:
        return ("1600 x 500 px", "Metabolismo Lipídico, Saúde Hepática & Desintoxicação")
    if "laclaze" in pn or "lactase" in pn:
        return ("1600 x 550 px", "Digestão Completa da Lactose & Conforto Digestivo")
    if "naturedux" in pn or "cromo" in pn:
        return ("1600 x 480 px", "Controle Glicêmico & Metabolismo de Carboidratos e Gorduras")
    return ("1600 x 500 px", "Imagem Conceitual de Estilo de Vida & Bem-Estar")


def find_illustrative_banner(page_idx: int, prod_full: str) -> Any:
    """Retorna o caminho da imagem ilustrativa gerada caso exista na pasta do projeto."""
    img_dir = WORKSPACE_DIR / "imagens_ilustrativas"
    if not img_dir.exists():
        return None

    p_norm = norm(prod_full)

    # Mapeamento direto das imagens novas (Gemini_Generated_*) e padrão por produto
    direct_map = [
        ("borg", "calcio", "p06_borg_calcio_500mg.png"),
        ("borg", "feno", "Gemini_Generated_Image_it7ur2it7ur2it7u.jpeg"),
        ("borg", "dimalato", "Gemini_Generated_Image_nmlhrhnmlhrhnmlh.jpeg"),
        ("borg", "p a", "p09_borg_magnesio_p_a.png"),
        ("borg", "treonato", "Gemini_Generated_Image_f2d13sf2d13sf2d1.jpeg"),
        ("borg", "nac", "Gemini_Generated_Image_xcr4e1xcr4e1xcr4.jpeg"),
        ("carti", "hialuronico", "p15_carti_master_colageno_tipo_ii_acido_hialuronico.png"),
        ("carti", "condroitina", "p16_carti_master_condroitina_msm.png"),
        ("carti", "ultra", "p17_carti_master_ultra.png"),
        ("cronovit", "calcio", "p19_cronovit_calcio.png"),
        ("cronovit", "arginina", "Gemini_Generated_Image_wq23wtwq23wtwq23.jpeg"),
        ("cronovit", "bc kids", "cronovit_bc_kids_banner.jpeg"),
        ("cronovit", "imune", "cronovit_imune_banner.jpeg"),
        ("cronovit", "vitamina c", "cronovit_vitamina_c_banner.jpeg"),
        ("cronovit", "vitamina d", "cronovit_vitamina_d_banner.jpeg"),
        ("cronovit", "zinco", "cronovit_zinco_selenio_banner.jpeg"),
        ("cronovit", "vitamina e", "Gemini_Generated_Image2_k9mabgk9mabgk9ma_copiar.jpg"),
        ("cronoliv", "cabelo", "Gemini_Generated_Image_jyh6ejyh6ejyh6ej.jpeg"),
        ("cronoliv", "verisol", "p25_cronoliv_colageno_verisol.png"),
        ("cronoliv", "propolis", "Gemini_Generated_Image_v78pejv78pejv78p.jpeg"),
        ("nutrivix", "coenzima", "Gemini_Generated_Image.jpeg"),
        ("nutrivix", "dimalato", "Gemini_Generated_Image_508r3l508r3l508r.jpeg"),
        ("nutrivix", "treonato", "p29_nutrivix_magnesio_treonato.png"),
        ("biomov", "hialuronico", "Gemini_Generated_Image_xmxw6fxmxw6fxmxw__1_.jpeg"),
        ("ceitil", "acetil", "Gemini_Generated_Image_xcr4e1xcr4e1xcr4.jpeg"),
        ("prodiz", "melatonina", "Gemini_Generated_Image_gdcunbgdcunbgdcu.jpeg"),
        ("epadose", "colina", "Gemini_Generated_Image_jdgkgkjdgkgkjdgk.jpeg"),
        ("laclaze", "lactase", "Gemini_Generated_Image_uwpqi8uwpqi8uwpq.jpeg"),
        ("malosso", "calcio", "Gemini_Generated_Image_d8faxqd8faxqd8fa.jpeg"),
        ("naturedux", "cromo", "Gemini_Generated_Image_l6cr1ml6cr1ml6cr.jpeg"),
    ]

    for brand, kw, filename in direct_map:
        if brand in p_norm and kw in p_norm:
            candidate = img_dir / filename
            if candidate.exists():
                return str(candidate.resolve())

    prefix = f"p{page_idx:02d}_"
    for ext in ("*.png", "*.jpg", "*.jpeg"):
        for f in img_dir.glob(ext):
            if f.name.startswith(prefix):
                return str(f.resolve())
    return None


# ==============================================================================
# 8. GERADOR DO HTML DA PÁGINA
# ==============================================================================
def render_product_page(idx: int, pdata: Dict[str, Any], img_path: str) -> str:
    fm = pdata["fm"]
    prod_full = fm.get("produto", f"Produto {idx}").strip()
    linha = fm.get("linha", "Assifarma").strip()

    notif_title, notif_val = format_notification(prod_full, pdata)

    display_title = prod_full
    if not display_title.lower().startswith(linha.lower()) and linha.lower() not in [
        "especiais",
        "assifarma",
    ]:
        display_title = f"{linha} {display_title}"

    t_len = len(display_title)
    if t_len <= 18:
        title_font_size = "23pt"
    elif t_len <= 26:
        title_font_size = "20pt"
    elif t_len <= 36:
        title_font_size = "17.5pt"
    elif t_len <= 45:
        title_font_size = "15.2pt"
    else:
        title_font_size = "13.8pt"

    theme = extract_palette_from_image(img_path, linha)

    # Destaques Rápidos Padronizados
    b1 = "Zero Açúcar"
    b2 = "Não contém Glúten"
    b3 = "Não contém Sódio"

    apresentacao = fm.get("apresentacao", "Contém 60 unidades")
    recomendacao = pdata["recomendacao"]
    publico_alvo = pdata["via_uso"]

    denominacao = pdata["denominacao"]
    if not denominacao:
        denominacao = "SUPLEMENTO ALIMENTAR EM CÁPSULAS"

    # Conhecimento do Produto: Ativos Destacados e Alegações IN 28 Oficiais
    know = PRODUCT_KNOWLEDGE.get(prod_full)
    if not know:
        for k, v in PRODUCT_KNOWLEDGE.items():
            if k.lower() in prod_full.lower() or prod_full.lower() in k.lower():
                know = v
                break

    if know:
        key_actives = know["key_actives"]
        in28_claims = know["in28_claims"]
    else:
        key_actives = []
        in28_claims = pdata["alegacoes"] or [
            "Auxilia no funcionamento do sistema imune e metabolismo energético.",
            "Contribui para a manutenção da saúde e proteção contra danos dos radicais livres.",
        ]

    # Blocos preenchidos de ingredientes importantes (um por linha no topo do card)
    actives_html = ""
    if key_actives:
        actives_pills = "".join([f'<div class="active-badge-pill">{act}</div>' for act in key_actives])
        actives_html = f'<div class="key-actives-container">{actives_pills}</div>'

    # Lista de alegações IN 28 estritas
    alegacoes_html = "".join([f"<li>{al}</li>" for al in in28_claims])

    # Ingredientes e Alérgenos (alérgenos na cor padrão, sem vermelho)
    ingredientes = pdata["ingredientes"]
    alergicos = pdata["alergicos"]
    alergicos_html = f'<span class="allergens-inline">{alergicos}</span>' if alergicos else ""

    # Ajuste para Borg Ômega 3 e Cartimaster + Ácido Hialurônico
    p_norm = norm(prod_full)
    is_omega_3_trio = (
        "omega 3" in p_norm
        and "borg" in p_norm
        and "6" not in p_norm
        and "az" not in p_norm
    )
    is_cartimaster_hialuronico = (
        "carti" in p_norm
        and "hialuronico" in p_norm
    )
    is_panoramic_stage = is_omega_3_trio or is_cartimaster_hialuronico

    if is_omega_3_trio:
        porcoes_display = "20, 40, 80 porções"
    elif is_cartimaster_hialuronico:
        porcoes_display = "30 e 60 porções"
    else:
        porcoes_display = pdata["porcoes_emb"]

    # Tabela ANVISA — Densidade ajustada em 4 faixas precisas
    table_rows = pdata["table_rows"]
    row_count = len(table_rows)
    if row_count <= 6:
        table_density_class = "density-short"
    elif row_count <= 13:
        table_density_class = "density-medium"
    elif row_count <= 19:
        table_density_class = "density-semidense"
    else:
        table_density_class = "density-dense"

    rows_html = ""
    for r in table_rows:
        n = r[0]
        q = r[1] if len(r) > 1 else ""
        vd = r[2] if len(r) > 2 else "0"
        rows_html += f"<tr><td>{n}</td><td>{q}</td><td>{vd}</td></tr>\n"

    insignificant = pdata["insignificant"]
    advertencias = pdata["advertencias"]
    conservacao = pdata["conservacao"]

    # Card de Informações e Benefícios (coluna 1)
    card_beneficios_html = f"""
        <div class="glass-info-card">
          <h3 class="card-heading">Informações e benefícios</h3>
          <ul class="md-benefits-list">
            {alegacoes_html}
          </ul>
        </div>
    """

    # Card de Ingredientes
    card_ingredientes_html = f"""
        <div class="glass-info-card">
          <h3 class="card-heading">Ingredientes</h3>
          <p class="ingredients-copy">
            {ingredientes}
            {alergicos_html}
          </p>
        </div>
    """

    # Bloco dos 3 Destaques Rápidos
    highlights_row_html = f"""
        <div class="below-image-highlights">
          <div class="highlight-feature-box"><span class="hl-main">{b1}</span></div>
          <div class="highlight-feature-box"><span class="hl-main">{b2}</span></div>
          <div class="highlight-feature-box"><span class="hl-main">{b3}</span></div>
        </div>
    """

    # Tabela ANVISA
    anvisa_table_html = f"""
        <div class="anvisa-box {table_density_class}">
          <div class="anvisa-title">INFORMAÇÃO NUTRICIONAL</div>
          <div class="anvisa-serving-block">
            Porções por Embalagem: {porcoes_display}<br />
            Porção: {pdata['porcao']}
          </div>
          <table class="anvisa-table">
            <thead>
              <tr>
                <th></th>
                <th></th>
                <th>%VD*</th>
              </tr>
            </thead>
            <tbody>
              {rows_html}
            </tbody>
          </table>
          <div class="anvisa-insignificant">
            {insignificant}
          </div>
          <div class="anvisa-footnote">
            * Percentual de valores diários fornecidos pela porção.
          </div>
        </div>
    """

    # Classificação de Densidade da Página:
    # - is-omega-trio-page: Borg Ômega 3 com palco panorâmico ampliado (3 produtos grandes) e sem placeholder na base
    # - is-dense (row_count >= 20): tabelas longas (24-30 linhas), sem placeholder
    # - is-semidense (14 <= row_count <= 19): tabelas médias-longas (15-19 linhas), sem placeholder
    # - is-spacious (row_count <= 13): espaço livre nas 2 colunas -> placeholder panorâmico de 2 colunas na base
    if is_omega_3_trio:
        density_page_class = "is-omega-trio-page"
        has_bottom_banner = False
    elif row_count >= 20:
        density_page_class = "is-dense"
        has_bottom_banner = False
    elif row_count >= 14:
        density_page_class = "is-semidense"
        has_bottom_banner = False
    else:
        density_page_class = "is-spacious"
        has_bottom_banner = True

    # Com os boxes de ativos movidos para a Coluna 2 (abaixo da Tabela Nutricional):
    # - No layout panorâmico (Pág. 12 e Pág. 15), Cuidados de Conservação fica na Coluna 1 (Diff = 0.0mm)
    # - Nas demais páginas com até 19 linhas, Cuidados de Conservação fica em card próprio na Coluna 2
    # - Nas páginas densas (>= 20 linhas), Cuidados de Conservação fica integrado ao card de Advertências na Coluna 2
    split_conservation_left_panoramic = is_panoramic_stage
    split_conservation_right = (not is_panoramic_stage) and (row_count <= 19)

    if split_conservation_left_panoramic:
        warnings_card_html = f"""
        <div class="warnings-precautions-card">
          <h3 class="card-heading">Advertências e precauções</h3>
          <p class="warnings-caps">{advertencias}</p>
        </div>
        """
        extra_left_card_html = f"""
        <div class="glass-info-card conservation-card">
          <h3 class="card-heading">Cuidados de conservação</h3>
          <p class="ingredients-copy">{conservacao}</p>
        </div>
        """
    elif split_conservation_right:
        warnings_card_html = f"""
        <div class="warnings-precautions-card">
          <h3 class="card-heading">Advertências e precauções</h3>
          <p class="warnings-caps">{advertencias}</p>
        </div>
        <div class="glass-info-card conservation-card">
          <h3 class="card-heading">Cuidados de conservação</h3>
          <p class="ingredients-copy">{conservacao}</p>
        </div>
        """
        extra_left_card_html = ""
    else:
        warnings_card_html = f"""
        <div class="warnings-precautions-card">
          <h3 class="card-heading">Advertências e precauções</h3>
          <p class="warnings-caps">{advertencias}</p>
          <p class="conservation-text"><strong>Cuidados de Conservação:</strong> {conservacao}</p>
        </div>
        """
        extra_left_card_html = ""

    # Imagem Ilustrativa (Foto real gerada ou placeholder cinza ocupando as DUAS COLUNAS)
    placeholder_banner_html = ""
    if has_bottom_banner:
        px_size, short_desc = get_placeholder_spec(prod_full)
        banner_img = find_illustrative_banner(idx, display_title)
        if banner_img:
            placeholder_banner_html = f"""
            <section class="placeholder-banner-section">
              <div class="image-illustrative-card">
                <img class="banner-photo" src="{banner_img}" alt="{short_desc}" />
              </div>
            </section>
            """
        else:
            placeholder_banner_html = f"""
            <section class="placeholder-banner-section">
              <div class="image-placeholder-card placeholder-full-width">
                <div class="placeholder-icon">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="3" width="18" height="18" rx="3" ry="3"/>
                    <circle cx="8.5" cy="8.5" r="1.5"/>
                    <polyline points="21 15 16 10 5 21"/>
                  </svg>
                </div>
                <div class="placeholder-badge">IMAGEM ILUSTRATIVA ({px_size})</div>
                <div class="placeholder-desc">{short_desc}</div>
                <div class="placeholder-sub">Área reservada em 2 colunas para imagem conceitual ou fotografia de estilo de vida</div>
              </div>
            </section>
            """

    # LAYOUT PANORÂMICO DE 2 COLUNAS NO TOPO (Borg Ômega 3 e Cartimaster + Ácido Hialurônico)
    if is_panoramic_stage:
        main_content_html = f"""
        <section class="panoramic-stage-container">
          <div class="glass-product-stage glass-stage-panoramic">
            <img class="packshot packshot-panoramic" src="{img_path}" alt="{prod_full}" />
          </div>
        </section>

        <section class="equal-columns-grid omega-trio-grid">
          <div class="col-left">
            {highlights_row_html}
            {card_beneficios_html}
            {card_ingredientes_html}
            {extra_left_card_html}
          </div>
          <div class="col-right">
            {anvisa_table_html}
            {actives_html}
            {warnings_card_html}
          </div>
        </section>
        {placeholder_banner_html}
        """
    else:
        main_content_html = f"""
        <section class="equal-columns-grid">
          <div class="col-left">
            <div class="glass-product-stage">
              <img class="packshot" src="{img_path}" alt="{prod_full}" />
            </div>
            {highlights_row_html}
            {card_beneficios_html}
            {card_ingredientes_html}
            {extra_left_card_html}
          </div>
          <div class="col-right">
            {anvisa_table_html}
            {actives_html}
            {warnings_card_html}
          </div>
        </section>
        {placeholder_banner_html}
        """

    page_html = f"""
    <!-- PÁGINA {idx:02d}: {display_title} -->
    <article class="catalog-page {density_page_class}" id="pagina-{idx}" style="
      --theme-color: {theme['theme_color']};
      --theme-dark: {theme['theme_dark']};
      --theme-light: {theme['theme_light']};
      --page-bg: {theme['page_bg']};
      --header-grad: {theme['header_grad']};
      --stage-grad: {theme['stage_grad']};
      --glass-border: {theme['glass_border']};
      --box-grad: {theme['box_grad']};
    ">
      <div class="product-page-flow">
        
        <header class="hero-color-header">
          <div class="hero-top-row">
            <h1 class="title-product-unified" style="font-size: {title_font_size};">{display_title}</h1>
            <span class="hero-category-glass">{linha.upper()}</span>
          </div>
          <p class="md-denominacao-venda">{denominacao}</p>
        </header>

        <div class="brand-spectrum-bar"></div>

        <section class="key-specs-highlight-grid">
          <div class="key-spec-box">
            <span class="key-spec-label">Apresentação:</span>
            <span class="key-spec-value">{apresentacao}</span>
          </div>
          <div class="key-spec-box">
            <span class="key-spec-label">Recomendação:</span>
            <span class="key-spec-value">{recomendacao}</span>
          </div>
          <div class="key-spec-box">
            <span class="key-spec-label">Público-Alvo:</span>
            <span class="key-spec-value">{publico_alvo.split('•')[0].strip()}</span>
          </div>
        </section>

        {main_content_html}

      </div>

      <footer class="bottom-brand-footer">
        <div class="footer-col-1">
          <div>
            <span class="footer-brand-title">{linha}</span>
            <span class="footer-brand-sub">INTERCRON / FORHEALTH</span>
          </div>
        </div>
        <div class="footer-right-group">
          <div class="footer-col-2">
            <strong>{notif_title}</strong>
            {notif_val}
          </div>
          <div class="footer-col-3">
            Pág. <strong>{idx:02d}</strong>
          </div>
        </div>
      </footer>
    </article>
    """
    return page_html


def render_cover_page() -> str:
    """Renderiza a Página 01 (Capa Oficial) no modelo Retrato A4 igual ao padrão VitaMaiz."""
    capa_bg_path = str((WORKSPACE_DIR / "Design padrão" / "extracted_assets" / "capa_azul.png").resolve())
    logo_white_path = str((WORKSPACE_DIR / "Design padrão" / "extracted_assets" / "logo_forhealth_white.svg").resolve())

    return f"""
    <!-- ========================================================================
         PÁGINA 01: CAPA OFICIAL
         ======================================================================== -->
    <section class="catalog-page cover-clean-page" id="pagina-1">
      <div class="cover-image-layer" style="background-image: url('{capa_bg_path}');"></div>
      <div class="cover-content-layer">
        <div class="cover-brand-top">
          <span class="cover-intercron-pill">INTERCRON • FORHEALTH</span>
          <img
            class="cover-main-logo"
            src="{logo_white_path}"
            alt="Forhealth Advanced Nutrition"
          />
          <div class="cover-brand-divider"></div>
          <p class="cover-brand-tagline">Linhas Exclusivas de Suplementos Alimentares</p>
        </div>

        <div class="cover-titles-block">
          <p class="cover-edition-label">Catálogo de Produtos 2026</p>
          <p class="cover-edition-sub">BORG • CARTI MASTER • CRONOVIT • CRONOLIV • NUTRIVIX</p>
        </div>
      </div>
    </section>
    """


def render_toc_page(toc_entries: List[Dict[str, Any]]) -> str:
    """Renderiza a Página 02 (Índice Geral por Linha de Produto) no modelo Retrato A4."""
    logo_dark_path = str((WORKSPACE_DIR / "Design padrão" / "extracted_assets" / "logo_forhealth_dark.svg").resolve())

    # Agrupar itens por grupo de linha mantendo ordem sequencial
    groups_order = [
        ("Linha Borg", "badge-borg", ["borg"]),
        ("Linha Carti Master", "badge-cartimaster", ["carti master"]),
        ("Linha Cronovit", "badge-cronovit", ["cronovit"]),
        ("Linha Cronoliv", "badge-cronoliv", ["cronoliv"]),
        ("Linha Nutrivix", "badge-nutrivix", ["nutrivix"]),
        ("Marcas Especiais", "badge-especiais", []),
    ]

    grouped: Dict[str, List[Dict[str, Any]]] = {g[0]: [] for g in groups_order}
    for entry in toc_entries:
        ln = entry["linha"].lower().strip()
        placed = False
        for g_title, _, match_keys in groups_order[:-1]:
            if any(k in ln for k in match_keys):
                grouped[g_title].append(entry)
                placed = True
                break
        if not placed:
            grouped["Marcas Especiais"].append(entry)

    def render_cat_block(cat_title: str, badge_cls: str, items: List[Dict[str, Any]]) -> str:
        lis = []
        for it in items:
            pg_str = f"{it['page']:02d}"
            lis.append(f"""
              <li class="toc-clean-item">
                <a href="#pagina-{it['page']}" class="toc-item-link">
                  <span class="toc-clean-name">{it['title']}</span>
                  <span class="toc-clean-leader"></span>
                  <span class="toc-clean-page">Pág. {pg_str}</span>
                </a>
              </li>""")
        count_label = f"{len(items)} produto" if len(items) == 1 else f"{len(items)} produtos"
        flex_weight = len(items) + 1.8
        return f"""
            <div class="toc-category-card" style="flex: {flex_weight:.1f};">
              <div class="toc-category-head">
                <span class="toc-cat-pill {badge_cls}">{cat_title}</span>
                <span class="toc-cat-count">{count_label}</span>
              </div>
              <ul class="toc-clean-list">
                {"".join(lis)}
              </ul>
            </div>"""

    # Coluna esquerda: Págs. 03 a 23 (Borg, Carti Master, Cronovit = 21 produtos)
    col_left_html = (
        render_cat_block("Linha Borg", "badge-borg", grouped["Linha Borg"])
        + render_cat_block("Linha Carti Master", "badge-cartimaster", grouped["Linha Carti Master"])
        + render_cat_block("Linha Cronovit", "badge-cronovit", grouped["Linha Cronovit"])
    )

    # Coluna direita: Cronoliv, Nutrivix, Marcas Especiais
    col_right_html = (
        render_cat_block("Linha Cronoliv", "badge-cronoliv", grouped["Linha Cronoliv"])
        + render_cat_block("Linha Nutrivix", "badge-nutrivix", grouped["Linha Nutrivix"])
        + render_cat_block("Marcas Especiais", "badge-especiais", grouped["Marcas Especiais"])
    )

    return f"""
    <!-- ========================================================================
         PÁGINA 02: ÍNDICE DE PRODUTOS
         ======================================================================== -->
    <section class="catalog-page toc-page" id="pagina-2">
      <div class="product-page-flow">

        <header class="toc-simple-header">
          <div>
            <h1 class="toc-giant-heading">Índice</h1>
            <p class="toc-sub-heading">Portfólio Organizado por Linha de Produto</p>
          </div>
          <div class="toc-header-brand">
            <img
              class="toc-simple-logo"
              src="{logo_dark_path}"
              alt="Forhealth Advanced Nutrition"
            />
            <span class="toc-brand-caption">INTERCRON / FORHEALTH</span>
          </div>
        </header>

        <div class="brand-spectrum-bar"></div>

        <div class="toc-columns-wrapper">
          <div class="toc-col">
            {col_left_html}
          </div>
          <div class="toc-col">
            {col_right_html}
          </div>
        </div>

      </div>

      <footer class="bottom-brand-footer">
        <div class="footer-col-1">
          <div>
            <span class="footer-brand-title" style="color: #0B132B;">Catálogo Oficial 2026</span>
            <span class="footer-brand-sub">INTERCRON / FORHEALTH</span>
          </div>
        </div>
        <div class="footer-right-group">
          <div class="footer-col-2">
            <strong>SUMÁRIO GERAL</strong>
            {len(toc_entries)} Produtos • 6 Linhas
          </div>
          <div class="footer-col-3" style="color: #0B132B; border-color: #cbd5e1;">
            Pág. <strong>02</strong>
          </div>
        </div>
      </footer>
    </section>
    """


def render_back_cover_page(page_num: int = 40) -> str:
    """Renderiza a Página 40 (Contracapa Institucional) no modelo Retrato A4."""
    logo_dark_path = str((WORKSPACE_DIR / "Design padrão" / "extracted_assets" / "logo_forhealth_dark.svg").resolve())

    return f"""
    <!-- ========================================================================
         PÁGINA {page_num:02d}: CONTRACAPA INSTITUCIONAL
         ======================================================================== -->
    <section class="catalog-page back-cover-clean-page" id="pagina-{page_num}">
      <div class="back-cover-top-bar"></div>
      <div class="back-cover-content">
        <span class="back-cover-pill">INTERCRON • FORHEALTH</span>
        <img
          class="back-cover-logo"
          src="{logo_dark_path}"
          alt="Forhealth Advanced Nutrition"
        />
        <div class="back-cover-spectrum"></div>
        <p class="back-cover-lines">BORG • CARTI MASTER • CRONOVIT • CRONOLIV • NUTRIVIX</p>
      </div>
      <div class="back-cover-footer">
        <span>CATÁLOGO OFICIAL DE PRODUTOS 2026 • INTERCRON / FORHEALTH</span>
      </div>
    </section>
    """


# ==============================================================================
# 9. COMPILAÇÃO DO HTML COMPLETO
# ==============================================================================
def build_catalog():
    print("=" * 64)
    print("🚀 COMPILANDO CATÁLOGO OFICIAL ASSIFARMA 2026 (RETRATO A4)")
    print("=" * 64)

    raw_files = [f for f in MD_DIR.glob("*.md") if "odessy" not in f.name.lower() and "condroitina" not in f.name.lower()]
    md_files = sorted(raw_files, key=get_product_sort_key)
    print(f"Total de produtos agrupados por linha: {len(md_files)}")

    product_pages_html: List[str] = []
    toc_entries: List[Dict[str, Any]] = []

    for idx, f in enumerate(md_files, 1):
        page_num = idx + 2  # Pág. 01 = Capa, Pág. 02 = Índice, Pág. 03..39 = Produtos
        prefix = f.name[:9]
        pdata = parse_md(f)
        prod_name = pdata["fm"].get("produto", f.name).strip()
        linha_clean = pdata["fm"].get("linha", "Assifarma").strip()
        img_path = find_best_image(prefix, prod_name)

        display_title = prod_name
        if not display_title.lower().startswith(linha_clean.lower()) and linha_clean.lower() not in [
            "especiais",
            "assifarma",
        ]:
            display_title = f"{linha_clean} {display_title}"

        toc_entries.append({
            "page": page_num,
            "title": display_title,
            "linha": linha_clean,
        })

        print(f"Processando [Pág. {page_num:02d}] {display_title[:32]:32s} -> {Path(img_path).name}")
        page_html = render_product_page(page_num, pdata, img_path)
        product_pages_html.append(page_html)

    cover_html = render_cover_page()
    toc_html = render_toc_page(toc_entries)
    back_cover_html = render_back_cover_page(len(md_files) + 3)
    all_pages_combined = "\n".join([cover_html, toc_html] + product_pages_html + [back_cover_html])

    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Assifarma — Catálogo Oficial 2026 (Completo)</title>

  <!-- Google Fonts: Bricolage Grotesque, Plus Jakarta Sans e Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet" />

  <style>
    :root {{
      --ink-900: #0B132B;
      --ink-700: #1E293B;
      --ink-500: #475569;
      --ink-300: #94A3B8;

      --font-title: 'Bricolage Grotesque', sans-serif;
      --font-ui: 'Plus Jakarta Sans', sans-serif;
      --font-body: 'Inter', sans-serif;
      --font-anvisa: Arial, Helvetica, sans-serif;

      --brand-spectrum: linear-gradient(
        90deg,
        #175da9 0%,
        #0284c7 20%,
        #059669 40%,
        #eab308 60%,
        #ea580c 80%,
        #dc2626 100%
      );

      --page-width: 210mm;
      --page-height: 297mm;
      --page-margin: 10mm;
      --col-gap: 6.5mm;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }}

    html, body {{
      margin: 0;
      padding: 0;
      background: #e2e8f0;
      font-family: var(--font-body);
      color: var(--ink-900);
      font-size: 8pt;
      line-height: 1.35;
      -webkit-font-smoothing: antialiased;
    }}

    .catalog-page {{
      width: var(--page-width);
      height: var(--page-height);
      min-width: var(--page-width);
      min-height: var(--page-height);
      max-width: var(--page-width);
      max-height: var(--page-height);
      margin: 12px auto;
      padding: var(--page-margin);
      background: var(--page-bg);
      position: relative;
      box-sizing: border-box;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
      page-break-after: always;
      break-after: page;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    @media print {{
      @page {{
        size: A4 portrait;
        margin: 0;
      }}
      body {{
        background: none;
      }}
      .editor-top-bar,
      #editor-toast,
      .image-edit-toolbar,
      .mask-resize-handle,
      .drop-zone-overlay,
      .hidden-editor-file-input {{
        display: none !important;
      }}
      .catalog-page {{
        margin: 0;
        box-shadow: none;
        page-break-after: always;
        break-after: page;
      }}
    }}

    .product-page-flow {{
      display: flex;
      flex-direction: column;
      gap: 2.8mm;
      padding-bottom: 4.5mm;
      flex: 1;
      min-height: 0;
    }}

    /* HEADER COM PADDING AMPLIADO */
    .hero-color-header {{
      flex-shrink: 0;
      background: var(--header-grad);
      color: #ffffff;
      padding: 4.8mm 5.8mm;
      border-radius: 13px;
      box-shadow: 0 6px 18px -4px rgba(9, 20, 38, 0.22);
      position: relative;
      overflow: hidden;
    }}

    .hero-color-header::after {{
      content: "";
      position: absolute;
      top: -25mm;
      right: -15mm;
      width: 75mm;
      height: 75mm;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(255, 255, 255, 0.22) 0%, rgba(255, 255, 255, 0) 70%);
      pointer-events: none;
    }}

    .hero-top-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: relative;
      z-index: 2;
      gap: 3.5mm;
      margin-bottom: 1.2mm;
    }}

    .title-product-unified {{
      font-family: var(--font-title);
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.05;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      flex: 1;
      min-width: 0;
    }}

    .hero-category-glass {{
      background: rgba(255, 255, 255, 0.20);
      border: 1px solid rgba(255, 255, 255, 0.45);
      backdrop-filter: blur(12px);
      color: #ffffff;
      font-family: var(--font-ui);
      font-size: 7.4pt;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.10em;
      padding: 4px 12px;
      border-radius: 999px;
      white-space: nowrap;
      flex-shrink: 0;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.12);
    }}

    .md-denominacao-venda {{
      position: relative;
      z-index: 2;
      font-family: var(--font-ui);
      font-size: 7.4pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: rgba(255, 255, 255, 0.95);
      padding-top: 1.4mm;
      border-top: 1px solid rgba(255, 255, 255, 0.25);
    }}

    .brand-spectrum-bar {{
      width: 100%;
      height: 3px;
      background: var(--brand-spectrum);
      border-radius: 2px;
      margin: 0.4mm 0;
    }}

    /* KEY SPECS GRID */
    .key-specs-highlight-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 3.2mm;
    }}

    .key-spec-box {{
      background: var(--box-grad);
      border: 1.5px solid var(--glass-border);
      backdrop-filter: blur(12px);
      border-radius: 12px;
      padding: 2.2mm 3.4mm;
      display: flex;
      flex-direction: column;
      justify-content: center;
      box-shadow: 0 4px 14px -4px rgba(9, 20, 38, 0.08);
    }}

    .key-spec-label {{
      font-family: var(--font-ui);
      font-size: 7.3pt;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--theme-color);
      margin-bottom: 0.4mm;
    }}

    .key-spec-value {{
      font-family: var(--font-title);
      font-size: 9.8pt;
      font-weight: 800;
      color: var(--ink-900);
      line-height: 1.15;
    }}

    /* EQUAL COLUMNS GRID (PADRÃO 100%: ESQUERDA IMAGEM / DIREITA TABELA) */
    .equal-columns-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--col-gap);
      flex: 1;
      align-items: stretch;
      min-height: 0;
    }}

    .col-left, .col-right {{
      display: flex;
      flex-direction: column;
      gap: 2.8mm;
      min-width: 0;
      height: 100%;
      justify-content: flex-start;
    }}

    /* Cards flexíveis absorvem diferenças finas de altura entre colunas mantendo gaps 100% uniformes */
    .col-left > .glass-info-card,
    .col-right > .warnings-precautions-card,
    .col-right > .glass-info-card {{
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}

    /* COMPORTAMENTO PÁGINAS DENSAS (row_count >= 20, ex: Borg AZ Ômega - Página 1) */
    .catalog-page.is-dense .equal-columns-grid {{
      flex: 1;
    }}

    .catalog-page.is-dense .col-left,
    .catalog-page.is-dense .col-right {{
      gap: 2.4mm;
    }}

    .catalog-page.is-dense .glass-product-stage {{
      height: 68mm;
      padding: 2.6mm;
    }}

    .catalog-page.is-dense .glass-product-stage img.packshot {{
      max-height: 61mm;
    }}

    .catalog-page.is-dense .glass-info-card {{
      padding: 2.6mm 3.4mm;
    }}

    .catalog-page.is-dense .ingredients-copy {{
      line-height: 1.34;
    }}

    .catalog-page.is-dense .warnings-precautions-card {{
      padding: 2.6mm 3.4mm;
      line-height: 1.32;
    }}

    /* COMPORTAMENTO PÁGINAS SEMIDENSAS (14 <= row_count <= 19) */
    .catalog-page.is-semidense .equal-columns-grid {{
      flex: 1;
    }}

    .catalog-page.is-semidense .col-left,
    .catalog-page.is-semidense .col-right {{
      gap: 2.8mm;
    }}

    .catalog-page.is-semidense .glass-product-stage {{
      height: 70mm;
      padding: 2.8mm;
    }}

    .catalog-page.is-semidense .glass-product-stage img.packshot {{
      max-height: 63mm;
    }}

    .catalog-page.is-semidense .glass-info-card {{
      padding: 3.0mm 3.8mm;
    }}

    .catalog-page.is-semidense .warnings-precautions-card {{
      padding: 3.0mm 3.8mm;
    }}

    /* COMPORTAMENTO ESPECIAL BORG ÔMEGA 3 (3 PRODUTOS AMPLIADOS PREENCHENDO O ESPAÇO VAGO, SEM PLACEHOLDER) */
    .catalog-page.is-omega-trio-page .equal-columns-grid {{
      flex: 1;
    }}

    .catalog-page.is-omega-trio-page .col-left,
    .catalog-page.is-omega-trio-page .col-right {{
      gap: 2.8mm;
    }}

    .catalog-page.is-omega-trio-page .glass-stage-panoramic {{
      height: 86mm !important;
      padding: 2.2mm 2.8mm !important;
    }}

    .catalog-page.is-omega-trio-page .packshot-panoramic {{
      max-height: 81mm !important;
      max-width: 98.5% !important;
    }}

    .catalog-page.is-omega-trio-page .glass-info-card {{
      padding: 3.0mm 3.8mm;
    }}

    .catalog-page.is-omega-trio-page .warnings-precautions-card {{
      padding: 3.2mm 3.8mm;
      line-height: 1.38;
    }}

    /* COMPORTAMENTO PÁGINAS ESPAÇOSAS (row_count <= 13 -> Banner Ilustrativo em 2 Colunas na Base) */
    .catalog-page.is-spacious .equal-columns-grid {{
      flex: 0 0 auto;
    }}

    .catalog-page.is-spacious .col-left,
    .catalog-page.is-spacious .col-right {{
      gap: 2.8mm;
    }}

    .catalog-page.is-spacious .glass-product-stage {{
      height: 60mm;
      padding: 2.8mm;
    }}

    .catalog-page.is-spacious .glass-product-stage img.packshot {{
      max-height: 53mm;
    }}

    .catalog-page.is-spacious .glass-stage-panoramic {{
      height: 50mm !important;
      padding: 2.5mm 5mm !important;
    }}

    .catalog-page.is-spacious .packshot-panoramic {{
      max-height: 44mm !important;
    }}

    .catalog-page.is-spacious .glass-info-card {{
      padding: 2.8mm 3.6mm;
    }}

    .catalog-page.is-spacious .card-heading {{
      margin-bottom: 1.3mm;
    }}

    .catalog-page.is-spacious .md-benefits-list {{
      gap: 1.3mm;
      line-height: 1.38;
    }}

    .catalog-page.is-spacious .ingredients-copy {{
      line-height: 1.38;
    }}

    .catalog-page.is-spacious .anvisa-box.density-short {{
      padding: 2.8mm 3.4mm;
    }}

    .catalog-page.is-spacious .anvisa-serving-block {{
      line-height: 1.32;
      padding: 1.2mm 0;
    }}

    .catalog-page.is-spacious .anvisa-table.density-short td,
    .catalog-page.is-spacious .anvisa-table.density-short th {{
      padding: 1.2mm 1.5mm;
      line-height: 1.28;
    }}

    .catalog-page.is-spacious .warnings-precautions-card {{
      padding: 2.8mm 3.6mm;
      line-height: 1.35;
    }}

    /* SEÇÃO PANORÂMICA DE 2 COLUNAS PARA PLACEHOLDER / IMAGEM ILUSTRATIVA */
    .placeholder-banner-section {{
      flex: 1;
      display: flex;
      flex-direction: column;
      width: 100%;
      min-height: 32mm;
      max-height: 42mm;
    }}

    .image-illustrative-card {{
      width: 100%;
      height: 100%;
      min-height: 32mm;
      max-height: 42mm;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 4px 14px rgba(9, 20, 38, 0.08);
      border: 1px solid var(--glass-border);
      display: flex;
      background: #000000;
    }}

    .banner-photo {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}

    .image-placeholder-card {{
      background: #f8fafc;
      border: 1.5px dashed #cbd5e1;
      border-radius: 12px;
      padding: 3.0mm 4.5mm;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      gap: 1.2mm;
      box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.03);
      flex: 1;
      width: 100%;
      min-height: 30mm;
      box-sizing: border-box;
    }}

    .placeholder-icon {{
      color: #94a3b8;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .placeholder-badge {{
      font-family: var(--font-title);
      font-size: 6.8pt;
      font-weight: 800;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: #475569;
      background: #e2e8f0;
      padding: 1.5px 10px;
      border-radius: 999px;
    }}

    .placeholder-desc {{
      font-family: var(--font-title);
      font-size: 8.2pt;
      font-weight: 700;
      color: #334155;
      line-height: 1.25;
      max-width: 90%;
    }}

    .placeholder-sub {{
      font-family: var(--font-body);
      font-size: 6.4pt;
      font-style: italic;
      color: #64748b;
      line-height: 1.2;
    }}

    /* PALCO PADRÃO DO PRODUTO */
    .glass-product-stage {{
      background: var(--stage-grad);
      border: 1.5px solid rgba(255, 255, 255, 0.85);
      box-shadow:
        0 12px 28px -8px rgba(9, 20, 38, 0.12),
        inset 0 1px 0 rgba(255, 255, 255, 0.9);
      backdrop-filter: blur(16px);
      border-radius: 16px;
      padding: 2.8mm;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      height: 68mm;
    }}

    .glass-product-stage img.packshot {{
      max-height: 60mm;
      max-width: 100%;
      width: auto;
      object-fit: contain;
      filter: drop-shadow(0 14px 22px rgba(9, 20, 38, 0.25));
    }}

    /* PALCO PANORÂMICO (BORG ÔMEGA 3 E CARTIMASTER HIALURÔNICO) */
    .panoramic-stage-container {{
      width: 100%;
    }}

    .glass-stage-panoramic {{
      height: 54mm !important;
      padding: 2.8mm 5.5mm !important;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .packshot-panoramic {{
      max-height: 48mm !important;
      max-width: 94% !important;
      width: auto;
      object-fit: contain;
      filter: drop-shadow(0 12px 22px rgba(9, 20, 38, 0.22));
    }}

    .trio-badges-row {{
      display: flex;
      justify-content: center;
      gap: 10mm;
      width: 100%;
      margin-top: 1.5mm;
    }}

    .trio-badge {{
      font-family: var(--font-title);
      font-size: 7.2pt;
      font-weight: 800;
      color: var(--ink-700);
      background: rgba(255, 255, 255, 0.90);
      border: 1px solid var(--glass-border);
      padding: 1.5px 12px;
      border-radius: 999px;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
    }}

    .trio-badge.featured {{
      color: #ffffff;
      background: var(--header-grad);
      border: 1px solid rgba(255, 255, 255, 0.4);
    }}

    /* DESTAQUES RÁPIDOS PADRONIZADOS (Zero Açúcar / Não contém Glúten / Não contém Sódio) */
    .below-image-highlights {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.8mm;
    }}

    .highlight-feature-box {{
      background: var(--header-grad);
      color: #ffffff;
      border-radius: 8px;
      padding: 2.2mm 1.8mm;
      text-align: center;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 12px -3px rgba(0, 0, 0, 0.16);
    }}

    .highlight-feature-box .hl-main {{
      font-family: var(--font-title);
      font-size: 8.4pt;
      font-weight: 800;
      line-height: 1.15;
      color: #ffffff;
      white-space: nowrap;
    }}

    /* CARDS DE INFORMAÇÕES E INGREDIENTES */
    .glass-info-card {{
      background: rgba(255, 255, 255, 0.90);
      border: 1px solid var(--glass-border);
      backdrop-filter: blur(12px);
      border-radius: 12px;
      padding: 2.6mm 3.4mm;
      box-shadow: 0 4px 14px rgba(9, 20, 38, 0.04);
    }}

    .card-heading {{
      font-family: var(--font-ui);
      font-size: 8.6pt;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--theme-dark);
      margin-bottom: 1.4mm;
    }}

    /* BLOCOS PREENCHIDOS DE ATIVOS / INGREDIENTES IMPORTANTES (1 POR LINHA ABAIXO DA TABELA NUTRICIONAL) */
    .key-actives-container {{
      display: flex;
      flex-direction: column;
      gap: 1.5mm;
      margin: 0;
    }}

    .active-badge-pill {{
      background: var(--header-grad);
      color: #ffffff;
      font-family: var(--font-title);
      font-size: 8.8pt;
      font-weight: 800;
      padding: 2.0mm 3.4mm;
      border-radius: 8px;
      letter-spacing: 0.02em;
      line-height: 1.2;
      box-shadow: 0 3px 10px -2px rgba(0, 0, 0, 0.14);
    }}

    .catalog-page.is-dense .key-actives-container {{
      gap: 1.1mm;
    }}

    .catalog-page.is-dense .active-badge-pill {{
      font-size: 7.7pt;
      padding: 1.3mm 2.8mm;
    }}

    /* ALEGAÇÕES IN 28 */
    .md-benefits-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 1.5mm;
    }}

    .md-benefits-list li {{
      font-size: 8.6pt;
      color: var(--ink-700);
      line-height: 1.35;
      padding-left: 12px;
      position: relative;
    }}

    .catalog-page.is-spacious .md-benefits-list li {{
      font-size: 9.0pt;
      line-height: 1.36;
    }}

    .catalog-page.is-dense .md-benefits-list li {{
      font-size: 8.0pt;
      line-height: 1.30;
    }}

    .md-benefits-list li::before {{
      content: "";
      position: absolute;
      left: 0;
      top: 5.5px;
      width: 5.5px;
      height: 5.5px;
      border-radius: 50%;
      background: var(--theme-color);
    }}

    .ingredients-copy {{
      font-size: 7.7pt;
      color: var(--ink-700);
      line-height: 1.34;
    }}

    .catalog-page.is-dense .ingredients-copy {{
      font-size: 7.3pt;
      line-height: 1.30;
    }}

    /* ALÉRGENOS NA COR PADRÃO (SEM VERMELHO) */
    .ingredients-copy .allergens-inline {{
      display: block;
      margin-top: 1.2mm;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--ink-900);
      font-size: 7.7pt;
      letter-spacing: 0.02em;
    }}

    .catalog-page.is-dense .ingredients-copy .allergens-inline {{
      font-size: 7.3pt;
    }}

    /* ADVERTÊNCIAS E CONSERVAÇÃO */
    .warnings-precautions-card {{
      background: rgba(255, 255, 255, 0.90);
      border: 1.2px solid var(--glass-border);
      border-left: 4px solid var(--theme-color);
      border-radius: 12px;
      padding: 2.8mm 3.6mm;
      box-shadow: 0 4px 14px rgba(9, 20, 38, 0.04);
    }}

    .warnings-precautions-card .target-audience-line {{
      font-family: var(--font-ui);
      font-size: 7.8pt;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--theme-dark);
      margin-bottom: 0.8mm;
      display: block;
    }}

    .warnings-precautions-card .warnings-caps {{
      font-size: 7.4pt;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--ink-900);
      line-height: 1.32;
      margin-bottom: 0.8mm;
    }}

    .catalog-page.is-dense .warnings-precautions-card .warnings-caps {{
      font-size: 7.0pt;
      line-height: 1.26;
    }}

    .warnings-precautions-card .conservation-text {{
      font-size: 7.4pt;
      color: var(--ink-700);
      line-height: 1.30;
    }}

    .catalog-page.is-dense .warnings-precautions-card .conservation-text {{
      font-size: 7.0pt;
      line-height: 1.25;
    }}

    .warnings-precautions-card .conservation-text strong {{
      color: var(--ink-900);
      font-weight: 700;
    }}

    /* TABELA NUTRICIONAL ANVISA */
    .anvisa-box {{
      background: #ffffff;
      border: 1pt solid #000000;
      font-family: var(--font-anvisa);
      color: #000000;
      box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
    }}

    .anvisa-box.density-short {{
      padding: 2.6mm 3.0mm;
    }}
    .anvisa-box.density-short .anvisa-title {{
      font-size: 10.2pt;
      padding-bottom: 1.1mm;
    }}
    .anvisa-box.density-short .anvisa-serving-block {{
      font-size: 8.8pt;
      padding: 1.1mm 0.5mm;
      line-height: 1.24;
    }}
    .anvisa-box.density-short table.anvisa-table th {{
      font-size: 9.0pt;
      padding: 1.05mm 0.9mm;
    }}
    .anvisa-box.density-short table.anvisa-table td {{
      font-size: 8.8pt;
      padding: 1.05mm 0.9mm;
    }}
    .anvisa-box.density-short .anvisa-insignificant {{
      font-size: 7.4pt;
      padding: 1.1mm 0.7mm;
    }}
    .anvisa-box.density-short .anvisa-footnote {{
      font-size: 7.4pt;
      padding: 0.9mm 0.7mm 0.4mm;
    }}

    .anvisa-box.density-medium {{
      padding: 2.1mm 2.6mm;
    }}
    .anvisa-box.density-medium .anvisa-title {{
      font-size: 9.6pt;
      padding-bottom: 0.9mm;
    }}
    .anvisa-box.density-medium .anvisa-serving-block {{
      font-size: 8.3pt;
      padding: 0.9mm 0.5mm;
      line-height: 1.20;
    }}
    .anvisa-box.density-medium table.anvisa-table th {{
      font-size: 8.5pt;
      padding: 0.85mm 0.8mm;
    }}
    .anvisa-box.density-medium table.anvisa-table td {{
      font-size: 8.3pt;
      padding: 0.80mm 0.8mm;
    }}
    .anvisa-box.density-medium .anvisa-insignificant {{
      font-size: 7.0pt;
      padding: 0.85mm 0.55mm;
    }}
    .anvisa-box.density-medium .anvisa-footnote {{
      font-size: 7.0pt;
      padding: 0.75mm 0.55mm 0.35mm;
    }}

    .anvisa-box.density-semidense {{
      padding: 2.0mm 2.5mm;
    }}
    .anvisa-box.density-semidense .anvisa-title {{
      font-size: 9.2pt;
      padding-bottom: 0.85mm;
    }}
    .anvisa-box.density-semidense .anvisa-serving-block {{
      font-size: 7.8pt;
      padding: 0.8mm 0.5mm;
      line-height: 1.16;
    }}
    .anvisa-box.density-semidense table.anvisa-table th {{
      font-size: 8.0pt;
      padding: 0.78mm 0.75mm;
    }}
    .anvisa-box.density-semidense table.anvisa-table td {{
      font-size: 7.8pt;
      padding: 0.70mm 0.75mm;
    }}
    .anvisa-box.density-semidense .anvisa-insignificant {{
      font-size: 6.5pt;
      padding: 0.75mm 0.5mm;
    }}
    .anvisa-box.density-semidense .anvisa-footnote {{
      font-size: 6.5pt;
      padding: 0.65mm 0.5mm 0.3mm;
    }}

    .anvisa-box.density-dense {{
      padding: 1.2mm 1.8mm;
    }}
    .anvisa-box.density-dense .anvisa-title {{
      font-size: 8.6pt;
      padding-bottom: 0.55mm;
    }}
    .anvisa-box.density-dense .anvisa-serving-block {{
      font-size: 7.0pt;
      padding: 0.45mm 0.4mm;
      line-height: 1.08;
    }}
    .anvisa-box.density-dense table.anvisa-table th {{
      font-size: 7.2pt;
      padding: 0.44mm 0.55mm;
    }}
    .anvisa-box.density-dense table.anvisa-table td {{
      font-size: 6.8pt;
      padding: 0.36mm 0.55mm;
    }}
    .anvisa-box.density-dense .anvisa-insignificant {{
      font-size: 5.9pt;
      padding: 0.50mm 0.45mm;
    }}
    .anvisa-box.density-dense .anvisa-footnote {{
      font-size: 5.9pt;
      padding: 0.40mm 0.45mm 0.2mm;
    }}

    .anvisa-title {{
      font-family: var(--font-anvisa);
      font-weight: 700;
      text-align: center;
      text-transform: uppercase;
      border-bottom: 0.75pt solid #000000;
      color: #000000;
      letter-spacing: 0.04em;
    }}

    .anvisa-serving-block {{
      font-family: var(--font-anvisa);
      font-weight: 400;
      border-bottom: 2.2pt solid #000000;
      color: #000000;
    }}

    table.anvisa-table {{
      width: 100%;
      border-collapse: collapse;
      font-family: var(--font-anvisa);
      font-weight: 400;
      color: #000000;
      border-bottom: 2pt solid #000000;
    }}

    table.anvisa-table th {{
      font-family: var(--font-anvisa);
      font-weight: 700;
      text-align: center;
      vertical-align: middle;
      border-bottom: 0.75pt solid #000000;
      color: #000000;
      line-height: 1.05;
    }}

    table.anvisa-table th:first-child {{
      width: 58%;
      text-align: left;
      padding-left: 0.6mm;
    }}

    table.anvisa-table th:nth-child(2) {{
      width: 21%;
      border-left: none;
    }}

    table.anvisa-table th:nth-child(3) {{
      width: 21%;
      border-left: 0.75pt solid #000000;
    }}

    table.anvisa-table td {{
      font-family: var(--font-anvisa);
      font-weight: 400;
      border-bottom: 0.75pt solid #000000;
      color: #000000;
    }}

    table.anvisa-table tr:last-child td {{
      border-bottom: none;
    }}

    table.anvisa-table td:first-child {{
      text-align: left;
      padding-left: 0.6mm;
    }}

    table.anvisa-table th:not(:first-child),
    table.anvisa-table td:not(:first-child) {{
      text-align: center;
      border-left: 0.75pt solid #000000;
    }}

    .anvisa-insignificant {{
      font-family: var(--font-anvisa);
      font-weight: 400;
      border-bottom: 0.75pt solid #000000;
      text-align: justify;
      line-height: 1.15;
      color: #000000;
    }}

    .anvisa-footnote {{
      font-family: var(--font-anvisa);
      font-weight: 400;
      text-align: left;
      line-height: 1.12;
      color: #000000;
    }}

    /* FOOTER */
    .bottom-brand-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 2.2mm;
      border-top: 1px solid rgba(0, 0, 0, 0.08);
      font-family: var(--font-ui);
      font-size: 7.2pt;
      color: var(--ink-500);
    }}

    .footer-brand-title {{
      font-family: var(--font-title);
      font-weight: 800;
      font-size: 9.6pt;
      color: var(--theme-dark);
      display: block;
      line-height: 1;
    }}

    .footer-brand-sub {{
      font-size: 6.8pt;
      font-weight: 700;
      color: var(--ink-500);
      text-transform: uppercase;
      letter-spacing: 0.07em;
    }}

    .footer-right-group {{
      display: flex;
      align-items: center;
      gap: 5mm;
    }}

    .footer-col-2 {{
      text-align: right;
      line-height: 1.25;
      font-size: 6.8pt;
      color: var(--ink-700);
    }}

    .footer-col-2 strong {{
      display: block;
      font-family: var(--font-ui);
      color: var(--ink-900);
      font-weight: 800;
      font-size: 6.9pt;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }}

    .footer-col-3 {{
      font-family: var(--font-title);
      font-size: 9.2pt;
      color: var(--theme-dark);
      background: rgba(255, 255, 255, 0.90);
      border: 1px solid var(--glass-border);
      padding: 1.5mm 3.2mm;
      border-radius: 6px;
    }}

    /* ==========================================================================
       PÁGINA 01: CAPA OFICIAL (MODELO RETRATO A4 IGUAL VITAMAIZ)
       ========================================================================== */
    .cover-clean-page {{
      width: 210mm !important;
      height: 297mm !important;
      box-sizing: border-box !important;
      position: relative;
      padding: 0 !important;
      overflow: hidden;
      background: #022045 !important;
    }}

    .cover-image-layer {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-position: center center;
      background-size: cover;
      background-repeat: no-repeat;
      z-index: 1;
    }}

    .cover-content-layer {{
      position: relative;
      z-index: 2;
      padding: 24mm 20mm 22mm 20mm;
      height: 100%;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
    }}

    .cover-brand-top {{
      align-self: flex-start;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 4mm;
      max-width: 115mm;
    }}

    .cover-intercron-pill {{
      font-family: var(--font-ui);
      font-size: 8.5pt;
      font-weight: 800;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #FFC400;
      background: rgba(2, 32, 69, 0.55);
      border: 1px solid rgba(255, 196, 0, 0.45);
      padding: 2mm 4.5mm;
      border-radius: 999px;
      backdrop-filter: blur(8px);
    }}

    .cover-main-logo {{
      width: 96mm;
      height: auto;
      display: block;
      filter: drop-shadow(0 6px 18px rgba(0, 0, 0, 0.28));
    }}

    .cover-brand-divider {{
      width: 68mm;
      height: 3px;
      background: linear-gradient(90deg, #FFC400 0%, rgba(255, 255, 255, 0.6) 65%, rgba(255, 255, 255, 0) 100%);
      border-radius: 2px;
      margin-top: 1mm;
    }}

    .cover-brand-tagline {{
      font-family: var(--font-ui);
      font-size: 9.8pt;
      font-weight: 700;
      color: rgba(255, 255, 255, 0.92);
      letter-spacing: 0.04em;
      margin: 0;
    }}

    .cover-titles-block {{
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      gap: 2.2mm;
    }}

    .cover-edition-label {{
      font-family: var(--font-title);
      font-size: 18pt;
      font-weight: 800;
      color: #FFFFFF !important;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      text-align: center;
      margin: 0;
      text-shadow: 0 2px 12px rgba(0, 0, 0, 0.35);
    }}

    .cover-edition-sub {{
      font-family: var(--font-ui);
      font-size: 7.6pt;
      font-weight: 700;
      color: rgba(255, 255, 255, 0.82);
      letter-spacing: 0.16em;
      text-transform: uppercase;
      margin: 0;
    }}

    /* ==========================================================================
       PÁGINA 02: ÍNDICE DE PRODUTOS (ORGANIZADO POR LINHA)
       ========================================================================== */
    .toc-page {{
      background: #FFFFFF !important;
      --glass-border: #CBD5E1;
      --theme-dark: #0B132B;
    }}

    .toc-simple-header {{
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 2.5mm;
    }}

    .toc-giant-heading {{
      font-family: var(--font-title);
      font-size: 32pt;
      font-weight: 800;
      color: #0F172A;
      letter-spacing: -0.03em;
      line-height: 1;
      margin: 0;
    }}

    .toc-sub-heading {{
      font-family: var(--font-ui);
      font-size: 8.2pt;
      font-weight: 700;
      color: #64748B;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-top: 1.4mm;
    }}

    .toc-header-brand {{
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 1mm;
    }}

    .toc-simple-logo {{
      width: 44mm;
      height: auto;
      display: block;
    }}

    .toc-brand-caption {{
      font-family: var(--font-ui);
      font-size: 6.6pt;
      font-weight: 800;
      letter-spacing: 0.12em;
      color: #475569;
      text-transform: uppercase;
    }}

    .toc-columns-wrapper {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6mm;
      flex: 1;
      align-items: stretch;
      min-height: 0;
    }}

    .toc-col {{
      display: flex;
      flex-direction: column;
      gap: 3.2mm;
      justify-content: flex-start;
      height: 100%;
    }}

    .toc-category-card {{
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 12px;
      padding: 3.2mm 4.0mm;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
    }}

    .toc-category-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 1.8mm;
      margin-bottom: 1.8mm;
      border-bottom: 1.5px solid #E2E8F0;
      flex-shrink: 0;
    }}

    .toc-cat-pill {{
      font-family: var(--font-title);
      font-size: 8.2pt;
      font-weight: 800;
      padding: 1.1mm 3.2mm;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .badge-borg {{
      background: #FEF3C7;
      color: #92400E;
    }}

    .badge-cartimaster {{
      background: #FFEDD5;
      color: #9A3412;
    }}

    .badge-cronovit {{
      background: #FCE7F3;
      color: #9D174D;
    }}

    .badge-cronoliv {{
      background: #EDE9FE;
      color: #5B21B6;
    }}

    .badge-nutrivix {{
      background: #CCFBF1;
      color: #115E59;
    }}

    .badge-odessy {{
      background: #DBEAFE;
      color: #1E40AF;
    }}

    .badge-especiais {{
      background: #E0F2FE;
      color: #0369A1;
    }}

    .toc-cat-count {{
      font-family: var(--font-ui);
      font-size: 7.2pt;
      font-weight: 700;
      color: #64748B;
    }}

    .toc-clean-list {{
      list-style: none;
      padding: 0;
      margin: 0;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      gap: 1.2mm;
    }}

    .toc-clean-item {{
      margin: 0;
      padding: 0;
    }}

    .toc-item-link {{
      display: flex;
      align-items: baseline;
      font-size: 8.5pt;
      line-height: 1.28;
      text-decoration: none;
      color: inherit;
    }}

    .toc-clean-name {{
      font-weight: 600;
      color: #1E293B;
      flex-shrink: 0;
    }}

    .toc-clean-leader {{
      flex: 1;
      border-bottom: 1px dotted #CBD5E1;
      margin: 0 2mm;
      height: 1px;
    }}

    .toc-clean-page {{
      font-family: var(--font-title);
      font-size: 7.8pt;
      font-weight: 700;
      color: #475569;
      flex-shrink: 0;
    }}

    /* ==========================================================================
       PÁGINA 40: CONTRACAPA INSTITUCIONAL (FECHAMENTO A4)
       ========================================================================== */
    .back-cover-clean-page {{
      width: 210mm !important;
      height: 297mm !important;
      box-sizing: border-box !important;
      position: relative;
      padding: 0 !important;
      overflow: hidden;
      background: #FFFFFF !important;
      display: flex !important;
      flex-direction: column !important;
      justify-content: space-between !important;
      align-items: center !important;
    }}

    .back-cover-top-bar {{
      width: 100%;
      height: 4mm;
      background: var(--brand-spectrum);
    }}

    .back-cover-content {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      gap: 5.5mm;
      flex: 1;
      width: 100%;
      padding: 0 24mm;
    }}

    .back-cover-pill {{
      font-family: var(--font-ui);
      font-size: 8.5pt;
      font-weight: 800;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #0B132B;
      background: #F1F5F9;
      border: 1px solid #CBD5E1;
      padding: 2mm 5mm;
      border-radius: 999px;
    }}

    .back-cover-logo {{
      width: 105mm;
      height: auto;
      display: block;
    }}

    .back-cover-spectrum {{
      width: 72mm;
      height: 3px;
      background: var(--brand-spectrum);
      border-radius: 2px;
    }}

    .back-cover-tagline {{
      font-family: var(--font-title);
      font-size: 11pt;
      font-weight: 700;
      color: #334155;
      letter-spacing: 0.02em;
      margin: 0;
    }}

    .back-cover-lines {{
      font-family: var(--font-ui);
      font-size: 7.4pt;
      font-weight: 800;
      color: #64748B;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      margin: 0;
    }}

    .back-cover-footer {{
      width: 100%;
      padding: 6mm 20mm 8mm 20mm;
      border-top: 1px solid #E2E8F0;
      text-align: center;
      font-family: var(--font-ui);
      font-size: 7.2pt;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: #64748B;
      text-transform: uppercase;
    }}
    {EDITOR_CSS}
  </style>
</head>
<body>
  {EDITOR_BODY_START}
  <main class="catalog-wrapper">
    {all_pages_combined}
  </main>
  {EDITOR_BODY_END}
</body>
</html>
"""

    # Backup preventivo antes de sobrescrever
    backup_dir = WORKSPACE_DIR / "backups"
    backup_dir.mkdir(parents=True, exist_ok=True)
    if OUTPUT_HTML.exists():
        import datetime
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        (backup_dir / f"catalogo_pre_build_{ts}.html").write_text(OUTPUT_HTML.read_text(encoding="utf-8"), encoding="utf-8")

    OUTPUT_HTML.write_text(html_content, encoding="utf-8")
    print(f"✅ HTML Consolidado gravado com sucesso em: {OUTPUT_HTML}")
    print(f"   Tamanho do arquivo: {OUTPUT_HTML.stat().st_size:,} bytes")


if __name__ == "__main__":
    build_catalog()
