#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Apresentação PowerPoint 16:9 (PPTX) — Catálogo Assifarma 2026
=========================================================================
Projeto independente de apresentação comercial widescreen 16:9 (13.333" x 7.5").
- Layout executivo em 3 zonas consistentes (Vitrine Visual | Informações | Tabela ANVISA)
- Tabela Nutricional 100% no padrão obrigatório ANVISA (RDC 429/2020 / IN 75/2020)
- Zero sombras, imagens otimizadas e textos/tabelas nativos editáveis.
"""

import io
import re
import shutil
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.xmlchemy import OxmlElement

WS = Path("/Users/joel/Documents/CATÁLOGO PDF/ASSIFARMA - CATÁLOGO")
HTML_FILE = WS / "catalogo_completo.html"
OPT_DIR = WS / "imagens_otimizadas"
OUT_PPTX = WS / "Catalogo_Assifarma_2026_16x9.pptx"
DL_PPTX = Path.home() / "Downloads" / "Catalogo_Assifarma_2026_16x9.pptx"

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
FONT_NAME = "Arial"
NS_A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def hex_to_rgb(hex_str: str, fallback=(30, 58, 138)) -> RGBColor:
    if not hex_str:
        return RGBColor(*fallback)
    h = hex_str.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        return RGBColor(*fallback)
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def parse_theme_vars(style_attr: str) -> dict:
    vars_found = {}
    for key in ("--theme-color", "--theme-dark", "--theme-light"):
        m = re.search(rf"{re.escape(key)}\s*:\s*(#[0-9a-fA-F]{{3,6}})", style_attr or "")
        if m:
            vars_found[key] = m.group(1)
    return {
        "color": hex_to_rgb(vars_found.get("--theme-color", "#1e3a8a")),
        "dark": hex_to_rgb(vars_found.get("--theme-dark", "#0f172a")),
        "light": hex_to_rgb(vars_found.get("--theme-light", "#eef2ff")),
    }


def set_cell_edges(cell, left=None, right=None, top=None, bottom=None):
    """Set individual cell borders as (width_pt, hex_color) or None for no border."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    edge_map = {"lnL": left, "lnR": right, "lnT": top, "lnB": bottom}
    for edge_name, spec in edge_map.items():
        for old in tcPr.findall(f"{NS_A}{edge_name}"):
            tcPr.remove(old)
        ln = OxmlElement(f"a:{edge_name}")
        if spec is None:
            noFill = OxmlElement("a:noFill")
            ln.append(noFill)
        else:
            width_pt, color_hex = spec
            ln.set("w", str(int(width_pt * 12700)))
            ln.set("cap", "flat")
            ln.set("cmpd", "sng")
            ln.set("algn", "ctr")
            solidFill = OxmlElement("a:solidFill")
            srgbClr = OxmlElement("a:srgbClr")
            srgbClr.set("val", color_hex)
            solidFill.append(srgbClr)
            ln.append(solidFill)
        tcPr.append(ln)


def set_cell_margins(cell, left=0.06, right=0.06, top=0.015, bottom=0.015):
    cell.margin_left = Inches(left)
    cell.margin_right = Inches(right)
    cell.margin_top = Inches(top)
    cell.margin_bottom = Inches(bottom)


def add_rounded_rect(slide, x, y, w, h, fill_rgb=None, line_rgb=None, line_pt=0.75, radius=0.05):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    if shp.adjustments:
        shp.adjustments[0] = radius
    if fill_rgb is not None:
        shp.fill.solid()
        shp.fill.fore_color.rgb = fill_rgb
    else:
        shp.fill.background()
    if line_rgb is not None:
        shp.line.color.rgb = line_rgb
        shp.line.width = Pt(line_pt)
    else:
        shp.line.fill.background()
    return shp


def add_rect(slide, x, y, w, h, fill_rgb=None, line_rgb=None, line_pt=0.75):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill_rgb is not None:
        shp.fill.solid()
        shp.fill.fore_color.rgb = fill_rgb
    else:
        shp.fill.background()
    if line_rgb is not None:
        shp.line.color.rgb = line_rgb
        shp.line.width = Pt(line_pt)
    else:
        shp.line.fill.background()
    return shp


def add_textbox(slide, x, y, w, h, text="", font_size=10, bold=False, color=RGBColor(15, 23, 42),
                align=PP_ALIGN.LEFT, valign=MSO_ANCHOR.TOP, margin=(0.04, 0.04, 0.02, 0.02)):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = valign
    tf.margin_left = Inches(margin[0])
    tf.margin_right = Inches(margin[1])
    tf.margin_top = Inches(margin[2])
    tf.margin_bottom = Inches(margin[3])
    if text:
        p = tf.paragraphs[0]
        p.alignment = align
        r = p.add_run()
        r.text = text
        r.font.name = FONT_NAME
        r.font.size = Pt(font_size)
        r.font.bold = bold
        r.font.color.rgb = color
    return tb


def add_picture_contained(slide, img_path: Path, x, y, max_w, max_h):
    if not img_path or not img_path.exists():
        return None
    with Image.open(img_path) as im:
        iw, ih = im.size
    box_ratio = max_w / max_h
    img_ratio = iw / max(1, ih)
    if img_ratio >= box_ratio:
        w = max_w
        h = w / img_ratio
    else:
        h = max_h
        w = h * img_ratio
    px = x + (max_w - w) / 2.0
    py = y + (max_h - h) / 2.0
    return slide.shapes.add_picture(str(img_path), Inches(px), Inches(py), width=Inches(w), height=Inches(h))


