"""
Descarga el modelo abliterated recomendado para RTX 4060 (8 GB VRAM).
GGUF Q4_K_M (~4.5 GB) + backend llama.cpp con GPU.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from voidwhisper_store import MODEL_DIR, download_hf_asset

REPO_ID = "DavidAU/L3.2-Rogue-Creative-Instruct-Uncensored-Abliterated-7B-GGUF"
GGUF_FILE = "L3.2-Rogue-Creative-Instruct-Uncensored-Abliterated-7B-D_AU-Q4_k_m.gguf"


def main() -> int:
    try:
        print(f"[INFO] Destino: {MODEL_DIR}")
        print(f"[INFO] Descargando {REPO_ID} / {GGUF_FILE}")
        print("[INFO] Tamaño aproximado: 4.5 GB. Puede tardar varios minutos.")
        path = download_hf_asset(REPO_ID, GGUF_FILE, MODEL_DIR)
        print(f"[SUCCESS] Modelo listo en: {path}")
        print(f"[INFO] Activa en Ajustes: {path.name}")
        return 0
    except Exception as exc:
        print(f"[ERROR] Falló la descarga: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
