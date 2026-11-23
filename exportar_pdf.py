#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exportador de PDF Fiel de Alta Definição — Catálogo Assifarma 2026
=================================================================
Gera o PDF oficial A4 (210×297mm) com fidelidade gráfica idêntica ao VitaMaiz.

Como usar:
    python3 exportar_pdf.py
"""

import os
import shutil
import subprocess
import sys
import io
from pathlib import Path
from PIL import Image
import fitz

WORKSPACE_DIR = Path("/Users/joel/Documents/CATÁLOGO PDF/ASSIFARMA - CATÁLOGO")
HTML_FILE = WORKSPACE_DIR / "catalogo_completo.html"
OUTPUT_PDF = WORKSPACE_DIR / "Catalogo_Assifarma_2026.pdf"
DOWNLOADS_PDF = Path.home() / "Downloads" / "Catalogo_Assifarma_2026.pdf"
PREVIEW_DIR = WORKSPACE_DIR / "preview_pages"
PREVIEW_DIR.mkdir(exist_ok=True)

CHROME_CANDIDATES = [
    "/Applications/Google Chrome 1/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
]
CHROME_BIN = next((c for c in CHROME_CANDIDATES if c and Path(c).exists()), None)


def export_pdf():
    print("=" * 64)
    print("🚀 INICIANDO EXPORTAÇÃO DO CATÁLOGO ASSIFARMA 2026 EM PDF A4")
    print("=" * 64)

    if not CHROME_BIN:
        print("❌ Erro: Google Chrome não foi encontrado no sistema.")
        sys.exit(1)

    if not HTML_FILE.exists():
        print(f"❌ Erro: Arquivo {HTML_FILE} não encontrado. Execute gerar_catalogo.py primeiro.")
        sys.exit(1)

    print(f"1. Renderizando via Headless Chrome: {CHROME_BIN}")
    cmd = [
        CHROME_BIN,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={OUTPUT_PDF}",
        str(HTML_FILE),
    ]

    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0 or not OUTPUT_PDF.exists():
        print(f"❌ Erro ao gerar PDF: {res.stderr}")
        sys.exit(1)

    raw_mb = OUTPUT_PDF.stat().st_size / (1024 * 1024)
    print(f"   [OK] PDF bruto gerado: {raw_mb:.2f} MB")

    # 2. Otimizar PDF com PyMuPDF para equilibrar nitidez e peso
    print("\n2. Otimizando streams do PDF mantendo fidelidade visual...")
    doc = fitz.open(OUTPUT_PDF)
    print(f"   Total de páginas no PDF: {len(doc)}")

    processed_xrefs = set()
    for page_idx in range(len(doc)):
        page = doc[page_idx]
        for img_info in page.get_images(full=True):
            xref = img_info[0]
            if xref in processed_xrefs:
                continue
            processed_xrefs.add(xref)
            try:
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                im = Image.open(io.BytesIO(image_bytes))
                max_dim = max(im.width, im.height)
                limit = 1600
                if max_dim > limit:
                    scale = limit / max_dim
                    new_size = (int(im.width * scale), int(im.height * scale))
                    im = im.resize(new_size, Image.Resampling.LANCZOS)
                    buf = io.BytesIO()
                    im.save(buf, format="PNG", optimize=True)
                    new_bytes = buf.getvalue()
                    if len(new_bytes) < len(image_bytes):
                        doc.update_stream(xref, new_bytes)
            except Exception:
                pass

    temp_opt_pdf = WORKSPACE_DIR / "_temp_opt.pdf"
    doc.save(temp_opt_pdf, deflate=True, garbage=4)
    doc.close()
    shutil.move(temp_opt_pdf, OUTPUT_PDF)
    final_mb = OUTPUT_PDF.stat().st_size / (1024 * 1024)
    print(f"   [OK] PDF Otimizado: {final_mb:.2f} MB")

    # Copiar para Downloads
    try:
        shutil.copy2(OUTPUT_PDF, DOWNLOADS_PDF)
        print(f"   [OK] Cópia salva em Downloads: {DOWNLOADS_PDF}")
    except Exception as e:
        print(f"   [AVISO] Não foi possível copiar para Downloads: {e}")

    # 3. Renderizar previews em PNG das primeiras páginas
    print("\n3. Gerando previews visuais em PNG de alta definição...")
    doc = fitz.open(OUTPUT_PDF)
    num_previews = min(6, len(doc))
    for i in range(num_previews):
        page = doc[i]
        pix = page.get_pixmap(dpi=150)
        out_img = PREVIEW_DIR / f"catalogo_pagina_{i+1:02d}.png"
        pix.save(out_img)
        print(f"   [Preview] Página {i+1:02d} -> {out_img.name} ({pix.width}x{pix.height})")

    print("\n" + "=" * 64)
    print(f"✨ EXPORTAÇÃO CONCLUÍDA: {len(doc)} PÁGINAS A4")
    print(f"📁 PDF Oficial: {OUTPUT_PDF}")
    print("=" * 64)


if __name__ == "__main__":
    export_pdf()