def add_picture_cover_cropped(slide, img_path: Path, x, y, target_w, target_h):
    if not img_path or not img_path.exists():
        return None
    with Image.open(img_path) as im:
        im = im.convert("RGB")
        iw, ih = im.size
        target_ratio = target_w / target_h
        img_ratio = iw / max(1, ih)
        if img_ratio > target_ratio:
            new_w = int(ih * target_ratio)
            left = (iw - new_w) // 2
            im = im.crop((left, 0, left + new_w, ih))
        else:
            new_h = int(iw / target_ratio)
            top = (ih - new_h) // 2
            im = im.crop((0, top, iw, top + new_h))
        if im.width > 1400:
            im = im.resize((1400, int(1400 / target_ratio)), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=84, optimize=True)
        buf.seek(0)
    return slide.shapes.add_picture(buf, Inches(x), Inches(y), width=Inches(target_w), height=Inches(target_h))


def build_cover_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg_path = WS / "Design padrão/extracted_assets/capa_azul.png"
    if bg_path.exists():
        add_picture_cover_cropped(slide, bg_path, 0, 0, 13.333, 7.5)

    overlay = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    overlay.fill.solid()
    overlay.fill.fore_color.rgb = RGBColor(10, 22, 48)
    srgb = overlay.fill._xPr.solidFill.srgbClr
    alpha = OxmlElement("a:alpha")
    alpha.set("val", "55000")
    srgb.append(alpha)
    overlay.line.fill.background()

    pill = add_rounded_rect(slide, 0.9, 1.35, 3.3, 0.42, fill_rgb=RGBColor(30, 64, 175), radius=0.4)
    tf = pill.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "INTERCRON  •  FORHEALTH"
    r.font.name = FONT_NAME
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

    logo_w = OPT_DIR / "logo_forhealth_white.png"
    if logo_w.exists():
        add_picture_contained(slide, logo_w, 0.9, 2.05, 4.8, 1.45)

    add_rect(slide, 0.9, 3.75, 4.2, 0.05, fill_rgb=RGBColor(56, 189, 248))
    add_textbox(slide, 0.9, 4.05, 10.5, 0.75, "Apresentação de Produtos 2026",
                font_size=36, bold=True, color=RGBColor(255, 255, 255), margin=(0, 0, 0, 0))
    add_textbox(slide, 0.9, 4.85, 10.5, 0.45, "Linhas Exclusivas de Suplementos Alimentares • Portfólio Comercial",
                font_size=15, bold=False, color=RGBColor(203, 213, 225), margin=(0, 0, 0, 0))

    lines_bar = add_rounded_rect(slide, 0.9, 6.15, 11.533, 0.55, fill_rgb=RGBColor(15, 32, 68),
                                 line_rgb=RGBColor(56, 189, 248), line_pt=0.75, radius=0.15)
    tf2 = lines_bar.text_frame
    tf2.vertical_anchor = MSO_ANCHOR.MIDDLE
    p2 = tf2.paragraphs[0]
    p2.alignment = PP_ALIGN.CENTER
    r2 = p2.add_run()
    r2.text = "BORG   •   CRONOVIT   •   CRONOLIV   •   CARTI MASTER   •   NUTRIVIX   •   PORTFÓLIO COMPLEMENTAR"
    r2.font.name = FONT_NAME
    r2.font.size = Pt(11.5)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(226, 232, 240)


