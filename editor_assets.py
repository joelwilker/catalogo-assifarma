# -*- coding: utf-8 -*-
"""
Recursos de CSS, HTML e JavaScript para o Editor Visual Estilo Gutenberg — Catálogo Assifarma 2026.
"""

EDITOR_CSS = r"""
    /* ==========================================================================
       BARRA DE CONTROLE DO EDITOR VISUAL ESTILO GUTENBERG / WORDPRESS
       ========================================================================== */
    .editor-top-bar {
      position: sticky;
      top: 0;
      left: 0;
      right: 0;
      z-index: 99999;
      background: #0B132B;
      color: #F8FAFC;
      padding: 9px 20px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      font-family: var(--font-ui), system-ui, sans-serif;
      font-size: 12px;
      box-shadow: 0 6px 24px rgba(0, 0, 0, 0.45);
      border-bottom: 1.5px solid rgba(255, 255, 255, 0.14);
    }

    .editor-left-meta {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .editor-brand-pill {
      background: #1E293B;
      border: 1px solid #334155;
      color: #E2E8F0;
      font-weight: 800;
      padding: 4px 12px;
      border-radius: 999px;
      font-size: 11px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }

    .editor-mode-indicator {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.08);
      padding: 4px 10px;
      border-radius: 6px;
      font-weight: 600;
      color: #E2E8F0;
    }

    .editor-pulse-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #64748B;
      transition: background 0.3s;
    }

    body.is-editing .editor-pulse-dot {
      background: #10B981;
      box-shadow: 0 0 8px #10B981;
    }

    .editor-tip {
      color: #94A3B8;
      font-size: 11px;
    }

    .editor-actions-group {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .editor-btn {
      appearance: none;
      border: 1px solid rgba(255, 255, 255, 0.16);
      background: rgba(255, 255, 255, 0.08);
      color: #F8FAFC;
      padding: 6px 12px;
      border-radius: 6px;
      font-family: inherit;
      font-size: 11.5px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.18s ease;
    }

    .editor-btn:hover {
      background: rgba(255, 255, 255, 0.16);
      transform: translateY(-1px);
    }

    .editor-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
      pointer-events: none;
    }

    .editor-btn-primary {
      background: #2563EB;
      border-color: #3B82F6;
      color: #FFFFFF;
    }

    .editor-btn-primary:hover {
      background: #1D4ED8;
    }

    .editor-btn-active-edit {
      background: #059669 !important;
      border-color: #10B981 !important;
    }

    .editor-btn-success {
      background: #10B981;
      border-color: #34D399;
      color: #022C22;
      font-weight: 700;
    }

    .editor-btn-success:hover {
      background: #059669;
      color: #FFFFFF;
    }

    .editor-btn-subtle {
      background: transparent;
      color: #CBD5E1;
    }

    /* Toast de Feedback */
    #editor-toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 999999;
      background: #0F172A;
      color: #F8FAFC;
      border: 1px solid #334155;
      padding: 11px 18px;
      border-radius: 10px;
      font-family: var(--font-ui), sans-serif;
      font-size: 13px;
      font-weight: 600;
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.35);
      opacity: 0;
      transform: translateY(16px);
      pointer-events: none;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    #editor-toast.show {
      opacity: 1;
      transform: translateY(0);
    }

    /* ==========================================================================
       BLOCOS INTERATIVOS ESTILO GUTENBERG
       ========================================================================== */
    body.is-editing .gb-block {
      position: relative;
      transition: outline 0.15s ease, box-shadow 0.15s ease;
    }

    body.is-editing .gb-block:hover {
      outline: 1.5px dashed rgba(37, 99, 235, 0.65);
      outline-offset: 2px;
    }

    body.is-editing .gb-block.gb-selected {
      outline: 2px solid #2563EB !important;
      outline-offset: 3px;
      box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.14);
      z-index: 40;
    }

    /* Barra Flutuante do Bloco (Gutenberg Block Toolbar) */
    .gutenberg-block-toolbar {
      display: none;
      position: absolute;
      top: -34px;
      left: 0;
      z-index: 1000;
      background: #1E293B;
      color: #FFFFFF;
      border-radius: 7px;
      padding: 3px 6px;
      align-items: center;
      gap: 3px;
      box-shadow: 0 6px 18px rgba(0, 0, 0, 0.28);
      border: 1px solid rgba(255, 255, 255, 0.15);
      font-family: var(--font-ui), system-ui, sans-serif;
      font-size: 11px;
      white-space: nowrap;
      user-select: none;
    }

    body.is-editing .gb-block:hover > .gutenberg-block-toolbar,
    body.is-editing .gb-block.gb-selected > .gutenberg-block-toolbar {
      display: flex;
    }

    .gb-drag-handle {
      cursor: grab;
      padding: 3px 5px;
      color: #94A3B8;
      font-weight: 800;
      font-size: 13px;
      letter-spacing: -1px;
    }

    .gb-drag-handle:active {
      cursor: grabbing;
    }

    .gb-block-label {
      font-size: 10px;
      font-weight: 700;
      color: #93C5FD;
      padding: 0 6px 0 2px;
      border-right: 1px solid rgba(255, 255, 255, 0.15);
      margin-right: 2px;
    }

    .gb-tb-btn {
      appearance: none;
      border: none;
      background: transparent;
      color: #F8FAFC;
      padding: 3px 6px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 3px;
      transition: background 0.12s;
    }

    .gb-tb-btn:hover:not(:disabled) {
      background: #3B82F6;
      color: #FFFFFF;
    }

    .gb-tb-btn:disabled {
      opacity: 0.35;
      cursor: not-allowed;
    }

    .gb-tb-sep {
      width: 1px;
      height: 16px;
      background: rgba(255, 255, 255, 0.15);
      margin: 0 2px;
    }

    /* Indicador de Drop (onde o bloco será solto) */
    .gb-block.gb-drop-above {
      border-top: 3px solid #2563EB !important;
    }
    .gb-block.gb-drop-below {
      border-bottom: 3px solid #2563EB !important;
    }
    .col-left.gb-col-drop-hover,
    .col-right.gb-col-drop-hover {
      background: rgba(37, 99, 235, 0.04);
      outline: 2px dashed rgba(37, 99, 235, 0.45);
      border-radius: 6px;
    }

    /* ==========================================================================
       PAINEL INSPETOR LATERAL ESTILO WORDPRESS GUTENBERG
       ========================================================================== */
    .gutenberg-inspector {
      display: none;
      position: fixed;
      top: 56px;
      right: 14px;
      width: 280px;
      max-height: calc(100vh - 76px);
      overflow-y: auto;
      z-index: 99990;
      background: #FFFFFF;
      color: #0F172A;
      border-radius: 12px;
      box-shadow: 0 14px 40px rgba(15, 23, 42, 0.22);
      border: 1px solid #CBD5E1;
      font-family: var(--font-ui), system-ui, sans-serif;
      font-size: 12px;
    }

    body.is-editing.inspector-open .gutenberg-inspector {
      display: block;
    }

    .gb-insp-header {
      background: #F8FAFC;
      padding: 11px 14px;
      border-bottom: 1px solid #E2E8F0;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-radius: 12px 12px 0 0;
    }

    .gb-insp-title {
      font-weight: 800;
      font-size: 12.5px;
      color: #0F172A;
    }

    .gb-insp-close {
      background: none;
      border: none;
      font-size: 16px;
      cursor: pointer;
      color: #64748B;
      padding: 0 4px;
    }

    .gb-insp-body {
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .gb-insp-section {
      border-bottom: 1px solid #F1F5F9;
      padding-bottom: 12px;
    }

    .gb-insp-section:last-child {
      border-bottom: none;
      padding-bottom: 0;
    }

    .gb-insp-label {
      display: block;
      font-size: 10.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #64748B;
      margin-bottom: 7px;
    }

    .gb-insp-badge {
      display: inline-block;
      background: #EFF6FF;
      color: #1D4ED8;
      border: 1px solid #BFDBFE;
      font-weight: 700;
      font-size: 11px;
      padding: 3px 8px;
      border-radius: 6px;
    }

    .gb-insp-btn-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
    }

    .gb-insp-btn {
      appearance: none;
      border: 1px solid #CBD5E1;
      background: #F8FAFC;
      color: #1E293B;
      padding: 6px 8px;
      border-radius: 6px;
      font-family: inherit;
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      transition: all 0.14s;
    }

    .gb-insp-btn:hover:not(:disabled) {
      background: #2563EB;
      border-color: #2563EB;
      color: #FFFFFF;
    }

    .gb-insp-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    .gb-insp-btn.active-col {
      background: #DBEAFE;
      border-color: #3B82F6;
      color: #1E40AF;
    }

    .gb-insp-control-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 8px;
    }

    .gb-insp-control-row span.ctrl-name {
      font-size: 11.5px;
      font-weight: 600;
      color: #334155;
    }

    .gb-stepper {
      display: inline-flex;
      align-items: center;
      border: 1px solid #CBD5E1;
      border-radius: 6px;
      overflow: hidden;
      background: #FFFFFF;
    }

    .gb-stepper button {
      border: none;
      background: #F1F5F9;
      color: #0F172A;
      width: 24px;
      height: 24px;
      font-weight: 700;
      cursor: pointer;
    }

    .gb-stepper button:hover {
      background: #2563EB;
      color: #FFFFFF;
    }

    .gb-stepper span {
      min-width: 42px;
      text-align: center;
      font-size: 11px;
      font-weight: 700;
      color: #0F172A;
    }

    /* ==========================================================================
       CONTROLES DE IMAGEM (ZOOM, PAN E REDIMENSIONAMENTO DE MÁSCARA)
       ========================================================================== */
    body.is-editing .glass-product-stage,
    body.is-editing .glass-stage-panoramic,
    body.is-editing .image-illustrative-card,
    body.is-editing .image-placeholder-card {
      position: relative;
      overflow: hidden !important;
    }

    body.is-editing .glass-product-stage img,
    body.is-editing .glass-stage-panoramic img,
    body.is-editing .image-illustrative-card img {
      cursor: grab;
      transition: none;
      user-select: none;
      -webkit-user-drag: none;
    }

    body.is-editing img.is-panning {
      cursor: grabbing !important;
    }

    .image-edit-toolbar {
      display: none;
      position: absolute;
      bottom: 12px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 950;
      background: rgba(15, 23, 42, 0.92);
      backdrop-filter: blur(8px);
      color: #F8FAFC;
      padding: 5px 10px;
      border-radius: 999px;
      align-items: center;
      gap: 8px;
      font-family: var(--font-ui), sans-serif;
      font-size: 11px;
      white-space: nowrap;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);
      border: 1px solid rgba(255, 255, 255, 0.18);
    }

    body.is-editing .glass-product-stage:hover .image-edit-toolbar,
    body.is-editing .glass-stage-panoramic:hover .image-edit-toolbar,
    body.is-editing .image-illustrative-card:hover .image-edit-toolbar,
    body.is-editing .image-placeholder-card:hover .image-edit-toolbar {
      display: flex;
    }

    .img-tool-btn, .img-tool-step {
      appearance: none;
      border: 1px solid rgba(255, 255, 255, 0.22);
      background: rgba(255, 255, 255, 0.1);
      color: #FFFFFF;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 10.5px;
      font-weight: 600;
      cursor: pointer;
    }

    .img-tool-btn:hover, .img-tool-step:hover {
      background: #2563EB;
      border-color: #60A5FA;
    }

    .img-tool-group {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      border-left: 1px solid rgba(255, 255, 255, 0.2);
      padding-left: 6px;
    }

    .tool-label {
      color: #94A3B8;
      font-size: 10px;
    }

    .mask-resize-handle {
      display: none;
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 10px;
      background: linear-gradient(to bottom, transparent, rgba(37, 99, 235, 0.35));
      cursor: ns-resize;
      z-index: 960;
      align-items: center;
      justify-content: center;
    }

    .mask-resize-handle::after {
      content: "⬍ Arraste para ajustar máscara";
      font-family: var(--font-ui), sans-serif;
      font-size: 9px;
      font-weight: 700;
      color: #FFFFFF;
      background: #2563EB;
      padding: 1px 8px;
      border-radius: 999px;
      opacity: 0;
      transition: opacity 0.15s;
    }

    body.is-editing .glass-product-stage:hover .mask-resize-handle,
    body.is-editing .glass-stage-panoramic:hover .mask-resize-handle,
    body.is-editing .image-illustrative-card:hover .mask-resize-handle,
    body.is-editing .image-placeholder-card:hover .mask-resize-handle {
      display: flex;
    }

    body.is-editing .mask-resize-handle:hover::after {
      opacity: 1;
    }

    .drop-zone-overlay {
      display: none;
      position: absolute;
      inset: 0;
      background: rgba(37, 99, 235, 0.85);
      color: #FFFFFF;
      z-index: 980;
      align-items: center;
      justify-content: center;
      font-family: var(--font-ui), sans-serif;
      font-size: 14px;
      font-weight: 700;
      border: 3px dashed #FFFFFF;
      border-radius: inherit;
    }

    .is-drag-over .drop-zone-overlay {
      display: flex;
    }

    body.is-editing [contenteditable="true"] {
      cursor: text;
      transition: outline 0.12s;
    }

    body.is-editing [contenteditable="true"]:hover {
      outline: 1px dashed rgba(59, 130, 246, 0.45);
      border-radius: 3px;
    }

    body.is-editing [contenteditable="true"]:focus {
      outline: 2px solid #2563EB !important;
      outline-offset: 2px;
      background-color: rgba(37, 99, 235, 0.06) !important;
      border-radius: 4px;
    }

    /* OCULTAR TUDO NA IMPRESSÃO / PDF */
    @media print {
      .editor-top-bar,
      #editor-toast,
      .gutenberg-block-toolbar,
      .gutenberg-inspector,
      .image-edit-toolbar,
      .mask-resize-handle,
      .drop-zone-overlay,
      .hidden-editor-file-input {
        display: none !important;
      }
      .gb-block {
        outline: none !important;
        box-shadow: none !important;
      }
    }
"""

