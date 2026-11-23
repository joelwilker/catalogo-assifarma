#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Geração dos Arquivos Markdown (.md) das 38 Páginas do PDF
'PRODUTOS EMBALAGENS.pdf' do Catálogo Assifarma / Forhealth.
Segue estritamente o padrão dos arquivos de embalagens do Catálogo VitaMaiz.
"""

import os
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent / "md_embalagens"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PAGES_DATA = [
    # -------------------------------------------------------------------------
    # PÁGINA 1
    # -------------------------------------------------------------------------
    {
        "filename": "pagina_01_borg_calcio_500mg_60_comprimidos.md",
        "pagina_pdf": 1,
        "produto": "Borg Cálcio 500mg",
        "linha": "Borg",
        "forma": "Comprimido",
        "apresentacao": "60 comprimidos",
        "notificacao_anvisa": "25351064162202664",
        "ean": "7908079521774",
        "faca": "74X74X126MM",
        "acabamento": "Verniz UV",
        "cores": "Policromia (Ciano, Magenta, Amarelo, Preto)",
        "fechamento": "Fechamento Fundo Automático",
        "codigo_arte": "007690-0626A",
        "titulo": "Borg Cálcio 500mg",
        "denominacao": "SUPLEMENTO ALIMENTAR EM COMPRIMIDOS",
        "destaques_frontais": "Não contém açúcares, Não contém glúten, O cálcio auxilia na formação e manutenção de ossos e dentes",
        "via_uso": "Via Oral - Uso Adulto (≥ 19 anos)",
        "porcoes_emb": "60",
        "porcao": "1,5 g (1 comprimido)",
        "tabela": [
            ("Cálcio (mg)", "500 mg", "50%"),
        ],
        "insignificante": "Não contém quantidades significativas de Valor energético, Carboidratos, Açúcares totais, Açúcares adicionados, Proteínas, Gorduras totais, Gorduras saturadas, Gorduras trans, Fibras alimentares e Sódio.",
        "nota_vd": "(*) Percentual de valores diários fornecidos pela porção.",
        "ingredientes": "Carbonato de Cálcio, Antiumectantes Celulose em Pó INS 460(ii), Dióxido de Silício INS 551 e Estearato de Magnésio INS 470(iii), Estabilizantes Carboximetilcelulose Sódica Reticulada INS 468 e Polivinilpirrolidona INS 1201, Glaceante Hidroxipropilmetilcelulose INS 464.",
        "alergicos": "PODE CONTER LEITE, PEIXES E SOJA. NÃO CONTÉM GLÚTEN.",
        "recomendacao": "Recomendações de uso: 1 (um) comprimido ao dia, para adultos ≥ 19 anos.",
        "advertencias": "PRODUTO DESTINADO A ADULTOS (≥ 19 ANOS). ESTE PRODUTO NÃO É UM MEDICAMENTO. NÃO EXCEDER A RECOMENDAÇÃO DIÁRIA DE CONSUMO INDICADA NA EMBALAGEM. MANTENHA FORA DO ALCANCE DE CRIANÇAS.",
        "conservacao": "CUIDADOS DE CONSERVAÇÃO: CONSERVAR AO ABRIGO DA LUZ, UMIDADE E CALOR EXCESSIVO, E COM A EMBALAGEM FECHADA, INCLUSIVE APÓS ABERTO. NÃO CONSUMIR ESTE PRODUTO, CASO O LACRE DE SEGURANÇA ESTEJA VIOLADO. APÓS ABERTO CONSUMIR EM ATÉ 60 DIAS. Lote, fabricação e validade impressos na embalagem.",
        "alegacoes": [
            "O cálcio auxilia na formação e manutenção de ossos e dentes.",
            "O cálcio auxilia no funcionamento muscular e neuromuscular.",
            "O cálcio auxilia no metabolismo energético.",
            "O cálcio auxilia na coagulação do sangue e na divisão celular."
        ],
        "fabricante": "Forhealth Nutricional Ltda.",
        "cnpj": "19.676.466/0001-30",
        "endereco": "SPLM Conjunto 5, Lote 9 - Placa da Mercedes, Núcleo Bandeirante, Brasília - DF, CEP: 71.732-050, Indústria Brasileira",
        "crf": "Thalita Alves da Silva - CRF/DF nº 589799",
        "sac": "(61) 3297-9321",
        "site": "www.forhealthnutrition.com.br",
        "historico": "Licença Intercron S.A. Embalagem com cartuchadeira padrão 74x74x126mm com verniz UV."
    },

    # -------------------------------------------------------------------------
    # PÁGINA 2
    # -------------------------------------------------------------------------
    {
        "filename": "pagina_02_borg_coenzima_q10_60_capsulas_softgel.md",
        "pagina_pdf": 2,
        "produto": "Borg Coenzima Q10",
        "linha": "Borg",
        "forma": "Cápsula Softgel",
        "apresentacao": "60 cápsulas",
        "notificacao_anvisa": "Dispensado de registro / Notificado conforme RDC Anvisa",
        "ean": "7908079500342",
        "faca": "74X74X126MM",
        "acabamento": "Verniz UV",
        "cores": "Policromia (Ciano, Magenta, Amarelo, Preto)",
        "fechamento": "Fechamento Fundo Automático",
        "codigo_arte": "00291 - 1225B / Nova Embalagem",
        "titulo": "Borg Coenzima Q10 100mg com Vitaminas e Minerais",
        "denominacao": "SUPLEMENTO ALIMENTAR EM CÁPSULAS",
        "destaques_frontais": "Coenzima Q10 100mg, Licopeno 5mg, Óleo de Semente de Uva, Vitaminas & Minerais, Softgel",
        "via_uso": "Via Oral - Uso Adulto (≥ 19 anos)",
        "porcoes_emb": "30",
        "porcao": "2 g (2 cápsulas)",
        "tabela": [
            ("Valor energético (kcal)", "7 kcal", "0%"),
            ("Gorduras totais (g)", "0,8 g", "1%"),
            ("Gorduras saturadas (g)", "0,1 g", "1%"),
            ("Gorduras monoinsaturadas (g)", "0,1 g", "0%"),
            ("  Ácido oleico (g)", "0,1 g", ""),
            ("Gorduras poli-insaturadas (g)", "0,5 g", "2%"),
            ("  Ácido linolênico (g)", "0,5 g", ""),
            ("Colesterol (mg)", "0 mg", "0%"),
            ("Vitamina A (µg)", "600 µg", "75%"),
            ("Vitamina E (mg)", "10 mg", "67%"),
            ("Vitamina C (mg)", "45 mg", "45%"),
            ("Selênio (µg)", "34 µg", "57%"),
            ("Zinco (mg)", "7 mg", "64%"),
            ("Coenzima Q10 (mg)", "100 mg", ""),
            ("Licopeno (mg)", "5 mg", ""),
        ],
        "insignificante": "Não contém quantidades significativas de Carboidratos, Açúcares totais, Açúcares adicionados, Proteínas, Fibras alimentares e Sódio.",
        "nota_vd": "(*) Percentual de valores diários fornecidos pela porção.",
        "ingredientes": "Óleo de Semente de Uva (Vitis vinifera), Coenzima Q10, Ácido Ascórbico (Vitamina C), Licopeno Sintético, Óxido de Zinco, Acetato de DL-Alfa-Tocoferol (Vitamina E), Palmitato de Retinol (Vitamina A), Selenito de Sódio, Emulsificante Lecitina de Soja e Glaceante Cera de Abelha. Cápsula: Gelificante Gelatina, Umectante Glicerol, Água Purificada e Corantes Dióxido de Titânio, Vermelho Carmim e Óxido de Ferro Preto.",
        "alergicos": "CONTÉM DERIVADOS DE SOJA. PODE CONTER LEITE E PEIXE. NÃO CONTÉM GLÚTEN.",
        "recomendacao": "Recomenda-se a ingestão de 1 (uma) cápsula 2 (duas) vezes ao dia para adultos ≥ 19 anos.",
        "advertencias": "PRODUTO DESTINADO A ADULTOS (≥ 19 ANOS). ESTE PRODUTO NÃO É UM MEDICAMENTO. NÃO EXCEDER A RECOMENDAÇÃO DIÁRIA DE CONSUMO INDICADA NA EMBALAGEM. MANTENHA FORA DO ALCANCE DE CRIANÇAS. ESTE PRODUTO NÃO DEVE SER CONSUMIDO POR GESTANTES, LACTANTES E CRIANÇAS.",
        "conservacao": "CUIDADOS DE CONSERVAÇÃO: CONSERVAR AO ABRIGO DA LUZ, UMIDADE E CALOR EXCESSIVO, E COM A EMBALAGEM FECHADA, INCLUSIVE APÓS ABERTO. NÃO CONSUMIR ESTE PRODUTO, CASO O LACRE DE SEGURANÇA ESTEJA VIOLADO. APÓS ABERTO CONSUMIR EM ATÉ 60 DIAS. Lote, fabricação e validade impressos na embalagem.",
        "alegacoes": [
            "A Vitamina E e a Vitamina C são antioxidantes que auxiliam na proteção dos danos causados pelos radicais livres.",
            "O Zinco e a Vitamina C auxiliam no funcionamento do sistema imune.",
            "A Vitamina A contribui para a manutenção da pele e visão.",
            "O Zinco contribui para a manutenção do cabelo, da pele e das unhas e no metabolismo de proteínas, carboidratos e gorduras."
        ],
        "fabricante": "Forhealth Nutricional Ltda.",
        "cnpj": "19.676.466/0001-30",
        "endereco": "SPLM Conjunto 5, Lote 9 - Placa da Mercedes, Núcleo Bandeirante, Brasília - DF, CEP: 71.732-050, Indústria Brasileira",
        "crf": "Thalita Alves da Silva - CRF/DF nº 589799",
        "sac": "(61) 3297-9321",
        "site": "www.forhealthnutrition.com.br",
        "historico": "Licença Intercron S.A. Formulação rica em Coenzima Q10 carreada em óleo de semente de uva."
    },

    # -------------------------------------------------------------------------
    # PÁGINA 3
    # -------------------------------------------------------------------------
    {
        "filename": "pagina_03_borg_cog_memo_60_capsulas_softgel.md",
        "pagina_pdf": 3,
        "produto": "Borg Cog Memo",
        "linha": "Borg",
        "forma": "Cápsula Softgel",
        "apresentacao": "60 cápsulas",
        "notificacao_anvisa": "Dispensado de registro / Notificado conforme RDC Anvisa",
        "ean": "7908079515520",
        "faca": "74X74X126MM",
        "acabamento": "Verniz UV",
        "cores": "Policromia (Ciano, Magenta, Amarelo, Preto)",
        "fechamento": "Fechamento Fundo Automático",
        "codigo_arte": "005403 - 1125A / Nova Embalagem",
        "titulo": "Borg Cog Memo",
        "denominacao": "SUPLEMENTO ALIMENTAR EM CÁPSULAS",
        "destaques_frontais": "Fosfatidilserina 100mg, Tirosina 100mg, Cafeína 75mg, Colina, Vitaminas e Minerais, Softgel",
        "via_uso": "Via Oral - Uso Adulto (≥ 19 anos)",
        "porcoes_emb": "30",
        "porcao": "1 g (2 cápsulas)",
        "tabela": [
            ("Valor energético (kcal)", "7 kcal", "0%"),
            ("Gorduras totais (g)", "0,8 g", "1%"),
            ("Gorduras saturadas (g)", "0,1 g", "1%"),
            ("Gorduras monoinsaturadas (g)", "0,2 g", "1%"),
            ("Gorduras poli-insaturadas (g)", "0,5 g", "2%"),
            ("Vitamina D (µg)", "5 µg", "33%"),
            ("Vitamina E (mg)", "10 mg", "67%"),
            ("Vitamina B1 (mg)", "1,2 mg", "100%"),
            ("Ácido Pantotênico (mg)", "5 mg", "100%"),
            ("Vitamina B6 (mg)", "1,3 mg", "100%"),
            ("Ácido Fólico (µg)", "240 µg", "100%"),
            ("Vitamina B12 (µg)", "2,4 µg", "100%"),
            ("Magnésio (mg)", "63 mg", "15%"),
            ("Selênio (µg)", "34 µg", "57%"),
            ("Zinco (mg)", "7 mg", "64%"),
            ("Colina (mg)", "82,5 mg", "15%"),
            ("Cafeína (mg)", "75 mg", ""),
            ("Fosfatidilserina (mg)", "100 mg", ""),
            ("Tirosina (mg)", "100 mg", ""),
        ],
        "insignificante": "Não contém quantidades significativas de Carboidratos, Açúcares totais, Açúcares adicionados, Proteínas, Fibras alimentares e Sódio.",
        "nota_vd": "(*) Percentual de valores diários fornecidos pela porção.",
        "ingredientes": "Óleo de Girassol (Helianthus Annuus L.), Fosfatidilserina de Lecitina de Soja, L-Tirosina, Bitartarato de Colina, Cafeína Anidra, Óxido de Magnésio, Bisglicinato de Zinco, Acetato de DL-Alfa-Tocoferol, D-Pantotenato de Cálcio, Cloridrato de Piridoxina, Nitrato de Tiamina, Ácido Fólico, Selenito de Sódio, Colecalciferol, Cianocobalamina, Emulsificante Lecitina de Soja e Glaceante Cera de Abelha. Cápsula: Gelificante Gelatina, Umectante Glicerol, Água Purificada e Corantes Dióxido de Titânio e Corante Azul Brilhante.",
        "alergicos": "CONTÉM DERIVADOS DE SOJA. PODE CONTER LEITE E PEIXES. NÃO CONTÉM GLÚTEN.",
        "recomendacao": "Recomendações de uso: 2 (duas) cápsulas ao dia, para adultos ≥ 19 anos.",
        "advertencias": "PRODUTO DESTINADO A ADULTOS (≥ 19 ANOS). ESTE PRODUTO NÃO É UM MEDICAMENTO. NÃO EXCEDER A RECOMENDAÇÃO DIÁRIA DE CONSUMO INDICADA NA EMBALAGEM. MANTENHA FORA DO ALCANCE DE CRIANÇAS. ESTE PRODUTO NÃO DEVE SER CONSUMIDO POR GESTANTES, LACTANTES E CRIANÇAS.",
        "conservacao": "CUIDADOS DE CONSERVAÇÃO: CONSERVAR AO ABRIGO DA LUZ, UMIDADE E CALOR EXCESSIVO, E COM A EMBALAGEM FECHADA, INCLUSIVE APÓS ABERTO. NÃO CONSUMIR ESTE PRODUTO, CASO O LACRE DE SEGURANÇA ESTEJA VIOLADO. APÓS ABERTO CONSUMIR EM ATÉ 60 DIAS. Lote, fabricação e validade impressos na embalagem.",
        "alegacoes": [
            "A cafeína auxilia no aumento do estado de alerta e na melhora da concentração.",
            "A colina contribui para o metabolismo lipídico e da homocisteína.",
            "As vitaminas B1, B6, B12 e o ácido pantotênico auxiliam no metabolismo energético.",
            "O zinco e a vitamina E são antioxidantes que auxiliam na proteção dos danos causados pelos radicais livres."
        ],
        "fabricante": "Forhealth Nutricional Ltda.",
        "cnpj": "19.676.466/0001-30",
        "endereco": "SPLM Conjunto 5, Lote 9 - Placa da Mercedes, Núcleo Bandeirante, Brasília - DF, CEP: 71.732-050, Indústria Brasileira",
        "crf": "Thalita Alves da Silva - CRF/DF nº 589799",
        "sac": "(61) 3297-9321",
        "site": "www.forhealthnutrition.com.br",
        "historico": "Licença Intercron S.A. Desenvolvido para suporte cognitivo e foco mental."
    },

    # -------------------------------------------------------------------------
    # PÁGINA 4
    # -------------------------------------------------------------------------
    {
        "filename": "pagina_04_borg_feno_grego_60_capsulas_dura.md",
        "pagina_pdf": 4,
        "produto": "Borg Feno Grego",
        "linha": "Borg",
        "forma": "Cápsula Dura",
        "apresentacao": "60 cápsulas",
        "notificacao_anvisa": "25351145825202560",
        "ean": "7908079514554",
        "faca": "118X95X45MM",
        "acabamento": "Verniz UV",
        "cores": "Policromia (Ciano, Magenta, Amarelo, Preto) + Pantone 871C",
        "fechamento": "Fechamento Fundo Automático",
        "codigo_arte": "005404 - 1225A",
        "titulo": "Borg Feno Grego 600mg com Boro, Zinco e Vitamina B6",
        "denominacao": "SUPLEMENTO ALIMENTAR EM CÁPSULAS",
        "destaques_frontais": "Feno Grego 600mg*, Saponinas 450mg, Boro 4mg, Zinco 29mg, Vitamina B6 5mg, Sem Açúcar, Sem Glúten",
        "via_uso": "Via Oral - Uso Adulto (≥ 19 anos)",
        "porcoes_emb": "30",
        "porcao": "1 g (2 cápsulas)",
        "tabela": [
            ("Vitamina B6 (mg)", "5 mg", "385%"),
            ("Zinco (mg)", "29 mg", "264%"),
            ("Boro (mg)", "4 mg", ""),
            ("Saponinas (Glicosídeos de Furostanol) (mg)", "450 mg", ""),
        ],
        "insignificante": "Não contém quantidades significativas de Valor Energético, Carboidratos, Açúcares Totais, Açúcares Adicionados, Proteínas, Gorduras Totais, Gorduras Saturadas, Gorduras Trans, Fibras Alimentares e Sódio.",
        "nota_vd": "(*) Percentual de valores diários fornecidos pela porção. Contém 450mg de saponinas provenientes de 600mg de extrato de feno grego.",
        "ingredientes": "Extrato de Semente de Feno Grego (Trigonella Foenum-Graecum L.), Tetraborato de Sódio Decahidratado, Óxido de Zinco, Amido de Milho (Zea Mays), Cloridrato de Piridoxina, Antioxidante D-Alfa-Tocoferol INS 307(a), Antiumectantes Celulose em Pó INS 460(ii), Estearato de Magnésio INS 470(iii) e Dióxido de Silício INS 551, Estabilizante Croscarmelose Sódica INS 468; Cápsula: Gelificante Gelatina INS 428, Corantes Dióxido de Titânio INS 171, Azul Brilhante FCF INS 133 e Eritrosina INS 127.",
        "alergicos": "PODE CONTER LEITE, PEIXE E SOJA. NÃO CONTÉM GLÚTEN.",
        "recomendacao": "Recomendações de uso: 2 (duas) cápsulas ao dia, para adultos ≥ 19 anos.",
        "advertencias": "PRODUTO DESTINADO A ADULTOS (≥ 19 ANOS). ESTE PRODUTO NÃO É UM MEDICAMENTO. NÃO EXCEDER A RECOMENDAÇÃO DIÁRIA DE CONSUMO INDICADA NA EMBALAGEM. MANTENHA FORA DO ALCANCE DE CRIANÇAS. ESTE PRODUTO NÃO DEVE SER CONSUMIDO POR GESTANTES, LACTANTES E CRIANÇAS.",
        "conservacao": "CUIDADOS DE CONSERVAÇÃO: CONSERVAR AO ABRIGO DA LUZ, UMIDADE E CALOR EXCESSIVO, E COM A EMBALAGEM FECHADA, INCLUSIVE APÓS ABERTO. NÃO CONSUMIR ESTE PRODUTO, CASO O LACRE DE SEGURANÇA ESTEJA VIOLADO. APÓS ABERTO CONSUMIR EM ATÉ 60 DIAS. Lote, fabricação e validade impressos na embalagem.",
        "alegacoes": [
            "A vitamina B6 auxilia no metabolismo energético e no metabolismo de proteínas e do glicogênio.",
            "O zinco auxilia no funcionamento do sistema imune e na síntese de proteínas.",
            "O zinco auxilia na manutenção dos níveis de testosterona no sangue e no metabolismo de carboidratos e gorduras."
        ],
        "fabricante": "Forhealth Nutricional Ltda.",
        "cnpj": "19.676.466/0001-30",
        "endereco": "SPLM Conjunto 5, Lote 9 - Placa da Mercedes, Núcleo Bandeirante, Brasília - DF, CEP: 71.732-050, Indústria Brasileira",
        "crf": "Thalita Alves da Silva - CRF/DF nº 589799",
        "sac": "(61) 3297-9321",
        "site": "www.forhealthnutrition.com.br",
        "historico": "Notificação Sanitária ANVISA nº 25351145825202560. Cartucho faca 118x95x45mm com tinta especial Pantone 871C dourada."
    },

    # -------------------------------------------------------------------------
    # PÁGINA 5
    # -------------------------------------------------------------------------
    {
        "filename": "pagina_05_borg_magnesio_dimalato_60_capsulas_dura.md",
        "pagina_pdf": 5,
        "produto": "Borg Magnésio Dimalato",
        "linha": "Borg",
        "forma": "Cápsula Dura",
        "apresentacao": "60 cápsulas",
        "notificacao_anvisa": "25351097247202548",
        "ean": "7908079503602",
        "faca": "74X74X126MM",
        "acabamento": "Verniz UV",
        "cores": "Policromia (Ciano, Magenta, Amarelo, Preto)",
        "fechamento": "Fechamento Fundo Automático",
        "codigo_arte": "602 - 1225B / Nova Embalagem",
        "titulo": "Borg Magnésio Dimalato",
        "denominacao": "SUPLEMENTO ALIMENTAR EM CÁPSULAS",
        "destaques_frontais": "Fonte de Magnésio, 260mg de Magnésio por porção, Não contém açúcares, Não contém glúten",
        "via_uso": "Via Oral - Uso Adulto (≥ 19 anos)",
        "porcoes_emb": "15",
        "porcao": "1,5 g (4 cápsulas)",
        "tabela": [
            ("Magnésio (mg)", "260 mg", "62%"),
        ],
        "insignificante": "Não contém quantidades significativas de Valor energético, Carboidratos, Açúcares totais, Açúcares adicionados, Proteínas, Gorduras totais, Gorduras saturadas, Gorduras trans, Fibras alimentares e Sódio.",
        "nota_vd": "(*) Percentual de valores diários fornecidos pela porção.",
        "ingredientes": "Dimagnésio Malato, Óxido de Magnésio, Amido de Milho (Zea Mays), Antiumectantes Celulose em Pó INS 460(ii), Dióxido de Silício INS 551 e Estearato de Magnésio INS 470(iii), Estabilizante Croscarmelose Sódica INS 468 e Antioxidante D-Alfa-Tocoferol INS 307a; Cápsula: Gelificante Gelatina INS 428 e Corante Dióxido de Titânio INS 171.",
        "alergicos": "PODE CONTER LEITE, PEIXES E SOJA. NÃO CONTÉM GLÚTEN.",
        "recomendacao": "Recomendações de uso: 2 (duas) cápsulas duas vezes ao dia, para adultos ≥ 19 anos.",
        "advertencias": "PRODUTO DESTINADO A ADULTOS (≥ 19 ANOS). ESTE PRODUTO NÃO É UM MEDICAMENTO. NÃO EXCEDER A RECOMENDAÇÃO DIÁRIA DE CONSUMO INDICADA NA EMBALAGEM. MANTENHA FORA DO ALCANCE DE CRIANÇAS.",
        "conservacao": "CUIDADOS DE CONSERVAÇÃO: CONSERVAR AO ABRIGO DA LUZ, UMIDADE E CALOR EXCESSIVO, E COM A EMBALAGEM FECHADA, INCLUSIVE APÓS ABERTO. NÃO CONSUMIR ESTE PRODUTO, CASO O LACRE DE SEGURANÇA ESTEJA VIOLADO. APÓS ABERTO CONSUMIR EM ATÉ 60 DIAS. Lote, fabricação e validade impressos na embalagem.",
        "alegacoes": [
            "O magnésio auxilia no funcionamento muscular e neuromuscular.",
            "O magnésio auxilia no metabolismo energético e no metabolismo de proteínas, carboidratos e gorduras.",
            "O magnésio auxilia na formação e manutenção de ossos e dentes e no equilíbrio dos eletrólitos."
        ],
        "fabricante": "Forhealth Nutricional Ltda.",
        "cnpj": "19.676.466/0001-30",
        "endereco": "SPLM Conjunto 5, Lote 9 - Placa da Mercedes, Núcleo Bandeirante, Brasília - DF, CEP: 71.732-050, Indústria Brasileira",
        "crf": "Thalita Alves da Silva - CRF/DF nº 589799",
        "sac": "(61) 3297-9321",
        "site": "www.forhealthnutrition.com.br",
        "historico": "Notificação Sanitária ANVISA nº 25351097247202548. Linha Borg de sais nobres de magnésio."
    },
]

print(f"Estrutura base pronta com {len(PAGES_DATA)} páginas piloto.")