def build_toc_slide(prs, soup, total_slides):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(slide, 0, 0, 13.333, 7.5, fill_rgb=RGBColor(248, 250, 252))

    add_textbox(slide, 0.5, 0.28, 7.5, 0.55, "Índice de Produtos",
                font_size=26, bold=True, color=RGBColor(15, 23, 42), margin=(0, 0, 0, 0))
    add_textbox(slide, 0.5, 0.80, 7.5, 0.30, "Portfólio Organizado por Linha de Produto • Apresentação 16:9",
                font_size=10.5, color=RGBColor(100, 116, 139), margin=(0, 0, 0, 0))

    logo_d = OPT_DIR / "logo_forhealth_dark.png"
    if logo_d.exists():
        add_picture_contained(slide, logo_d, 10.35, 0.25, 2.5, 0.78)

    add_rect(slide, 0.5, 1.18, 4.1, 0.04, fill_rgb=RGBColor(30, 58, 138))
    add_rect(slide, 4.6, 1.18, 4.1, 0.04, fill_rgb=RGBColor(16, 185, 129))
    add_rect(slide, 8.7, 1.18, 4.133, 0.04, fill_rgb=RGBColor(217, 119, 6))

    toc_sec = soup.find("section", id="pagina-2")
    cards = toc_sec.find_all("div", class_="toc-category-card")

    pill_colors = [
        RGBColor(15, 23, 42),     # Borg
        RGBColor(194, 65, 12),    # Cronovit
        RGBColor(180, 83, 9),     # Cronoliv
        RGBColor(21, 128, 61),    # Carti Master
        RGBColor(29, 78, 216),    # Nutrivix
        RGBColor(71, 85, 105),    # Outros
    ]

    parsed_cards = []
    for idx, c in enumerate(cards):
        cat_name = c.find(class_="toc-cat-pill").get_text(strip=True)
        cat_count = c.find(class_="toc-cat-count").get_text(strip=True)
        items = []
        for li in c.find_all("li", class_="toc-clean-item"):
            name = li.find(class_="toc-clean-name").get_text(strip=True)
            pag = li.find(class_="toc-clean-page").get_text(strip=True).replace("Pág.", "Slide")
            items.append((name, pag))
        parsed_cards.append((cat_name, cat_count, items, pill_colors[idx % len(pill_colors)]))

    columns = [[], [], []]
    col_loads = [0, 0, 0]
    for card in parsed_cards:
        w_card = 2.2 + len(card[2])
        target_col = min(range(3), key=lambda k: col_loads[k])
        columns[target_col].append(card)
        col_loads[target_col] += w_card

    col_w = 3.96
    gap_x = 0.22
    start_x = 0.50
    for col_idx, col_cards in enumerate(columns):
        x = start_x + col_idx * (col_w + gap_x)
        total_h = 5.72
        gap_y = 0.14
        avail_h = total_h - gap_y * max(0, len(col_cards) - 1)
        total_units = sum(2.0 + len(c[2]) for c in col_cards)
        cur_y = 1.35

        for cat_name, cat_count, items, pcolor in col_cards:
            ch = avail_h * ((2.0 + len(items)) / max(1, total_units))
            add_rounded_rect(slide, x, cur_y, col_w, ch, fill_rgb=RGBColor(255, 255, 255),
                             line_rgb=RGBColor(226, 232, 240), line_pt=0.75, radius=0.04)
            pill = add_rounded_rect(slide, x + 0.14, cur_y + 0.10, 1.85, 0.28, fill_rgb=pcolor, radius=0.35)
            ptf = pill.text_frame
            ptf.vertical_anchor = MSO_ANCHOR.MIDDLE
            pp = ptf.paragraphs[0]
            pp.alignment = PP_ALIGN.CENTER
            pr = pp.add_run()
            pr.text = cat_name.upper()
            pr.font.name = FONT_NAME
            pr.font.size = Pt(8)
            pr.font.bold = True
            pr.font.color.rgb = RGBColor(255, 255, 255)

            add_textbox(slide, x + 2.05, cur_y + 0.12, col_w - 2.18, 0.25, cat_count,
                        font_size=8, bold=True, color=RGBColor(100, 116, 139), align=PP_ALIGN.RIGHT, margin=(0, 0, 0, 0))

            tb = slide.shapes.add_textbox(Inches(x + 0.14), Inches(cur_y + 0.44), Inches(col_w - 0.28), Inches(ch - 0.50))
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
            f_sz = 8.5 if len(items) <= 9 else 8.0
            for i_idx, (name, pag) in enumerate(items):
                p = tf.paragraphs[0] if i_idx == 0 else tf.add_paragraph()
                p.space_after = Pt(2.5 if len(items) <= 8 else 1.5)
                r1 = p.add_run()
                r1.text = f"• {name}  "
                r1.font.name = FONT_NAME
                r1.font.size = Pt(f_sz)
                r1.font.color.rgb = RGBColor(30, 41, 59)
                r2 = p.add_run()
                r2.text = f"({pag})"
                r2.font.name = FONT_NAME
                r2.font.size = Pt(f_sz - 0.5)
                r2.font.bold = True
                r2.font.color.rgb = pcolor

            cur_y += ch + gap_y

    add_textbox(slide, 0.5, 7.15, 7.0, 0.25, "APRESENTAÇÃO DE PRODUTOS 2026  •  INTERCRON / FORHEALTH",
                font_size=8, bold=True, color=RGBColor(100, 116, 139), margin=(0, 0, 0, 0))
    add_textbox(slide, 11.3, 7.15, 1.5, 0.25, f"Slide 2 / {total_slides}",
                font_size=8, bold=True, color=RGBColor(71, 85, 105), align=PP_ALIGN.RIGHT, margin=(0, 0, 0, 0))


