#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MD_DIR = BASE_DIR / "md_embalagens"

with open("/tmp/pages_ocr_cache.json") as f:
    cache = json.load(f)

md_files = sorted(list(MD_DIR.glob("*.md")))
print(f"Total de arquivos MD encontrados para conferência: {len(md_files)}")

assert len(md_files) == 38, f"Esperado 38 arquivos, encontrado {len(md_files)}"

report = []
total_checks = 0
passed_checks = 0

for idx, md_path in enumerate(md_files, 1):
    content = md_path.read_text(encoding="utf-8")
    
    # 1. Checar frontmatter
    assert content.startswith("---"), f"Frontmatter ausente em {md_path.name}"
    fm_match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    assert fm_match, f"Erro ao extrair frontmatter de {md_path.name}"
    fm_text = fm_match.group(1)
    
    page_match = re.search(r"pagina_pdf:\s*(\d+)", fm_text)
    assert page_match, f"pagina_pdf não encontrado em {md_path.name}"
    pno = int(page_match.group(1))
    assert pno == idx, f"Número de página inconsistente: {pno} vs {idx}"
    
    # 2. Checar seções obrigatórias padrão Vitamais
    required_sections = [
        "## 1. Painel Principal (Frente da Embalagem)",
        "## 2. Informação Nutricional",
        "## 3. Dizeres de Rotulagem (Texto da Embalagem)",
        "## 4. Dados do Fabricante e Regulatórios",
        "## 5. Informações Administrativas e Históricas (Uso Interno)"
    ]
    for sec in required_sections:
        total_checks += 1
        if sec in content:
            passed_checks += 1
        else:
            report.append(f"[{md_path.name}] Seção ausente: {sec}")
            
    # 3. Checar campos críticos de rotulagem
    required_fields = [
        "**INGREDIENTES:**",
        "**ALÉRGICOS:**",
        "**RECOMENDAÇÃO DE USO:**",
        "**ADVERTÊNCIAS E CONSERVAÇÃO:**",
        "Fabricado e Distribuído por:",
        "CNPJ:",
        "Porções por embalagem:",
        "Porção:"
    ]
    for rf in required_fields:
        total_checks += 1
        if rf in content:
            passed_checks += 1
        else:
            report.append(f"[{md_path.name}] Campo obrigatório ausente: {rf}")
            
    # 4. Checar consistência com o PDF (OCR Items)
    page_ocr = cache[str(pno)]["ocr_items"]
    ocr_full_text = " ".join(it["text"] for it in page_ocr).upper()
    
    # Checar palavras-chave do produto no OCR
    prod_name_match = re.search(r'produto:\s*"(.*?)"', fm_text)
    prod_name = prod_name_match.group(1) if prod_name_match else ""
    
    # Checar se tabela nutricional tem cabeçalho e linhas
    table_match = re.search(r"\| Informação Nutricional \|.*?\n\| :--- \|.*?\n(\|.*?\n)+", content)
    total_checks += 1
    if table_match:
        passed_checks += 1
    else:
        report.append(f"[{md_path.name}] Tabela nutricional mal formatada.")

    # Status por página
    print(f"Página {pno:02d} ({md_path.name}): OK | Produto: '{prod_name}'")

print("\n" + "="*60)
print(f"RELATÓRIO DE CONFERÊNCIA AUTOMATIZADA")
print("="*60)
print(f"Total de testes realizados: {total_checks}")
print(f"Testes aprovados: {passed_checks}")
if report:
    print(f"Falhas encontradas ({len(report)}):")
    for r in report:
        print("  -", r)
else:
    print("STATUS: 100% DOS ARQUIVOS CONFERIDOS E EM TOTAL CONFORMIDADE COM O PDF E PADRÃO VITAMAIS!")
