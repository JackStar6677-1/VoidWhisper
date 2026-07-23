# VoidWhisper

![VoidWhisper banner](assets/voidwhisper-hero.svg)

**VoidWhisper** es una interfaz local de IA pensada para chat, roleplay, personajes editables y carga de modelos desde tu propio entorno. La idea es simple: una base oscura, elegante y potente, con gestión de modelos integrada directamente en el proyecto.

## Lo esencial

- Interfaz local con estética galáctica, oscura y cuidada.
- Support for personajes YAML editables.
- Presets de generación separados del personaje.
- Descarga directa de modelos y files desde Hugging Face.
- Backend híbrido: `Transformers`, `AirLLM` y `llama.cpp` cuando toca.
- Configuración persistente en `user_data/`.
- Exportación e importación de chats.
- Exportación e importación de personajes.
- Reintento y continuación de respuestas desde la vista de conversación.
- Editor de presets integrado.

## Vista General

```mermaid
flowchart LR
    U[Jack / Operador] --> UI[VoidWhisper UI]
    UI --> C[Personajes YAML]
    UI --> P[Presets YAML]
    UI --> M[Config de modelos]
    UI --> D[Descarga Hugging Face]
    D --> L[user_data/models/*.gguf]
    L --> B[llama.cpp]
    UI --> T[Transformers]
    UI --> A[AirLLM]
    B --> R[Respuesta local]
    T --> R
    A --> R
```

## Arquitectura

```mermaid
flowchart TB
    subgraph Frontend
        F1[Templates HTML]
        F2[Settings / Chat / Characters]
    end

    subgraph Core
        C1[app.py]
        C2[voidwhisper_store.py]
        C3[SQLite + SQLAlchemy]
    end

    subgraph Data
        D1[user_data/settings.yaml]
        D2[user_data/characters/*.yaml]
        D3[user_data/presets/*.yaml]
        D4[user_data/models/config-user.yaml]
        D5[user_data/models/*.gguf]
    end

    subgraph Runtime
        R1[Transformers]
        R2[AirLLM]
        R3[llama.cpp]
    end

    F1 --> C1
    F2 --> C1
    C1 --> C2
    C1 --> C3
    C1 --> D1
    C1 --> D2
    C1 --> D3
    C1 --> D4
    C1 --> D5
    C1 --> R1
    C1 --> R2
    C1 --> R3
```

## Flujo de uso

```mermaid
sequenceDiagram
    participant Jack
    participant UI as VoidWhisper UI
    participant Store as user_data
    participant Model as Backend local

    Jack->>UI: Abre chat o configuración
    UI->>Store: Lee personaje, preset y modelo
    Jack->>UI: Envía mensaje
    UI->>Model: Construye prompt y ejecuta inferencia
    Model-->>UI: Devuelve respuesta
    UI-->>Jack: Muestra salida final
```

## Estructura de datos

VoidWhisper organiza sus datos locales así:

- `user_data/characters/`
  - personajes editables en YAML
- `user_data/presets/`
  - parámetros de temperatura, top_p, min_p, repetición, etc.
- `user_data/models/config-user.yaml`
  - reglas locales por extensión o patrón
- `user_data/settings.yaml`
  - defaults persistentes del entorno

## Motor de inferencia

### 1. Transformers

Pensado para modelos compatibles con `AutoModelForCausalLM`, con soporte de cuantización y carga estándar.

### 2. AirLLM

Útil si quieres dividir la carga en bloques y sobrevivir con hardware más justo.

### 3. llama.cpp / GGUF

Se activa para files `.gguf` locales. Si quieres usarlo de verdad, instala la dependencia opcional:

```bash
pip install -r requirements-gguf.txt
```

## Carpeta de modelos

Desde la screen de configuración puedes:

- escribir un repo de Hugging Face
- indicar un `.gguf` local
- descargar un archivo suelto o un repo completo al directorio del proyecto
- elegir el modelo local activo desde un selector
- ver los modelos y folders locales detectados

Desde el panel principal también puedes:

- exportar un chat a JSON
- importar un chat exportado
- exportar un personaje a JSON
- importar un personaje desde JSON
- reintentar la última respuesta de la IA
- continuar la generación desde el último contexto

## Installation rápida

```bash
git clone https://github.com/JackStar6677-1/VoidWhisper.git
cd VoidWhisper
python -m venv void_env
.\void_env\Scripts\activate
pip install -r requirements.txt
```

Si quieres soporte GGUF:

```bash
pip install -r requirements-gguf.txt
```

## Inicio

- `RUN_VOIDWHISPER.bat`
- `launch_voidwhisper.bat`
- `CREATE_DESKTOP_SHORTCUT.bat`

## Lo que incluye el proyecto

- `app.py`: backend principal Flask
- `voidwhisper_store.py`: capa de persistencia YAML y utilidades
- `templates/`: interfaz web
- `user_data/`: personas, presets, config y modelos locales
- `assets/`: branding visual del repo

## Mapa rápido

```text
VoidWhisper/
├─ app.py
├─ voidwhisper_store.py
├─ assets/
│  └─ voidwhisper-hero.svg
├─ templates/
├─ user_data/
│  ├─ characters/
│  ├─ presets/
│  ├─ models/
│  └─ settings.yaml
└─ requirements*.txt
```

## Notas

- El archivo `config-user.yaml` permite afinar patrones de carga locales.
- Los modelos pesados no se versionan; solo la configuración base.
- La estética está pensada para un tono oscuro, morado y dorado, con sensación cósmica.

## License

MIT License.

<!-- Updated for 2026 active baseline maintenance -->