def build_anvisa_table(slide, x, y, w, max_h, serving_lines, table_rows, insig_text, foot_text):
    """
    Constrói a Tabela Nutricional 100% no padrão obrigatório ANVISA (RDC 429/2020 / IN 75/2020)
    em uma única tabela nativa do PowerPoint (borda externa preta 1.5pt, barras grossas pretas,
    apenas linhas horizontais pretas entre nutrientes, fundo branco e texto preto).
    """
    n_nut = len(table_rows)  # includes header row ["", "", "%VD*"]
    has_insig = bool(insig_text)
    has_foot = bool(foot_text)
    extra_footer_rows = 1 if (has_insig or has_foot) else 0
    total_rows = 2 + n_nut + extra_footer_rows  # Title + Serving + Table + Footnote

    # Dynamic sizing so even 31-row tables fit cleanly inside max_h
    if n_nut >= 25:
        title_h, srv_h, foot_h = 0.24, 0.34, 0.42
        fs_title, fs_srv, fs_tbl, fs_foot = 8.5, 6.8, 6.2, 5.8
        v_pad = 0.005
    elif n_nut >= 16:
        title_h, srv_h, foot_h = 0.26, 0.36, 0.46
        fs_title, fs_srv, fs_tbl, fs_foot = 9.0, 7.2, 6.8, 6.2
        v_pad = 0.008
    elif n_nut >= 10:
        title_h, srv_h, foot_h = 0.28, 0.40, 0.52
        fs_title, fs_srv, fs_tbl, fs_foot = 9.5, 7.5, 7.6, 6.5
        v_pad = 0.012
    else:
        title_h, srv_h, foot_h = 0.30, 0.42, 0.55
        fs_title, fs_srv, fs_tbl, fs_foot = 9.5, 7.8, 8.2, 6.8
        v_pad = 0.018

    avail_nut_h = max(0.8, max_h - title_h - srv_h - (foot_h if extra_footer_rows else 0))
    row_h = min(0.26, avail_nut_h / max(1, n_nut))
    actual_h = title_h + srv_h + row_h * n_nut + (foot_h if extra_footer_rows else 0)

    n_cols = 3
    shape_tbl = slide.shapes.add_table(total_rows, n_cols, Inches(x), Inches(y), Inches(w), Inches(actual_h))
    tbl = shape_tbl.table
    tbl.columns[0].width = Inches(w * 0.57)
    tbl.columns[1].width = Inches(w * 0.25)
    tbl.columns[2].width = Inches(w * 0.18)

    BLACK = "000000"
    WHITE = RGBColor(255, 255, 255)
    BLACK_RGB = RGBColor(0, 0, 0)

    # --- ROW 0: INFORMAÇÃO NUTRICIONAL ---
    tbl.rows[0].height = Inches(title_h)
    tbl.cell(0, 0).merge(tbl.cell(0, 2))
    c0 = tbl.cell(0, 0)
    c0.fill.solid()
    c0.fill.fore_color.rgb = WHITE
    c0.vertical_anchor = MSO_ANCHOR.MIDDLE
    set_cell_margins(c0, left=0.07, right=0.07, top=0.01, bottom=0.01)
    set_cell_edges(c0, left=(1.5, BLACK), right=(1.5, BLACK), top=(1.5, BLACK), bottom=(0.75, BLACK))
    p0 = c0.text_frame.paragraphs[0]
    p0.alignment = PP_ALIGN.CENTER
    r0 = p0.add_run()
    r0.text = "INFORMAÇÃO NUTRICIONAL"
    r0.font.name = FONT_NAME
    r0.font.size = Pt(fs_title)
    r0.font.bold = True
    r0.font.color.rgb = BLACK_RGB

    # --- ROW 1: Porções por embalagem / Porção ---
    tbl.rows[1].height = Inches(srv_h)
    tbl.cell(1, 0).merge(tbl.cell(1, 2))
    c1 = tbl.cell(1, 0)
    c1.fill.solid()
    c1.fill.fore_color.rgb = WHITE
    c1.vertical_anchor = MSO_ANCHOR.MIDDLE
    set_cell_margins(c1, left=0.07, right=0.07, top=0.015, bottom=0.015)
    set_cell_edges(c1, left=(1.5, BLACK), right=(1.5, BLACK), top=(0.75, BLACK), bottom=(1.75, BLACK))
    tf1 = c1.text_frame
    tf1.word_wrap = True
    for si, sline in enumerate(serving_lines if serving_lines else [""]):
        ps = tf1.paragraphs[0] if si == 0 else tf1.add_paragraph()
        ps.alignment = PP_ALIGN.LEFT
        rs = ps.add_run()
        rs.text = sline
        rs.font.name = FONT_NAME
        rs.font.size = Pt(fs_srv)
        rs.font.bold = False
        rs.font.color.rgb = BLACK_RGB

    # --- ROWS 2 .. 2+n_nut-1: Nutrient Header & Rows ---
    for idx, rdata in enumerate(table_rows):
        ri = 2 + idx
        tbl.rows[ri].height = Inches(row_h)
        is_hdr = (idx == 0)
        is_last_nut = (idx == n_nut - 1)
        top_edge = (1.75, BLACK) if is_hdr else (0.5, BLACK)
        bot_edge = (1.5, BLACK) if (is_hdr or is_last_nut) else (0.5, BLACK)

        for ci in range(n_cols):
            cell = tbl.cell(ri, ci)
            cell.fill.solid()
            cell.fill.fore_color.rgb = WHITE
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            set_cell_margins(cell, left=0.06, right=0.06, top=v_pad, bottom=v_pad)
            left_e = (1.5, BLACK) if ci == 0 else None
            right_e = (1.5, BLACK) if ci == 2 else None
            set_cell_edges(cell, left=left_e, right=right_e, top=top_edge, bottom=bot_edge)

            val_str = rdata[ci] if ci < len(rdata) else ""
            cp = cell.text_frame.paragraphs[0]
            cp.alignment = PP_ALIGN.LEFT if ci == 0 else (PP_ALIGN.RIGHT if ci == 1 else PP_ALIGN.CENTER)
            cr = cp.add_run()
            cr.text = val_str
            cr.font.name = FONT_NAME
            cr.font.size = Pt(fs_tbl)
            cr.font.bold = is_hdr
            cr.font.color.rgb = BLACK_RGB

    # --- FINAL ROW: Não contém quantidades significativas + * Percentual ---
    if extra_footer_rows:
        fi = 2 + n_nut
        tbl.rows[fi].height = Inches(foot_h)
        tbl.cell(fi, 0).merge(tbl.cell(fi, 2))
        cf = tbl.cell(fi, 0)
        cf.fill.solid()
        cf.fill.fore_color.rgb = WHITE
        cf.vertical_anchor = MSO_ANCHOR.MIDDLE
        set_cell_margins(cf, left=0.07, right=0.07, top=0.02, bottom=0.02)
        set_cell_edges(cf, left=(1.5, BLACK), right=(1.5, BLACK), top=(1.5, BLACK), bottom=(1.5, BLACK))
        tff = cf.text_frame
        tff.word_wrap = True
        first_p = True
        if has_insig:
            p_ins = tff.paragraphs[0]
            first_p = False
            p_ins.alignment = PP_ALIGN.LEFT
            p_ins.space_after = Pt(1.5)
            r_ins = p_ins.add_run()
            r_ins.text = insig_text
            r_ins.font.name = FONT_NAME
            r_ins.font.size = Pt(fs_foot)
            r_ins.font.color.rgb = BLACK_RGB
        if has_foot:
            p_ft = tff.paragraphs[0] if first_p else tff.add_paragraph()
            p_ft.alignment = PP_ALIGN.LEFT
            r_ft = p_ft.add_run()
            r_ft.text = foot_text
            r_ft.font.name = FONT_NAME
            r_ft.font.size = Pt(fs_foot)
            r_ft.font.color.rgb = BLACK_RGB

    return actual_h