EDITOR_BODY_START = r"""  <!-- BARRA DE CONTROLE DO EDITOR VISUAL ESTILO GUTENBERG -->
  <aside class="editor-top-bar">
    <div class="editor-left-meta">
      <span class="editor-brand-pill">Assifarma • Editor Visual</span>
      <div class="editor-mode-indicator">
        <span class="editor-pulse-dot"></span>
        <span id="editor-status-text">Modo Visualização</span>
      </div>
      <span class="editor-tip">💡 No Modo Edição: clique em qualquer bloco (ex: Destaques) para mover entre colunas ⬅️ ➡️, ajustar espaçamento, zoom ou texto.</span>
    </div>

    <div class="editor-actions-group">
      <button id="btn-toggle-edit" class="editor-btn editor-btn-primary" onclick="toggleEditMode()">
        ✏️ Ativar Editor Gutenberg
      </button>
      <button id="btn-toggle-inspector" class="editor-btn" onclick="toggleInspector()" style="display:none;" title="Abrir/Fechar Painel Lateral do Bloco">
        ⚙️ Inspetor de Bloco
      </button>
      <button id="btn-undo" class="editor-btn" onclick="undoEdit()" disabled title="Desfazer última alteração (Cmd+Z / Ctrl+Z)">
        ↩️ Desfazer
      </button>
      <button id="btn-redo" class="editor-btn" onclick="redoEdit()" disabled title="Refazer alteração (Cmd+Shift+Z / Ctrl+Y)">
        ↪️ Refazer
      </button>
      <button id="btn-save-catalog" class="editor-btn editor-btn-success" onclick="saveCatalog()" title="Salvar alterações no arquivo catalogo_completo.html (Cmd+S / Ctrl+S)">
        💾 Salvar Alterações
      </button>
      <button class="editor-btn" onclick="downloadHtmlBackup()" title="Baixar cópia do arquivo HTML">
        📥 Baixar HTML
      </button>
      <button id="btn-discard" class="editor-btn editor-btn-subtle" onclick="discardEdits()" title="Recarregar versão salva do disco">
        ↩️ Recarregar
      </button>
      <button class="editor-btn" onclick="window.print()" title="Imprimir ou gerar PDF (Cmd+P)">
        🖨️ PDF (Cmd+P)
      </button>
    </div>
  </aside>

  <!-- PAINEL LATERAL INSPETOR ESTILO WORDPRESS -->
  <aside class="gutenberg-inspector" id="gutenberg-inspector">
    <div class="gb-insp-header">
      <span class="gb-insp-title">⚙️ Inspetor de Bloco</span>
      <button class="gb-insp-close" onclick="toggleInspector(false)" title="Fechar Painel">&times;</button>
    </div>
    <div class="gb-insp-body" id="gb-insp-content">
      <p style="color:#64748B; text-align:center; padding: 16px 0;">
        Clique em qualquer bloco no catálogo (Destaques, Tabela Nutricional, Imagem, Card de Texto) para editar suas propriedades em tempo real.
      </p>
    </div>
  </aside>

  <div id="editor-toast"></div>
  <input type="file" id="editor-global-file-input" class="hidden-editor-file-input" accept="image/*" style="display: none;" />"""

