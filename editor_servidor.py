import urllib.parse
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servidor Local de Edição Visual em Tempo Real — Catálogo Assifarma 2026
=====================================================================
Permite editar visualmente todas as imagens, textos, alturas de máscaras,
zoom e posicionamento com salvamento automático direto no arquivo
`catalogo_completo.html`.

Como usar no Terminal:
    python3 editor_servidor.py
"""

import http.server
import socketserver
import webbrowser
import json
import base64
import sys
import re
from pathlib import Path

PORT = 8080
WORKSPACE_DIR = Path(__file__).resolve().parent
TARGET_FILE = WORKSPACE_DIR / "catalogo_completo.html"
USER_EDITS_FILE = WORKSPACE_DIR / "catalogo_edicoes_usuario.html"
BACKUP_DIR = WORKSPACE_DIR / "backups"
BACKUP_DIR.mkdir(parents=True, exist_ok=True)
UPLOAD_DIR = WORKSPACE_DIR / "imagens_ilustrativas"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class CatalogEditHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WORKSPACE_DIR), **kwargs)

    def translate_path(self, path):
        clean_path = urllib.parse.unquote(path)
        if clean_path.startswith("/Users/"):
            return clean_path
        return super().translate_path(path)

    def do_POST(self):
        if self.path == "/api/save":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")

            try:
                import datetime
                ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                # 1. Salvar no arquivo principal
                TARGET_FILE.write_text(body, encoding="utf-8")
                # 2. Salvar cópia permanente de edições do usuário
                USER_EDITS_FILE.write_text(body, encoding="utf-8")
                # 3. Salvar backup com carimbo de data/hora
                backup_path = BACKUP_DIR / f"catalogo_backup_{ts}.html"
                backup_path.write_text(body, encoding="utf-8")

                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(b'{"status": "ok", "message": "Arquivo catalogo_completo.html e backup salvos com sucesso!"}')
                print(f"[OK] Alterações gravadas em catalogo_completo.html e backup em {backup_path.name} ({len(body):,} bytes)")
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(f'{{"status": "error", "message": "{str(e)}"}}'.encode("utf-8"))
                print(f"[ERRO] Falha ao gravar arquivo: {e}")

        elif self.path == "/api/upload-image":
            content_length = int(self.headers.get("Content-Length", 0))
            raw_data = self.rfile.read(content_length).decode("utf-8")
            try:
                data = json.loads(raw_data)
                filename = data.get("filename", "custom_image.png")
                # Sanitizar nome
                filename = re.sub(r"[^a-zA-Z0-9_\-\.]", "_", filename)
                b64_content = data.get("data", "")
                if "," in b64_content:
                    b64_content = b64_content.split(",", 1)[1]

                img_bytes = base64.b64decode(b64_content)
                save_path = UPLOAD_DIR / filename
                save_path.write_bytes(img_bytes)

                rel_url = f"imagens_ilustrativas/{filename}"
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                resp = json.dumps({"status": "ok", "url": rel_url, "path": str(save_path)})
                self.wfile.write(resp.encode("utf-8"))
                print(f"[OK] Nova imagem salva em: {save_path} ({len(img_bytes):,} bytes)")
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(f'{{"status": "error", "message": "{str(e)}"}}'.encode("utf-8"))
                print(f"[ERRO] Falha no upload: {e}")
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


def run_server(port=PORT):
    socketserver.TCPServer.allow_reuse_address = True
    for p in range(port, port + 10):
        try:
            httpd = socketserver.TCPServer(("", p), CatalogEditHandler)
            url = f"http://localhost:{p}/catalogo_completo.html"
            print("=" * 64)
            print("🚀 SERVIDOR LOCAL DE EDICAO EM TEMPO REAL ATIVADO!")
            print(f"👉 Acesse no seu navegador: {url}")
            print("💡 Toda alteração visual (imagens, zoom, pan, textos) pode ser salva diretamente.")
            print("Pressione Ctrl+C para encerrar o servidor.")
            print("=" * 64)
            webbrowser.open(url)
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nServidor encerrado.")
            return
        except OSError:
            continue

    print(f"❌ Não foi possível abrir porta entre {port} e {port+10}")


if __name__ == "__main__":
    run_server()