def build_product_slide(prs, art, slide_num, total_slides):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    theme = parse_theme_vars(art.get("style", ""))
    t_col = theme["color"]
    t_dark = theme["dark"]
    t_light = theme["light"]

    # Clean light background
    add_rect(slide, 0, 0, 13.333, 7.5, fill_rgb=RGBColor(248, 250, 252))

    # --- Parse HTML data ---
    title_el = art.find("h1", class_="title-product-unified")
    title = title_el.get_text(" ", strip=True) if title_el else ""
    cat_el = art.find(class_="hero-category-glass")
    cat = cat_el.get_text(" ", strip=True) if cat_el else ""
    denom_el = art.find(class_="md-denominacao-venda")
    denom = denom_el.get_text(" ", strip=True) if denom_el else ""

    specs = []
    for box in art.find_all("div", class_="key-spec-box"):
        lbl = box.find(class_="key-spec-label")
        val = box.find(class_="key-spec-value")
        specs.append((lbl.get_text(" ", strip=True) if lbl else "", val.get_text(" ", strip=True) if val else ""))

    pack_img_el = art.find("img", class_="packshot")
    pack_src = Path(pack_img_el["src"]) if pack_img_el and pack_img_el.get("src") else None

    highlights = [el.get_text(" ", strip=True) for el in art.find_all(class_="hl-main")]
    actives = [el.get_text(" ", strip=True) for el in art.find_all(class_="active-badge-pill")]
    benefits = [li.get_text(" ", strip=True) for li in art.select(".md-benefits-list li")]

    ing_text, allergens_text, cons_text = "", "", ""
    for card in art.find_all("div", class_="glass-info-card"):
        h3 = card.find("h3", class_="card-heading")
        if h3 and "Ingrediente" in h3.get_text():
            p_el = card.find("p", class_="ingredients-copy")
            if p_el:
                al_el = p_el.find("span", class_="allergens-inline")
                if al_el:
                    allergens_text = al_el.get_text(" ", strip=True)
                    al_el.extract()
                ing_text = p_el.get_text(" ", strip=True)
        elif h3 and "conserva" in h3.get_text().lower():
            p_el = card.find("p", class_="ingredients-copy")
            cons_text = p_el.get_text(" ", strip=True) if p_el else ""

    warn_el = art.find("p", class_="warnings-caps")
    warn_text = warn_el.get_text(" ", strip=True) if warn_el else ""

    banner_el = art.find("img", class_="banner-photo")
    banner_src = Path(banner_el["src"]) if banner_el and banner_el.get("src") else None
    if banner_src and not banner_src.is_absolute():
        banner_src = WS / banner_src

    anvisa_box = art.find("div", class_="anvisa-box")
    serving_lines, table_rows, insig_text, foot_text = [], [], "", ""
    if anvisa_box:
        srv = anvisa_box.find("div", class_="anvisa-serving-block")
        if srv:
            serving_lines = [s.strip() for s in srv.stripped_strings]
        tbl = anvisa_box.find("table", class_="anvisa-table")
        if tbl:
            for tr in tbl.find_all("tr"):
                cells = [c.get_text(" ", strip=True) for c in tr.find_all(["th", "td"])]
                if any(cells):
                    table_rows.append(cells)
        insig = anvisa_box.find("div", class_="anvisa-insignificant")
        if insig:
            insig_text = insig.get_text(" ", strip=True)
        foot = anvisa_box.find("div", class_="anvisa-footnote")
        if foot:
            foot_text = foot.get_text(" ", strip=True)

    n_rows = len(table_rows)
    ultra_dense_table = (n_rows >= 22)

    # --- 1. TOP HEADER BAR (y=0.18", h=0.78") ---
    add_rounded_rect(slide, 0.35, 0.18, 12.633, 0.78, fill_rgb=t_dark, radius=0.08)
    title_size = 20 if len(title) <= 34 else (17.5 if len(title) <= 46 else 15.5)
    add_textbox(slide, 0.55, 0.22, 9.9, 0.40, title, font_size=title_size, bold=True,
                color=RGBColor(255, 255, 255), valign=MSO_ANCHOR.MIDDLE, margin=(0, 0, 0, 0))
    add_textbox(slide, 0.55, 0.62, 9.9, 0.26, denom, font_size=8.5, bold=False,
                color=RGBColor(226, 232, 240), valign=MSO_ANCHOR.MIDDLE, margin=(0, 0, 0, 0))

    if cat:
        cpill = add_rounded_rect(slide, 10.65, 0.34, 2.10, 0.44, fill_rgb=t_col,
                                 line_rgb=RGBColor(255, 255, 255), line_pt=0.75, radius=0.4)
        ctf = cpill.text_frame
        ctf.vertical_anchor = MSO_ANCHOR.MIDDLE
        cp = ctf.paragraphs[0]
        cp.alignment = PP_ALIGN.CENTER
        cr = cp.add_run()
        cr.text = cat
        cr.font.name = FONT_NAME
        cr.font.size = Pt(9.5)
        cr.font.bold = True
        cr.font.color.rgb = RGBColor(255, 255, 255)

    add_rect(slide, 0.35, 1.00, 12.633, 0.03, fill_rgb=t_col)

    # --- 2. SPEC STRIP ---
    # On ultra_dense_table (rows >= 22), Spec Strip spans Zone A+B (w=8.45") so Zone C gets full height!
    spec_total_w = 8.45 if ultra_dense_table else 12.633
    spec_w = (spec_total_w - 0.24) / max(1, len(specs))
    for i, (lbl, val) in enumerate(specs[:3]):
        sx = 0.35 + i * (spec_w + 0.12)
        add_rounded_rect(slide, sx, 1.10, spec_w, 0.42, fill_rgb=RGBColor(255, 255, 255),
                         line_rgb=RGBColor(203, 213, 225), line_pt=0.75, radius=0.10)
        tb = slide.shapes.add_textbox(Inches(sx + 0.10), Inches(1.11), Inches(spec_w - 0.20), Inches(0.40))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        r1 = p.add_run()
        r1.text = f"{lbl} "
        r1.font.name = FONT_NAME
        r1.font.size = Pt(7.5 if ultra_dense_table else 8.0)
        r1.font.bold = True
        r1.font.color.rgb = t_col
        r2 = p.add_run()
        r2.text = val
        r2.font.name = FONT_NAME
        r2.font.size = Pt(7.5 if (ultra_dense_table or len(val) > 34) else 8.5)
        r2.font.bold = True
        r2.font.color.rgb = RGBColor(15, 23, 42)

    # --- 3. THREE CONSISTENT WIDESCREEN ZONES (y=1.60" to y=6.94", H=5.34") ---
    body_top = 1.60
    body_bot = 6.94

    # === ZONE A: LEFT VISUAL SHOWCASE (x=0.35", w=3.70") ===
    c1_x, c1_w = 0.35, 3.70
    place_banner_left = (banner_src is not None and 11 <= n_rows < 22)

    if place_banner_left:
        stage_h = 2.75
    elif len(actives) >= 3:
        stage_h = 2.85
    elif len(actives) >= 1:
        stage_h = 3.25
    else:
        stage_h = 3.90

    add_rounded_rect(slide, c1_x, body_top, c1_w, stage_h, fill_rgb=t_light,
                     line_rgb=RGBColor(203, 213, 225), line_pt=0.75, radius=0.05)
    if pack_src:
        add_picture_contained(slide, pack_src, c1_x + 0.14, body_top + 0.12, c1_w - 0.28, stage_h - 0.24)

    # Highlight pills directly under packshot
    hl_y = body_top + stage_h + 0.08
    if highlights:
        hw = (c1_w - 0.12) / max(1, len(highlights))
        for i, hl in enumerate(highlights[:3]):
            hx = c1_x + i * (hw + 0.06)
            hp = add_rounded_rect(slide, hx, hl_y, hw, 0.34, fill_rgb=t_col, radius=0.18)
            htf = hp.text_frame
            htf.vertical_anchor = MSO_ANCHOR.MIDDLE
            htf.margin_left = htf.margin_right = Inches(0.02)
            hpp = htf.paragraphs[0]
            hpp.alignment = PP_ALIGN.CENTER
            hr = hpp.add_run()
            hr.text = hl
            hr.font.name = FONT_NAME
            hr.font.size = Pt(7.5 if len(hl) < 18 else 6.8)
            hr.font.bold = True
            hr.font.color.rgb = RGBColor(255, 255, 255)

    left_rem_y = hl_y + 0.42
    left_rem_h = body_bot - left_rem_y

    if place_banner_left:
        # Active badges compact if any, else banner takes remaining space
        if actives:
            act_h = 0.30
            for i, act in enumerate(actives[:2]):
                ay = left_rem_y + i * (act_h + 0.05)
                ap = add_rounded_rect(slide, c1_x, ay, c1_w, act_h, fill_rgb=t_dark, radius=0.14)
                atf = ap.text_frame
                atf.vertical_anchor = MSO_ANCHOR.MIDDLE
                app = atf.paragraphs[0]
                app.alignment = PP_ALIGN.CENTER
                ar = app.add_run()
                ar.text = act
                ar.font.name = FONT_NAME
                ar.font.size = Pt(7.4)
                ar.font.bold = True
                ar.font.color.rgb = RGBColor(255, 255, 255)
            ban_y = left_rem_y + len(actives[:2]) * (act_h + 0.05) + 0.04
        else:
            ban_y = left_rem_y
        ban_h = body_bot - ban_y
        if ban_h >= 0.85:
            add_rounded_rect(slide, c1_x, ban_y, c1_w, ban_h, fill_rgb=RGBColor(255, 255, 255),
                             line_rgb=RGBColor(203, 213, 225), line_pt=0.75, radius=0.05)
            add_picture_cover_cropped(slide, banner_src, c1_x + 0.05, ban_y + 0.05, c1_w - 0.10, ban_h - 0.10)
            banner_src = None
    elif actives:
        act_h = min(0.38, (left_rem_h - 0.06 * (len(actives) - 1)) / len(actives))
        for i, act in enumerate(actives):
            ay = left_rem_y + i * (act_h + 0.06)
            ap = add_rounded_rect(slide, c1_x, ay, c1_w, act_h, fill_rgb=t_dark, radius=0.14)
            atf = ap.text_frame
            atf.vertical_anchor = MSO_ANCHOR.MIDDLE
            app = atf.paragraphs[0]
            app.alignment = PP_ALIGN.CENTER
            ar = app.add_run()
            ar.text = act
            ar.font.name = FONT_NAME
            ar.font.size = Pt(7.8 if len(act) < 46 else 7.0)
            ar.font.bold = True
            ar.font.color.rgb = RGBColor(255, 255, 255)
    elif left_rem_h >= 0.70:
        # Subtle brand summary box when neither actives nor left-banner exist
        add_rounded_rect(slide, c1_x, left_rem_y, c1_w, left_rem_h, fill_rgb=RGBColor(255, 255, 255),
                         line_rgb=RGBColor(203, 213, 225), line_pt=0.75, radius=0.05)
        add_textbox(slide, c1_x + 0.14, left_rem_y + 0.10, c1_w - 0.28, 0.22,
                    "DIFERENCIAIS DA FORMULAÇÃO", font_size=7.8, bold=True, color=t_col, margin=(0, 0, 0, 0))
        add_textbox(slide, c1_x + 0.14, left_rem_y + 0.34, c1_w - 0.28, left_rem_h - 0.42,
                    "Qualidade farmacêutica Forhealth / Intercron com padrão de rotulagem atualizado e notificação regularizada.",
                    font_size=7.5, color=RGBColor(71, 85, 105), margin=(0, 0, 0, 0))

    # === ZONE B: MIDDLE PRODUCT INFORMATION (x=4.20", w=4.60") ===
    # Always contains: 1. Benefícios, 2. Ingredientes & Alérgicos, 3. Conservação, 4. Advertências
    c2_x, c2_w = 4.20, 4.60
    total_ing_len = len(ing_text) + len(allergens_text)

    # Smart vertical allocation in Zone B (total H = 5.34", 3 gaps of 0.09" = 0.27" -> 5.07" net)
    ben_h = 1.25 if len(benefits) <= 3 else (1.50 if len(benefits) <= 5 else 1.70)
    if total_ing_len > 620:
        ben_h = max(1.08, ben_h - 0.20)

    cons_h = 0.92 if len(cons_text) < 260 else 1.05
    warn_h = 0.88 if len(warn_text) < 260 else 1.02
    ing_h = (body_bot - body_top) - ben_h - cons_h - warn_h - 0.27

    # 1. Benefícios
    y1 = body_top
    add_rounded_rect(slide, c2_x, y1, c2_w, ben_h, fill_rgb=RGBColor(255, 255, 255),
                     line_rgb=RGBColor(203, 213, 225), line_pt=0.75, radius=0.04)
    add_textbox(slide, c2_x + 0.14, y1 + 0.06, c2_w - 0.28, 0.22, "INFORMAÇÕES E BENEFÍCIOS",
                font_size=8.2, bold=True, color=t_col, margin=(0, 0, 0, 0))
    btb = slide.shapes.add_textbox(Inches(c2_x + 0.14), Inches(y1 + 0.28), Inches(c2_w - 0.28), Inches(ben_h - 0.34))
    btf = btb.text_frame
    btf.word_wrap = True
    btf.margin_left = btf.margin_right = btf.margin_top = btf.margin_bottom = 0
    b_fs = 8.2 if len(benefits) <= 3 else (7.4 if len(benefits) <= 5 else 6.8)
    for bi, btxt in enumerate(benefits):
        bp = btf.paragraphs[0] if bi == 0 else btf.add_paragraph()
        bp.space_after = Pt(1.5)
        br = bp.add_run()
        br.text = f"• {btxt}"
        br.font.name = FONT_NAME
        br.font.size = Pt(b_fs)
        br.font.color.rgb = RGBColor(30, 41, 59)

    # 2. Ingredientes e Alérgicos
    y2 = y1 + ben_h + 0.09
    add_rounded_rect(slide, c2_x, y2, c2_w, ing_h, fill_rgb=RGBColor(255, 255, 255),
                     line_rgb=RGBColor(203, 213, 225), line_pt=0.75, radius=0.04)
    add_textbox(slide, c2_x + 0.14, y2 + 0.06, c2_w - 0.28, 0.22, "INGREDIENTES E ALÉRGICOS",
                font_size=8.2, bold=True, color=t_col, margin=(0, 0, 0, 0))
    itb = slide.shapes.add_textbox(Inches(c2_x + 0.14), Inches(y2 + 0.28), Inches(c2_w - 0.28), Inches(ing_h - 0.34))
    itf = itb.text_frame
    itf.word_wrap = True
    itf.margin_left = itf.margin_right = itf.margin_top = itf.margin_bottom = 0
    ing_fs = 8.2 if total_ing_len < 340 else (7.3 if total_ing_len < 580 else 6.5)
    ip = itf.paragraphs[0]
    ir1 = ip.add_run()
    ir1.text = ing_text + (" " if allergens_text else "")
    ir1.font.name = FONT_NAME
    ir1.font.size = Pt(ing_fs)
    ir1.font.color.rgb = RGBColor(51, 65, 85)
    if allergens_text:
        ir2 = ip.add_run()
        ir2.text = allergens_text
        ir2.font.name = FONT_NAME
        ir2.font.size = Pt(ing_fs)
        ir2.font.bold = True
        ir2.font.color.rgb = RGBColor(15, 23, 42)

    # 3. Cuidados de Conservação
    y3 = y2 + ing_h + 0.09
    add_rounded_rect(slide, c2_x, y3, c2_w, cons_h, fill_rgb=RGBColor(255, 255, 255),
                     line_rgb=RGBColor(203, 213, 225), line_pt=0.75, radius=0.04)
    add_textbox(slide, c2_x + 0.14, y3 + 0.05, c2_w - 0.28, 0.20, "CUIDADOS DE CONSERVAÇÃO",
                font_size=8.0, bold=True, color=t_col, margin=(0, 0, 0, 0))
    add_textbox(slide, c2_x + 0.14, y3 + 0.25, c2_w - 0.28, cons_h - 0.30, cons_text,
                font_size=7.1 if len(cons_text) < 270 else 6.5, color=RGBColor(51, 65, 85), margin=(0, 0, 0, 0))

    # 4. Advertências e Precauções
    y4 = y3 + cons_h + 0.09
    add_rounded_rect(slide, c2_x, y4, c2_w, warn_h, fill_rgb=RGBColor(255, 255, 255),
                     line_rgb=RGBColor(203, 213, 225), line_pt=0.75, radius=0.04)
    add_rect(slide, c2_x, y4 + 0.08, 0.06, warn_h - 0.16, fill_rgb=t_col)
    add_textbox(slide, c2_x + 0.14, y4 + 0.05, c2_w - 0.24, 0.20, "ADVERTÊNCIAS E PRECAUÇÕES",
                font_size=8.0, bold=True, color=t_col, margin=(0, 0, 0, 0))
    add_textbox(slide, c2_x + 0.14, y4 + 0.25, c2_w - 0.24, warn_h - 0.30, warn_text,
                font_size=6.8 if len(warn_text) < 270 else 6.2, bold=True, color=RGBColor(30, 41, 59), margin=(0, 0, 0, 0))

    # === ZONE C: RIGHT OFFICIAL ANVISA NUTRITION TABLE + BANNER ===
    c3_x, c3_w = 8.95, 4.033
    nut_y = 1.10 if ultra_dense_table else body_top
    has_right_banner = (banner_src is not None and n_rows <= 11)
    right_ban_reserve = 1.85 if has_right_banner else 0.0
    nut_max_h = (body_bot - nut_y) - right_ban_reserve

    actual_nut_h = build_anvisa_table(slide, c3_x, nut_y, c3_w, nut_max_h,
                                      serving_lines, table_rows, insig_text, foot_text)

    if has_right_banner and banner_src is not None:
        by = nut_y + actual_nut_h + 0.12
        bh = body_bot - by
        if bh >= 0.90:
            add_rounded_rect(slide, c3_x, by, c3_w, bh, fill_rgb=RGBColor(255, 255, 255),
                             line_rgb=RGBColor(203, 213, 225), line_pt=0.75, radius=0.05)
            add_picture_cover_cropped(slide, banner_src, c3_x + 0.05, by + 0.05, c3_w - 0.10, bh - 0.10)

    # --- 4. FOOTER ---
    add_rect(slide, 0.35, 7.02, 12.633, 0.015, fill_rgb=RGBColor(203, 213, 225))
    f_brand = art.find(class_="footer-brand-title")
    f_sub = art.find(class_="footer-brand-sub")
    brand_str = f"{f_brand.get_text(strip=True) if f_brand else ''}  •  {f_sub.get_text(strip=True) if f_sub else 'INTERCRON / FORHEALTH'}"
    add_textbox(slide, 0.35, 7.07, 5.5, 0.28, brand_str, font_size=8, bold=True,
                color=t_dark, margin=(0, 0, 0, 0))

    anvisa_col = art.find(class_="footer-col-2")
    anvisa_txt = " ".join(anvisa_col.stripped_strings) if anvisa_col else ""
    add_textbox(slide, 6.0, 7.07, 5.4, 0.28, anvisa_txt, font_size=8, bold=True,
                color=RGBColor(71, 85, 105), align=PP_ALIGN.RIGHT, margin=(0, 0, 0, 0))
    add_textbox(slide, 11.55, 7.07, 1.433, 0.28, f"Slide {slide_num} / {total_slides}",
                font_size=8, bold=True, color=t_col, align=PP_ALIGN.RIGHT, margin=(0, 0, 0, 0))


