#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MD_DIR = BASE_DIR / "md_embalagens"
MD_DIR.mkdir(parents=True, exist_ok=True)

def render_md(data: dict) -> str:
    # Frontmatter
    lines = [
        "---",
        f'produto: "{data["produto"]}"',
        f'linha: "{data["linha"]}"',
        f'forma: "{data["forma"]}"',
        f'apresentacao: "{data["apresentacao"]}"',
        f'notificacao_anvisa: "{data.get("notificacao_anvisa", "")}"',
        f'pagina_pdf: {data["pagina_pdf"]}',
        f'ean: "{data.get("ean", "")}"',
        f'faca: "{data.get("faca", "")}"',
        "---",
        "",
        f'# {data["titulo"]}',
        "",
        "## 1. Painel Principal (Frente da Embalagem)",
        f'- Marca: {data["linha"]}',
        f'- Produto: {data["produto"]}',
        f'- Denominação de venda: {data["denominacao"]}',
        f'- Apresentação: {data["apresentacao"]}',
        f'- Forma: {data["forma"]}',
    ]
    if data.get("sabor"):
        lines.append(f'- Sabor: {data["sabor"]}')
    lines.extend([
        f'- Destaques frontais: {data["destaques_frontais"]}',
        f'- Via e uso: {data["via_uso"]}',
        "",
        "## 2. Informação Nutricional",
        f'Porções por embalagem: {data["porcoes_emb"]}',
        f'Porção: {data["porcao"]}',
        "",
    ])

    # Tabela
    # Header
    col1_w = max(len("Informação Nutricional"), max((len(r[0]) for r in data["tabela"]), default=20))
    col2_w = max(len(f'Quantidade por porção ({data["porcao"].split("(")[0].strip()})'), max((len(r[1]) for r in data["tabela"]), default=15))
    col3_w = max(len("% VD (*)"), max((len(r[2]) for r in data["tabela"]), default=8))

    header_col2 = f'Quantidade por porção ({data["porcao"].split("(")[0].strip()})'
    lines.append(f'| Informação Nutricional | {header_col2} | % VD (*) |')
    lines.append(f'| :--- | :--- | :--- |')
    for row in data["tabela"]:
        vd_val = row[2] if len(row) > 2 else ""
        lines.append(f'| {row[0]} | {row[1]} | {vd_val} |')
    lines.append("")

    if data.get("insignificante"):
        lines.append(data["insignificante"])
        lines.append("")
    if data.get("nota_vd"):
        lines.append(data["nota_vd"])
        lines.append("")

    lines.extend([
        "## 3. Dizeres de Rotulagem (Texto da Embalagem)",
        f'**INGREDIENTES:** {data["ingredientes"]}',
        "",
        f'**ALÉRGICOS:** {data["alergicos"]}',
        "",
        f'**RECOMENDAÇÃO DE USO:** {data["recomendacao"]}',
        "",
    ])

    if data.get("modo_preparo"):
        lines.extend([
            f'**MODO DE PREPARO:** {data["modo_preparo"]}',
            "",
        ])

    lines.extend([
        "**ADVERTÊNCIAS E CONSERVAÇÃO:**",
        data["advertencias"],
        data["conservacao"],
        "",
    ])

    if data.get("alegacoes"):
        lines.append("**ALEGAÇÕES DO RÓTULO:**")
        for al in data["alegacoes"]:
            lines.append(f'- {al}')
        lines.append("")

    lines.extend([
        "## 4. Dados do Fabricante e Regulatórios",
        f'- Fabricado e Distribuído por: {data["fabricante"]}',
        f'- CNPJ: {data["cnpj"]}',
        f'- Endereço: {data["endereco"]}',
        f'- Registro / Notificação Anvisa: {data.get("notificacao_anvisa", "Alimento notificado na Anvisa conforme legislação vigente")}',
        f'- Farmacêutica Responsável: {data["crf"]}',
        f'- SAC: {data["sac"]}',
        f'- Site: {data["site"]}',
        "",
        "## 5. Informações Administrativas e Históricas (Uso Interno)",
        f'- Página do Catálogo PDF: Página {data["pagina_pdf"]}',
        f'- Código EAN / Código de Barras: {data.get("ean", "N/A")}',
        f'- Código interno da arte / Versão: {data.get("codigo_arte", "N/A")}',
        f'- Dimensões da Faca Técnica: {data.get("faca", "N/A")}',
        f'- Acabamento Gráfico: {data.get("acabamento", "N/A")}',
        f'- Cores de Impressão: {data.get("cores", "N/A")}',
        f'- Sistema de Fechamento: {data.get("fechamento", "N/A")}',
        f'- Histórico e Linha: {data.get("historico", "N/A")}',
        ""
    ])

    return "\n".join(lines)

print("build_all_mds.py template renderer loaded.")