EDITOR_BODY_END = r"""  <!-- SCRIPT DO EDITOR INTERATIVO ESTILO GUTENBERG / WORDPRESS -->
  <script>
    let isEditing = false;
    let hasUnsavedChanges = false;
    let activeTargetStage = null;
    let selectedBlock = null;
    let draggedBlock = null;

    // Histórico Desfazer / Refazer (Gutenberg)
    const MAX_HISTORY = 50;
    let undoStack = [];
    let redoStack = [];
    let lastCommittedSnapshot = null;
    let isRestoringHistory = false;
    let inputHistoryTimer = null;

    const DRAFT_KEY = 'assifarma_catalog_draft_v1';
    const DRAFT_TIME_KEY = 'assifarma_catalog_draft_v1_time';

    const editableTextSelectors = [
      '.title-product-unified',
      '.hero-category-glass',
      '.md-denominacao-venda',
      '.key-spec-box .key-spec-value',
      '.key-spec-box .key-spec-label',
      '.hl-main',
      '.active-badge-pill',
      '.card-heading',
      '.md-benefits-list li',
      '.ingredients-copy',
      '.allergens-inline',
      '.warnings-caps',
      '.conservation-text',
      '.anvisa-title',
      '.anvisa-serving-block',
      '.anvisa-table th',
      '.anvisa-table td',
      '.anvisa-insignificant',
      '.anvisa-footnote',
      '.footer-brand-title',
      '.footer-brand-sub',
      '.footer-col-2 strong',
      '.cover-edition-label',
      '.cover-edition-sub',
      '.toc-giant-heading',
      '.toc-sub-heading',
      '.toc-clean-name',
      '.toc-clean-page'
    ];

    function toggleEditMode() {
      isEditing = !isEditing;
      const btn = document.getElementById('btn-toggle-edit');
      const inspBtn = document.getElementById('btn-toggle-inspector');
      const statusText = document.getElementById('editor-status-text');

      if (isEditing) {
        document.body.classList.add('is-editing');
        document.body.classList.add('inspector-open');
        btn.innerHTML = '👁️ Finalizar Edição';
        btn.classList.add('editor-btn-active-edit');
        if (inspBtn) inspBtn.style.display = 'inline-flex';
        statusText.innerText = 'Modo Edição Ativo';
        showToast('✏️ Editor Gutenberg Ativo! Clique em qualquer bloco para mover entre colunas, editar textos ou ajustar imagens.');

        editableTextSelectors.forEach(sel => {
          document.querySelectorAll(sel).forEach(el => {
            el.setAttribute('contenteditable', 'true');
            el.setAttribute('spellcheck', 'false');
          });
        });

        setupGutenbergBlocks();
        setupImageContainers();
        if (lastCommittedSnapshot === null) {
          lastCommittedSnapshot = getCleanWrapperHtml();
        }
        updateUndoRedoButtons();
      } else {
        document.body.classList.remove('is-editing');
        document.body.classList.remove('inspector-open');
        if (selectedBlock) {
          selectedBlock.classList.remove('gb-selected');
          selectedBlock = null;
        }
        btn.innerHTML = '✏️ Ativar Editor Gutenberg';
        btn.classList.remove('editor-btn-active-edit');
        if (inspBtn) inspBtn.style.display = 'none';
        statusText.innerText = hasUnsavedChanges ? 'Modo Visualização (● Alterações pendentes)' : 'Modo Visualização';
        showToast('👁️ Modo Visualização ativado.');

        editableTextSelectors.forEach(sel => {
          document.querySelectorAll(sel).forEach(el => {
            el.removeAttribute('contenteditable');
          });
        });
      }
    }

    function toggleInspector(forceState) {
      if (typeof forceState === 'boolean') {
        document.body.classList.toggle('inspector-open', forceState);
      } else {
        document.body.classList.toggle('inspector-open');
      }
    }

    function getBlockLabel(el) {
      if (el.classList.contains('key-actives-container')) return '✨ Destaques de Ativos';
      if (el.classList.contains('below-image-highlights')) return '🏷️ Selos Rápidos';
      if (el.classList.contains('anvisa-box')) return '📊 Tabela Nutricional';
      if (el.classList.contains('glass-product-stage') || el.classList.contains('glass-stage-panoramic')) return '🖼️ Imagem Produto';
      if (el.classList.contains('warnings-precautions-card')) return '⚠️ Advertências';
      if (el.classList.contains('conservation-card')) return '❄️ Conservação';
      if (el.classList.contains('glass-info-card')) {
        const h = el.querySelector('.card-heading');
        return h ? '📝 ' + h.innerText.trim() : '📝 Card de Texto';
      }
      if (el.classList.contains('image-illustrative-card') || el.classList.contains('image-placeholder-card')) {
        return '🎨 Banner Ilustrativo';
      }
      return '📦 Bloco';
    }

    function setupGutenbergBlocks() {
      const cols = document.querySelectorAll('.col-left, .col-right');
      cols.forEach(col => {
        Array.from(col.children).forEach(block => {
          initSingleBlock(block);
        });
        setupColumnDrop(col);
      });

      // Também permitir seleção em banners de base
      document.querySelectorAll('.placeholder-banner-section > div').forEach(banner => {
        initSingleBlock(banner);
      });
    }

    function initSingleBlock(block) {
      if (block.dataset.gbInit === '1') {
        updateBlockToolbarState(block);
        return;
      }
      block.dataset.gbInit = '1';
      block.classList.add('gb-block');

      const label = getBlockLabel(block);

      const tb = document.createElement('div');
      tb.className = 'gutenberg-block-toolbar';
      tb.innerHTML = `
        <span class="gb-drag-handle" title="Arraste para mover este bloco para qualquer posição ou coluna">⋮⋮</span>
        <span class="gb-block-label">${label}</span>
        <button type="button" class="gb-tb-btn" data-gb="up" title="Mover bloco para cima">▲</button>
        <button type="button" class="gb-tb-btn" data-gb="down" title="Mover bloco para baixo">▼</button>
        <span class="gb-tb-sep"></span>
        <button type="button" class="gb-tb-btn" data-gb="to-left" title="Mover para Coluna Esquerda">⬅️ Esq.</button>
        <button type="button" class="gb-tb-btn" data-gb="to-right" title="Mover para Coluna Direita">Dir. ➡️</button>
        <span class="gb-tb-sep"></span>
        <button type="button" class="gb-tb-btn" data-gb="inspect" title="Configurar espaçamento, fonte e propriedades">⚙️</button>
      `;
      block.prepend(tb);

      // Seleção do bloco ao clicar
      block.addEventListener('mousedown', (e) => {
        if (!isEditing) return;
        if (e.target.closest('.image-edit-toolbar') || e.target.closest('.mask-resize-handle')) return;
        selectBlock(block);
      });

      // Ações da barra do bloco
      tb.addEventListener('click', (e) => {
        const btn = e.target.closest('button');
        if (!btn) return;
        e.stopPropagation();
        const act = btn.dataset.gb;
        if (act === 'up') moveBlockVertical(block, -1);
        else if (act === 'down') moveBlockVertical(block, 1);
        else if (act === 'to-left') moveBlockToColumn(block, 'left');
        else if (act === 'to-right') moveBlockToColumn(block, 'right');
        else if (act === 'inspect') {
          selectBlock(block);
          toggleInspector(true);
        }
      });

      // Drag and drop pelo handle ⋮⋮
      const handle = tb.querySelector('.gb-drag-handle');
      handle.addEventListener('mousedown', () => {
        block.setAttribute('draggable', 'true');
      });
      handle.addEventListener('mouseup', () => {
        block.removeAttribute('draggable');
      });

      block.addEventListener('dragstart', (e) => {
        if (!isEditing) return;
        draggedBlock = block;
        e.dataTransfer.effectAllowed = 'move';
        e.dataTransfer.setData('text/plain', 'gb-block');
        setTimeout(() => block.style.opacity = '0.45', 0);
      });

      block.addEventListener('dragend', () => {
        block.style.opacity = '';
        block.removeAttribute('draggable');
        document.querySelectorAll('.gb-drop-above, .gb-drop-below, .gb-col-drop-hover').forEach(el => {
          el.classList.remove('gb-drop-above', 'gb-drop-below', 'gb-col-drop-hover');
        });
        draggedBlock = null;
      });

      block.addEventListener('dragover', (e) => {
        if (!isEditing || !draggedBlock || draggedBlock === block) return;
        if (!block.parentElement.classList.contains('col-left') && !block.parentElement.classList.contains('col-right')) return;
        e.preventDefault();
        const rect = block.getBoundingClientRect();
        const isTop = (e.clientY - rect.top) < (rect.height / 2);
        block.classList.toggle('gb-drop-above', isTop);
        block.classList.toggle('gb-drop-below', !isTop);
      });

      block.addEventListener('dragleave', () => {
        block.classList.remove('gb-drop-above', 'gb-drop-below');
      });

      block.addEventListener('drop', (e) => {
        if (!isEditing || !draggedBlock || draggedBlock === block) return;
        const targetCol = block.parentElement;
        if (!targetCol.classList.contains('col-left') && !targetCol.classList.contains('col-right')) return;
        e.preventDefault();
        e.stopPropagation();

        const isTop = block.classList.contains('gb-drop-above');
        block.classList.remove('gb-drop-above', 'gb-drop-below');

        if (isTop) {
          targetCol.insertBefore(draggedBlock, block);
        } else {
          targetCol.insertBefore(draggedBlock, block.nextSibling);
        }
        onBlockMoved(draggedBlock);
      });

      updateBlockToolbarState(block);
    }

    function setupColumnDrop(col) {
      if (col.dataset.gbColInit === '1') return;
      col.dataset.gbColInit = '1';

      col.addEventListener('dragover', (e) => {
        if (!isEditing || !draggedBlock) return;
        e.preventDefault();
        col.classList.add('gb-col-drop-hover');
      });

      col.addEventListener('dragleave', (e) => {
        if (!col.contains(e.relatedTarget)) {
          col.classList.remove('gb-col-drop-hover');
        }
      });

      col.addEventListener('drop', (e) => {
        if (!isEditing || !draggedBlock) return;
        e.preventDefault();
        col.classList.remove('gb-col-drop-hover');
        if (e.target === col) {
          col.appendChild(draggedBlock);
          onBlockMoved(draggedBlock);
        }
      });
    }

    function updateBlockToolbarState(block) {
      const tb = block.querySelector(':scope > .gutenberg-block-toolbar');
      if (!tb) return;
      const parent = block.parentElement;
      const isLeft = parent && parent.classList.contains('col-left');
      const isRight = parent && parent.classList.contains('col-right');

      const btnLeft = tb.querySelector('[data-gb="to-left"]');
      const btnRight = tb.querySelector('[data-gb="to-right"]');
      if (btnLeft) btnLeft.disabled = !isRight;
      if (btnRight) btnRight.disabled = !isLeft;
    }

    function moveBlockVertical(block, dir) {
      const parent = block.parentElement;
      if (!parent) return;
      if (dir < 0 && block.previousElementSibling) {
        parent.insertBefore(block, block.previousElementSibling);
        onBlockMoved(block);
      } else if (dir > 0 && block.nextElementSibling) {
        parent.insertBefore(block.nextElementSibling, block);
        onBlockMoved(block);
      }
    }

    function moveBlockToColumn(block, targetSide) {
      const grid = block.closest('.equal-columns-grid');
      if (!grid) {
        showToast('⚠️ Este bloco ocupa as 2 colunas e não pertence a uma coluna individual.');
        return;
      }
      const targetCol = grid.querySelector(targetSide === 'left' ? '.col-left' : '.col-right');
      if (!targetCol || block.parentElement === targetCol) return;

      targetCol.appendChild(block);
      onBlockMoved(block);
      showToast(targetSide === 'left' ? '⬅️ Bloco movido para a Coluna Esquerda!' : '➡️ Bloco movido para a Coluna Direita!');
    }

    function onBlockMoved(block) {
      updateBlockToolbarState(block);
      selectBlock(block);
      markDirty();
    }

    function selectBlock(block) {
      if (selectedBlock && selectedBlock !== block) {
        selectedBlock.classList.remove('gb-selected');
      }
      selectedBlock = block;
      block.classList.add('gb-selected');
      renderInspectorForBlock(block);
    }

    function renderInspectorForBlock(block) {
      const container = document.getElementById('gb-insp-content');
      if (!container) return;

      const label = getBlockLabel(block);
      const parent = block.parentElement;
      const isLeft = parent && parent.classList.contains('col-left');
      const isRight = parent && parent.classList.contains('col-right');
      const inColumn = isLeft || isRight;

      const comp = window.getComputedStyle(block);
      const curFontPt = parseFloat(block.style.fontSize) || (parseFloat(comp.fontSize) * 0.75);
      const curPadMm = parseFloat(block.style.paddingTop) || 2.8;
      const curFlex = block.style.flex || comp.flexGrow;
      const isStretched = (block.style.flex === '1 1 0%' || block.style.flex === '1' || (!block.style.flex && parseFloat(comp.flexGrow) >= 1));
      const colGap = parent && parent.style.gap ? parseFloat(parent.style.gap) : 2.8;

      container.innerHTML = `
        <div class="gb-insp-section">
          <span class="gb-insp-label">Bloco Selecionado</span>
          <span class="gb-insp-badge">${label}</span>
        </div>

        ${inColumn ? `
        <div class="gb-insp-section">
          <span class="gb-insp-label">Mover Entre Colunas</span>
          <div class="gb-insp-btn-grid" style="margin-bottom:8px;">
            <button type="button" class="gb-insp-btn ${isLeft ? 'active-col' : ''}" onclick="moveSelectedTo('left')" ${isLeft ? 'disabled' : ''}>⬅️ Esquerda</button>
            <button type="button" class="gb-insp-btn ${isRight ? 'active-col' : ''}" onclick="moveSelectedTo('right')" ${isRight ? 'disabled' : ''}>Direita ➡️</button>
          </div>
          <div class="gb-insp-btn-grid">
            <button type="button" class="gb-insp-btn" onclick="moveSelectedVert(-1)">⬆️ Subir Bloco</button>
            <button type="button" class="gb-insp-btn" onclick="moveSelectedVert(1)">⬇️ Descer Bloco</button>
          </div>
        </div>
        ` : ''}

        <div class="gb-insp-section">
          <span class="gb-insp-label">Tipografia & Espaçamento</span>
          <div class="gb-insp-control-row">
            <span class="ctrl-name">Tamanho do Texto</span>
            <div class="gb-stepper">
              <button type="button" onclick="adjustSelectedFont(-0.5)">-</button>
              <span id="insp-font-val">${curFontPt.toFixed(1)}pt</span>
              <button type="button" onclick="adjustSelectedFont(0.5)">+</button>
            </div>
          </div>

          <div class="gb-insp-control-row">
            <span class="ctrl-name">Padding Vertical</span>
            <div class="gb-stepper">
              <button type="button" onclick="adjustSelectedPad(-0.5)">-</button>
              <span id="insp-pad-val">${curPadMm.toFixed(1)}mm</span>
              <button type="button" onclick="adjustSelectedPad(0.5)">+</button>
            </div>
          </div>

          ${inColumn ? `
          <div class="gb-insp-control-row">
            <span class="ctrl-name">Espaço da Coluna</span>
            <div class="gb-stepper">
              <button type="button" onclick="adjustColGap(-0.5)">-</button>
              <span id="insp-gap-val">${colGap.toFixed(1)}mm</span>
              <button type="button" onclick="adjustColGap(0.5)">+</button>
            </div>
          </div>

          <div class="gb-insp-control-row" style="margin-top:8px;">
            <span class="ctrl-name">Altura Automática</span>
            <button type="button" class="gb-insp-btn" onclick="toggleSelectedFlex()" style="padding:4px 10px;">
              ${isStretched ? '📐 Esticado (Flex)' : '📦 Compacto'}
            </button>
          </div>
          ` : ''}
        </div>

        <div class="gb-insp-section">
          <span class="gb-insp-label">Ações Rápidas</span>
          <div class="gb-insp-btn-grid">
            <button type="button" class="gb-insp-btn" onclick="resetSelectedBlockStyles()">🔄 Resetar Bloco</button>
            <button type="button" class="gb-insp-btn" style="color:#DC2626;" onclick="toggleHideSelectedBlock()">👁️‍🗨️ Ocultar</button>
          </div>
        </div>
      `;
    }

    function moveSelectedTo(side) {
      if (selectedBlock) moveBlockToColumn(selectedBlock, side);
    }

    function moveSelectedVert(dir) {
      if (selectedBlock) moveBlockVertical(selectedBlock, dir);
    }

    function adjustSelectedFont(delta) {
      if (!selectedBlock) return;
      const comp = window.getComputedStyle(selectedBlock);
      const cur = parseFloat(selectedBlock.style.fontSize) || (parseFloat(comp.fontSize) * 0.75);
      const next = Math.max(5.5, Math.min(24, cur + delta));
      selectedBlock.style.fontSize = next.toFixed(1) + 'pt';
      // Também aplicar aos filhos de texto comuns
      selectedBlock.querySelectorAll('p, li, td, th, span:not(.gb-block-label)').forEach(el => {
        el.style.fontSize = next.toFixed(1) + 'pt';
      });
      renderInspectorForBlock(selectedBlock);
      markDirty();
    }

    function adjustSelectedPad(delta) {
      if (!selectedBlock) return;
      const cur = parseFloat(selectedBlock.style.paddingTop) || 2.8;
      const next = Math.max(0.5, Math.min(18, cur + delta));
      selectedBlock.style.paddingTop = next.toFixed(1) + 'mm';
      selectedBlock.style.paddingBottom = next.toFixed(1) + 'mm';
      renderInspectorForBlock(selectedBlock);
      markDirty();
    }

    function adjustColGap(delta) {
      if (!selectedBlock || !selectedBlock.parentElement) return;
      const col = selectedBlock.parentElement;
      const cur = col.style.gap ? parseFloat(col.style.gap) : 2.8;
      const next = Math.max(0.5, Math.min(15, cur + delta));
      col.style.gap = next.toFixed(1) + 'mm';
      renderInspectorForBlock(selectedBlock);
      markDirty();
    }

    function toggleSelectedFlex() {
      if (!selectedBlock) return;
      const comp = window.getComputedStyle(selectedBlock);
      const isStretched = (selectedBlock.style.flex === '1 1 0%' || selectedBlock.style.flex === '1' || (!selectedBlock.style.flex && parseFloat(comp.flexGrow) >= 1));
      selectedBlock.style.flex = isStretched ? '0 0 auto' : '1 1 0%';
      renderInspectorForBlock(selectedBlock);
      markDirty();
    }

    function resetSelectedBlockStyles() {
      if (!selectedBlock) return;
      selectedBlock.style.fontSize = '';
      selectedBlock.style.paddingTop = '';
      selectedBlock.style.paddingBottom = '';
      selectedBlock.style.flex = '';
      selectedBlock.querySelectorAll('p, li, td, th, span').forEach(el => el.style.fontSize = '');
      renderInspectorForBlock(selectedBlock);
      showToast('🔄 Estilos do bloco restaurados.');
      markDirty();
    }

    function toggleHideSelectedBlock() {
      if (!selectedBlock) return;
      if (confirm('Deseja remover/ocultar este bloco da página?')) {
        selectedBlock.style.display = 'none';
        markDirty();
        showToast('👁️‍🗨️ Bloco ocultado.');
      }
    }

    /* ==========================================================================
       CONTROLES DE IMAGEM (ZOOM, PAN, ALTURA DA MÁSCARA, UPLOAD)
       ========================================================================== */
    function setupImageContainers() {
      const stages = document.querySelectorAll(
        '.glass-product-stage, .glass-stage-panoramic, .image-illustrative-card, .image-placeholder-card'
      );

      stages.forEach(stage => {
        if (!stage.querySelector('.image-edit-toolbar')) {
          const tb = document.createElement('div');
          tb.className = 'image-edit-toolbar';
          tb.innerHTML = `
            <button type="button" class="img-tool-btn" data-act="upload" title="Substituir imagem do computador">📁 Trocar Imagem</button>
            <div class="img-tool-group">
              <span class="tool-label">Zoom:</span>
              <button type="button" class="img-tool-step" data-act="zoom-out">-</button>
              <span class="zoom-value-label">100%</span>
              <button type="button" class="img-tool-step" data-act="zoom-in">+</button>
            </div>
            <div class="img-tool-group">
              <span class="tool-label">Máscara:</span>
              <button type="button" class="img-tool-step" data-act="h-down">-</button>
              <span class="height-value-label">${Math.round(stage.offsetHeight)}px</span>
              <button type="button" class="img-tool-step" data-act="h-up">+</button>
            </div>
            <button type="button" class="img-tool-btn reset-btn" data-act="reset" title="Resetar imagem">🔄</button>
          `;
          stage.appendChild(tb);

          const handle = document.createElement('div');
          handle.className = 'mask-resize-handle';
          handle.title = 'Arraste para ajustar a altura da máscara';
          stage.appendChild(handle);

          const dropOv = document.createElement('div');
          dropOv.className = 'drop-zone-overlay';
          dropOv.innerHTML = '<span>📥 Solte a imagem aqui</span>';
          stage.appendChild(dropOv);

          attachStageEvents(stage);
        }
      });
    }

    function attachStageEvents(stage) {
      const img = stage.querySelector('img');
      const tb = stage.querySelector('.image-edit-toolbar');
      const handle = stage.querySelector('.mask-resize-handle');
      const zoomLbl = tb ? tb.querySelector('.zoom-value-label') : null;
      const heightLbl = tb ? tb.querySelector('.height-value-label') : null;

      let state = { zoom: 1.0, panX: 0, panY: 0 };
      if (img && img.dataset.zoom) {
        state.zoom = parseFloat(img.dataset.zoom) || 1.0;
        state.panX = parseFloat(img.dataset.panX) || 0;
        state.panY = parseFloat(img.dataset.panY) || 0;
      }

      function updateTransform() {
        if (!img) return;
        img.style.transform = `translate(${state.panX}px, ${state.panY}px) scale(${state.zoom})`;
        img.dataset.zoom = state.zoom;
        img.dataset.panX = state.panX;
        img.dataset.panY = state.panY;
        if (zoomLbl) zoomLbl.innerText = `${Math.round(state.zoom * 100)}%`;
        markDirty();
      }

      function updateHeight(newH) {
        stage.style.height = `${newH}px`;
        stage.style.minHeight = `${newH}px`;
        stage.style.maxHeight = `${newH}px`;
        if (heightLbl) heightLbl.innerText = `${Math.round(newH)}px`;
        markDirty();
      }

      if (tb) {
        tb.addEventListener('click', (e) => {
          const btn = e.target.closest('button');
          if (!btn) return;
          e.stopPropagation();
          const act = btn.dataset.act;

          if (act === 'upload') {
            activeTargetStage = stage;
            const fileInput = document.getElementById('editor-global-file-input');
            fileInput.value = '';
            fileInput.click();
          } else if (act === 'zoom-in') {
            state.zoom = Math.min(3.5, state.zoom + 0.15);
            updateTransform();
          } else if (act === 'zoom-out') {
            state.zoom = Math.max(0.4, state.zoom - 0.15);
            updateTransform();
          } else if (act === 'h-up') {
            updateHeight(stage.offsetHeight + 10);
          } else if (act === 'h-down') {
            updateHeight(Math.max(60, stage.offsetHeight - 10));
          } else if (act === 'reset') {
            state.zoom = 1.0;
            state.panX = 0;
            state.panY = 0;
            updateTransform();
            stage.style.height = '';
            stage.style.minHeight = '';
            stage.style.maxHeight = '';
            if (heightLbl) heightLbl.innerText = `${Math.round(stage.offsetHeight)}px`;
            showToast('🔄 Imagem redefinida.');
          }
        });
      }

      if (img) {
        let isPanning = false;
        let startX = 0, startY = 0, initPanX = 0, initPanY = 0;

        img.addEventListener('mousedown', (e) => {
          if (!isEditing || e.button !== 0) return;
          isPanning = true;
          img.classList.add('is-panning');
          startX = e.clientX;
          startY = e.clientY;
          initPanX = state.panX;
          initPanY = state.panY;
          e.preventDefault();
        });

        window.addEventListener('mousemove', (e) => {
          if (!isPanning) return;
          state.panX = initPanX + (e.clientX - startX);
          state.panY = initPanY + (e.clientY - startY);
          updateTransform();
        });

        window.addEventListener('mouseup', () => {
          if (isPanning) {
            isPanning = false;
            img.classList.remove('is-panning');
          }
        });

        stage.addEventListener('wheel', (e) => {
          if (!isEditing) return;
          e.preventDefault();
          const delta = e.deltaY < 0 ? 0.08 : -0.08;
          state.zoom = Math.max(0.4, Math.min(3.5, state.zoom + delta));
          updateTransform();
        }, { passive: false });
      }

      if (handle) {
        let isResizing = false;
        let startY = 0, startH = 0;

        handle.addEventListener('mousedown', (e) => {
          if (!isEditing || e.button !== 0) return;
          isResizing = true;
          startY = e.clientY;
          startH = stage.offsetHeight;
          document.body.style.cursor = 'ns-resize';
          e.preventDefault();
          e.stopPropagation();
        });

        window.addEventListener('mousemove', (e) => {
          if (!isResizing) return;
          const newH = Math.max(50, startH + (e.clientY - startY));
          updateHeight(newH);
        });

        window.addEventListener('mouseup', () => {
          if (isResizing) {
            isResizing = false;
            document.body.style.cursor = '';
          }
        });
      }

      stage.addEventListener('dragover', (e) => {
        if (!isEditing || draggedBlock) return;
        e.preventDefault();
        stage.classList.add('is-drag-over');
      });

      stage.addEventListener('dragleave', (e) => {
        if (!stage.contains(e.relatedTarget)) {
          stage.classList.remove('is-drag-over');
        }
      });

      stage.addEventListener('drop', (e) => {
        if (!isEditing || draggedBlock) return;
        e.preventDefault();
        stage.classList.remove('is-drag-over');
        const files = e.dataTransfer.files;
        if (files && files.length > 0 && files[0].type.startsWith('image/')) {
          applyNewImageFile(stage, files[0]);
        }
      });
    }

    document.addEventListener('DOMContentLoaded', () => {
      const fileInput = document.getElementById('editor-global-file-input');
      if (fileInput) {
        fileInput.addEventListener('change', (e) => {
          if (e.target.files && e.target.files.length > 0 && activeTargetStage) {
            applyNewImageFile(activeTargetStage, e.target.files[0]);
          }
        });
      }
    });

    async function applyNewImageFile(stage, file) {
      showToast(`Carregando imagem: ${file.name}...`);
      const reader = new FileReader();
      reader.onload = async (e) => {
        const base64Data = e.target.result;
        try {
          const resp = await fetch('/api/upload-image', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ filename: file.name, data: base64Data })
          });
          const res = await resp.json();
          if (res.status === 'ok' && res.url) {
            setImageSource(stage, res.url);
            showToast(`✅ Imagem salva e aplicada: ${file.name}`);
            return;
          }
        } catch (err) {}
        setImageSource(stage, base64Data);
        showToast(`✅ Imagem aplicada: ${file.name}`);
      };
      reader.readAsDataURL(file);
    }

    function setImageSource(stage, src) {
      let img = stage.querySelector('img');
      if (!img) {
        stage.className = 'image-illustrative-card gb-block';
        stage.innerHTML = `<img class="banner-photo" src="${src}" alt="Imagem Ilustrativa" />`;
        stage.dataset.gbInit = '';
        initSingleBlock(stage);
        setupImageContainers();
      } else {
        img.src = src;
        img.style.transform = 'translate(0px, 0px) scale(1)';
        img.dataset.zoom = 1;
        img.dataset.panX = 0;
        img.dataset.panY = 0;
      }
      markDirty();
    }

    function cleanCloneNode(root) {
      root.querySelectorAll('[contenteditable]').forEach(el => el.removeAttribute('contenteditable'));
      root.querySelectorAll('[spellcheck]').forEach(el => el.removeAttribute('spellcheck'));
      root.querySelectorAll('[draggable]').forEach(el => el.removeAttribute('draggable'));
      root.querySelectorAll('[data-gb-init]').forEach(el => el.removeAttribute('data-gb-init'));
      root.querySelectorAll('[data-gb-col-init]').forEach(el => el.removeAttribute('data-gb-col-init'));
      root.querySelectorAll('.gutenberg-block-toolbar, .image-edit-toolbar, .mask-resize-handle, .drop-zone-overlay').forEach(el => el.remove());
      root.querySelectorAll('.gb-selected, .is-selected, .is-panning, .is-drag-over, .gb-drop-above, .gb-drop-below, .gb-col-drop-hover').forEach(el => {
        el.classList.remove('gb-selected', 'is-selected', 'is-panning', 'is-drag-over', 'gb-drop-above', 'gb-drop-below', 'gb-col-drop-hover');
      });
      return root;
    }

    function getCleanWrapperHtml() {
      const cw = document.querySelector('.catalog-wrapper');
      if (!cw) return '';
      const clone = cleanCloneNode(cw.cloneNode(true));
      return clone.innerHTML;
    }

    function updateUndoRedoButtons() {
      const btnUndo = document.getElementById('btn-undo');
      const btnRedo = document.getElementById('btn-redo');
      if (btnUndo) btnUndo.disabled = undoStack.length === 0;
      if (btnRedo) btnRedo.disabled = redoStack.length === 0;
    }

    function commitHistorySnapshot() {
      if (isRestoringHistory) return;
      const current = getCleanWrapperHtml();
      if (!current) return;
      if (lastCommittedSnapshot === null) {
        lastCommittedSnapshot = current;
        updateUndoRedoButtons();
        return;
      }
      if (current === lastCommittedSnapshot) return;
      undoStack.push(lastCommittedSnapshot);
      if (undoStack.length > MAX_HISTORY) undoStack.shift();
      redoStack = [];
      lastCommittedSnapshot = current;
      updateUndoRedoButtons();
    }

    function rehydrateEditorDom() {
      selectedBlock = null;
      if (isEditing) {
        editableTextSelectors.forEach(sel => {
          document.querySelectorAll(sel).forEach(el => {
            el.setAttribute('contenteditable', 'true');
            el.setAttribute('spellcheck', 'false');
          });
        });
        setupGutenbergBlocks();
        setupImageContainers();
      }
      renderInspectorForBlock(null);
    }

    function undoEdit() {
      if (undoStack.length === 0) {
        showToast('Nada para desfazer.');
        return;
      }
      clearTimeout(inputHistoryTimer);
      isRestoringHistory = true;
      try {
        const current = getCleanWrapperHtml();
        const prev = undoStack.pop();
        if (current) redoStack.push(current);
        const cw = document.querySelector('.catalog-wrapper');
        if (cw && prev !== undefined) {
          cw.innerHTML = prev;
          lastCommittedSnapshot = prev;
          rehydrateEditorDom();
          markDirty(true);
          showToast('↩️ Alteração desfeita!');
        }
      } finally {
        isRestoringHistory = false;
        updateUndoRedoButtons();
      }
    }

    function redoEdit() {
      if (redoStack.length === 0) {
        showToast('Nada para refazer.');
        return;
      }
      clearTimeout(inputHistoryTimer);
      isRestoringHistory = true;
      try {
        const current = getCleanWrapperHtml();
        const next = redoStack.pop();
        if (current) undoStack.push(current);
        const cw = document.querySelector('.catalog-wrapper');
        if (cw && next !== undefined) {
          cw.innerHTML = next;
          lastCommittedSnapshot = next;
          rehydrateEditorDom();
          markDirty(true);
          showToast('↪️ Alteração refeita!');
        }
      } finally {
        isRestoringHistory = false;
        updateUndoRedoButtons();
      }
    }

    function markDirty(skipHistory) {
      hasUnsavedChanges = true;
      const statusText = document.getElementById('editor-status-text');
      if (statusText) statusText.innerText = 'Modo Edição (● Alterações não salvas)';
      if (!skipHistory && !isRestoringHistory) {
        commitHistorySnapshot();
      }
      try {
        const cw = document.querySelector('.catalog-wrapper');
        if (cw) {
          localStorage.setItem(DRAFT_KEY, cw.innerHTML);
          localStorage.setItem(DRAFT_TIME_KEY, Date.now().toString());
        }
      } catch (e) {}
    }

    document.addEventListener('focusin', (e) => {
      if (isEditing && e.target && e.target.isContentEditable && lastCommittedSnapshot === null) {
        lastCommittedSnapshot = getCleanWrapperHtml();
      }
    });

    document.addEventListener('input', (e) => {
      if (isEditing && e.target.isContentEditable) {
        markDirty(true);
        clearTimeout(inputHistoryTimer);
        inputHistoryTimer = setTimeout(() => {
          commitHistorySnapshot();
        }, 350);
      }
    });

    async function saveCatalog() {
      const cleanHtml = getCleanDocumentHtml();
      try {
        const resp = await fetch('/api/save', {
          method: 'POST',
          headers: { 'Content-Type': 'text/html; charset=utf-8' },
          body: cleanHtml
        });
        if (resp.ok) {
          hasUnsavedChanges = false;
          showToast('✅ Catálogo salvo com sucesso (+ backup automático)!');
          updateSavedStatus();
          return;
        }
      } catch (e) {}

      downloadHtmlBackup(cleanHtml);
      hasUnsavedChanges = false;
      showToast('💾 Arquivo HTML baixado para sua pasta de Downloads!');
      updateSavedStatus();
    }

    function downloadHtmlBackup(customHtml) {
      const content = customHtml || getCleanDocumentHtml();
      const blob = new Blob([content], { type: 'text/html; charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'catalogo_completo.html';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }

    function getCleanDocumentHtml() {
      const clone = cleanCloneNode(document.documentElement.cloneNode(true));

      const body = clone.querySelector('body');
      if (body) {
        body.classList.remove('is-editing', 'inspector-open');
      }
      return '<!DOCTYPE html>\n' + clone.outerHTML;
    }

    function discardEdits() {
      if (confirm('Deseja descartar as alterações desta sessão e restaurar a versão salva do disco?')) {
        localStorage.removeItem(DRAFT_KEY);
        localStorage.removeItem(DRAFT_TIME_KEY);
        window.location.reload();
      }
    }

    function updateSavedStatus() {
      const statusText = document.getElementById('editor-status-text');
      if (statusText) statusText.innerText = isEditing ? 'Modo Edição Ativo (Tudo salvo)' : 'Modo Visualização (Salvo)';
    }

    function showToast(msg) {
      const toast = document.getElementById('editor-toast');
      if (!toast) return;
      toast.innerText = msg;
      toast.classList.add('show');
      clearTimeout(window._toastTimeout);
      window._toastTimeout = setTimeout(() => toast.classList.remove('show'), 3800);
    }

    window.addEventListener('keydown', (e) => {
      const mod = e.metaKey || e.ctrlKey;
      if (!mod) return;
      const key = e.key.toLowerCase();
      if (key === 's') {
        e.preventDefault();
        saveCatalog();
      } else if (isEditing && key === 'z' && !e.shiftKey) {
        e.preventDefault();
        undoEdit();
      } else if (isEditing && ((key === 'z' && e.shiftKey) || key === 'y')) {
        e.preventDefault();
        redoEdit();
      }
    });
  </script>"""