def build_back_cover_slide(prs, total_slides):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(slide, 0, 0, 13.333, 7.5, fill_rgb=RGBColor(248, 250, 252))
    add_rect(slide, 0, 0, 13.333, 0.12, fill_rgb=RGBColor(30, 58, 138))

    pill = add_rounded_rect(slide, 4.916, 1.85, 3.5, 0.42, fill_rgb=RGBColor(226, 232, 240), radius=0.4)
    tf = pill.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "INTERCRON  •  FORHEALTH"
    r.font.name = FONT_NAME
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = RGBColor(15, 23, 42)

    logo_d = OPT_DIR / "logo_forhealth_dark.png"
    if logo_d.exists():
        add_picture_contained(slide, logo_d, 3.916, 2.55, 5.5, 1.65)

    add_rect(slide, 4.166, 4.55, 1.66, 0.05, fill_rgb=RGBColor(30, 58, 138))
    add_rect(slide, 5.83, 4.55, 1.66, 0.05, fill_rgb=RGBColor(16, 185, 129))
    add_rect(slide, 7.49, 4.55, 1.676, 0.05, fill_rgb=RGBColor(217, 119, 6))

    add_textbox(slide, 1.0, 4.85, 11.333, 0.45,
                "BORG   •   CARTI MASTER   •   CRONOVIT   •   CRONOLIV   •   NUTRIVIX",
                font_size=13, bold=True, color=RGBColor(51, 65, 85), align=PP_ALIGN.CENTER, margin=(0, 0, 0, 0))

    add_rect(slide, 0, 6.85, 13.333, 0.65, fill_rgb=RGBColor(15, 23, 42))
    add_textbox(slide, 0.5, 7.00, 12.333, 0.35,
                f"APRESENTAÇÃO OFICIAL DE PRODUTOS 2026  •  INTERCRON / FORHEALTH  •  Slide {total_slides} / {total_slides}",
                font_size=9.5, bold=True, color=RGBColor(226, 232, 240), align=PP_ALIGN.CENTER, margin=(0, 0, 0, 0))


def main():
    soup = BeautifulSoup(HTML_FILE.read_text(encoding="utf-8"), "html.parser")
    articles = soup.find_all("article", class_="catalog-page")
    total_slides = 2 + len(articles) + 1

    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    build_cover_slide(prs)
    build_toc_slide(prs, soup, total_slides)
    for idx, art in enumerate(articles, start=3):
        build_product_slide(prs, art, idx, total_slides)
    build_back_cover_slide(prs, total_slides)

    prs.save(OUT_PPTX)
    shutil.copy2(OUT_PPTX, DL_PPTX)
    mb = OUT_PPTX.stat().st_size / (1024 * 1024)
    print(f"PPTX 16:9 gerado com sucesso: {total_slides} slides ({mb:.2f} MB)")
    print(f"Projeto: {OUT_PPTX}")
    print(f"Downloads: {DL_PPTX}")


if __name__ == "__main__":
    main()
