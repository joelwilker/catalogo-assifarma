#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MD_DIR = BASE_DIR / "md_embalagens"
MD_DIR.mkdir(parents=True, exist_ok=True)

from build_all_mds import render_md
from data_pages_1_to_19 import PAGES_1_TO_19
from data_pages_20_to_38 import PAGES_20_TO_38

ALL_PAGES = PAGES_1_TO_19 + PAGES_20_TO_38
print(f"Total de páginas a gerar: {len(ALL_PAGES)}")

generated_files = []
for pdata in ALL_PAGES:
    fname = pdata["filename"]
    fpath = MD_DIR / fname
    content = render_md(pdata)
    fpath.write_text(content, encoding="utf-8")
    generated_files.append((pdata["pagina_pdf"], fname, len(content)))
    print(f"Página {pdata['pagina_pdf']:02d} gerada com sucesso -> {fname} ({len(content)} caracteres)")

print(f"\nSucesso total: {len(generated_files)} arquivos MD gerados na pasta '{MD_DIR}'.")
