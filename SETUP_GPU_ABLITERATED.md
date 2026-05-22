# VoidWhisper — GPU + modelos abliterated (RTX 4060, 8 GB)

## Estado en este PC

- **GPU:** NVIDIA GeForce RTX 4060 (8 GB)
- **PyTorch:** `2.6.0+cu124` (CUDA activa)
- **llama.cpp:** requiere que las DLL de `torch/lib` estén en el PATH (ya aplicado en `app.py`)

## Arranque rápido

```powershell
cd C:\Users\pablo\Documentos\GitHub\VoidWhisper
.\void_env\Scripts\activate
python download_abliterated_model.py
.\RUN_VOIDWHISPER.bat
```

Abre `http://127.0.0.1:5000` → **Ajustes** → confirma modelo y **GPU Layers: -1**.

## Modelo recomendado (abliterated, 8 GB VRAM)

| Prioridad | Repo Hugging Face | Archivo | Backend |
|-----------|-------------------|---------|---------|
| **1 (recomendado)** | `DavidAU/L3.2-Rogue-Creative-Instruct-Uncensored-Abliterated-7B-GGUF` | `L3.2-Rogue-Creative-Instruct-Uncensored-Abliterated-7B-D_AU-Q4_k_m.gguf` | llama.cpp + GPU |
| 2 (más ligero) | `huihui-ai/Qwen2.5-1.5B-Instruct-abliterated-SFT` | repo completo | Transformers + GPU |
| 3 (roleplay 8B) | `failspy/Meta-Llama-3-8B-Instruct-abliterated-v3` | safetensors / GGUF si existe | Transformers o GGUF |

Más opciones documentadas en `INVESTIGACION_ROLEPLAY.md`.

## Sin censura (3 capas)

1. **Modelo abliterated** — refusals eliminados a nivel de pesos.
2. **`no_limit_prefix`** en Ajustes — inyección de system prompt sin filtros (ya en `user_data/settings.yaml`).
3. **Personaje** — evita frases tipo “no puedo ayudar con eso” en el YAML del personaje.

## Descarga desde la UI

En **Ajustes → Descargar modelo**:

- **Repo:** `DavidAU/L3.2-Rogue-Creative-Instruct-Uncensored-Abliterated-7B-GGUF`
- **Archivo:** `L3.2-Rogue-Creative-Instruct-Uncensored-Abliterated-7B-D_AU-Q4_k_m.gguf`

## Verificar GPU

```powershell
.\void_env\Scripts\python.exe check_gpu.py
```

Debe mostrar `CUDA available: True` y tu RTX 4060.

## Si llama.cpp no carga

1. Reinstalar: `pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu124`
2. Instalar [Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)
3. Usar modelo Transformers abliterated 1.5B mientras tanto.
