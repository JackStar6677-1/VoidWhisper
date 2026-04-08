# VoidWhisper - The Uncensored Core

**VoidWhisper** es una interfaz local de Inteligencia Artificial diseñada desde cero para correr nativamente en tu entorno privado ofreciendo rol y chat textual sin filtros. Con enfoque en estéticas oscuras premium (estilo Whatsapp-Glassmorphism), alta portabilidad, y optimización arquitectónica estricta para hardware limitadísimo (e.g., 2GB VRAM).

---

## ✨ Características Premium Frontend
El sistema incluye una interfaz gráfica moderna puramente orquestada en HTML/Vanilla CSS optimizada para inmersión rápida.
- **Glassmorphism UI**: Interfaz de "Una Sola Página" (SPA-like) con Sidebar permanente, efectos de cristal y sombras sutiles.
- **Live Terminal (LogCatcher)**: Monitoreo in-game. Puedes abrir una terminal emergente desde el navegador que "hackea" e intercepta `stdout/stderr` para ver en tiempo real cómo tu GPU carga el modelo.
- **Generación Asíncrona Robusta**: En lugar de bloquear tu conexión web esperando 10 minutos a que responda un modelo (generando desconexiones `ERR_CONNECTION_RESET`), VoidWhisper despacha hilos fantasma de Python (`threading.Thread`) y lanza peticiones silenciosas `fetch()` de JavaScript, manteniendo al navegador intacto indiferentemente del castigo de VRAM en backend.
- **Renderizado de Emojis Nativo**: Parche inyectado de "Noto Color Emoji" en caso de que Windows borre sus fuentes dinámicas interrumpiendo emotes en tu interfaz.

---

## 🧠 Motores Híbridos & Memoria Exhausta

El sistema ha sido refinado para no ahogar tu computadora y ahora posee **Dos Motores Inferenciales Conmutables en Vivo**:

### 1. Motor Estándar (Transformers + BitsAndBytes)
Usa `AutoModelForCausalLM` mapeado directamente al dispositivo.
- Soporta **4-Bit Quantization** nativa y Auto CPU-Offload para hardware con poca memoria (requiere 4.5GB+ VRAM compartida para 7B).

### 2. Motor AirLLM (Hardware Bypass)
Si tus restricciones son absolutas (ej. MX450 / 2GB VRAM pura sin swapping suficiente), puedes activar el **Motor AirLLM** desde Configuración.
- Emplea **paginación en bloques**: Fractura un modelo 7B en tu disco duro (SSD) y carga la inferencia *Capa por Capa* hacia la memoria RAM, eliminando por completo las limitaciones de VRAM. Lentitud esperable a cambio de no crashear con falta de CUDA Memory extrema.

> **Modelo por defecto actual**: `DavidAU/Llama-3.2-3B-Instruct-heretic-ablitered-uncensored`
> Se ha escalado a este modelo arquitectónico de 3B para garantizar una inferencia 100% cruda, rápida e impecable en computadoras de Low-End (2GB a 4GB VRAM).

---

## ⚡ Escalabilidad Informática (RTX 4060, 4080, 4090)

Si clonas este repositorio en una estación de trabajo potente (por ejemplo una RTX 4060 con **8 GB de VRAM** o superior):
1. **AirLLM es innecesario**: Ve a *Configuración* y desactiva el motor AirLLM. Un modelo de 7B-8B cuantizado en 4-bits apenas consume ~4.5 GB de VRAM, por lo que cargará entero instantáneamente.
2. **Carga Única y Memoria Global**: Tras enviar tu primer mensaje, la gráfica demorará unos segundos en mapear el modelo desde tu SSD NVMe a la memoria. Una vez arriba, todos tus mensajes posteriores tomarán **0 segundos en cargar**.
3. **Velocidad Terminal**: A partir del primer golpe, verás tu respuesta decodificarse a velocidades abismales (40 a 70 palabras por segundo) directamente frente a ti en el flujo de la consola o la burbuja.

### 🎭 Recomendaciones Absolutas: Modelos "Zero-Censorship" & Roleplay
Si tienes la VRAM para aguantar modelos locales, ve a *Configuración* en VoidWhisper y pega en la celda *Nombre del Modelo* cualquiera de estas bestias de Rol sin límites disponibles hoy en HuggingFace:

- **Tier 1: Supervivencia (Hasta 2GB VRAM - MX450)**
  - `DavidAU/Llama-3.2-3B-Instruct-heretic-ablitered-uncensored` *(Recomendado para correr rápido. Abliterado a la perfección)*
  - `DavidAU/Qwen2.5-1.5B-VibeThinker-heretic-uncensored-abliterated` *(Minúsculo pero muy coherente y frío lógicamente)*
- **Tier 2: Rendimiento Óptimo (8GB VRAM - RTX 4060)**
  - `cognitivecomputations/dolphin-2.9-llama3-8b` *(Perfección absoluta sin filtros, astuto)*
  - `Sao10K/L3-8B-Stheno-v3.2` *(Centrado un 100% puramente en Roleplay creativo e intenso)*
- **Tier 3: El Límite de Memoria Oculta (11B a 14B)**
  - `Naphula/MN-12B-Mag-Mell-R1-Uncensored` *(Merge especializado en roleplay múltiple sin filtros)*
  - `Sao10K/Fimbulvetr-11B-v2` *(Un gigante dormido. Una inmersión brutal de trama)*
- **Tier Dios: Monstruos de 24GB VRAM**
  - `cognitivecomputations/dolphin-2.9-mixtral-8x7b` *(La obra cumbre de la IA de código abierto)*

---

## 🚀 Instalación y Despliegue Rápido

1. Asegúrate de tener Python instalado y clona este repositorio:
   ```bash
   git clone https://github.com/JackStar6677-1/VoidWhisper.git
   cd VoidWhisper
   ```

2. Genera y activa el Sandbox/Entorno Virtual:
   ```bash
   python -m venv void_env
   .\void_env\Scripts\activate
   ```

3. Instala los cimientos (Transformers o AirLLM):
   ```bash
   pip install -r requirements.txt
   ```

### Iniciando (Un clic)
Hemos incluido un generador de Atajos directo a tu escritorio:
Ejecuta el script: `CREATE_DESKTOP_SHORTCUT.bat`

Luego solo debes hacer doble clic en el ícono de **VoidWhisper** en tu fondo de pantalla y se activará. Si los Emojis no renderizan bien, haz doble click en `REPARAR_EMOJIS_PC.bat`.

---

## 🧩 Modos de Uso

### Base de Datos Centralizada
La persistencia usa SQLite con trayectos absolutos definidos mágicamente e impulsada bajo el estándar SQLAlchemy 2.0+ (`db.session.get()`). 

### Gestión de Operadores & Identidades
Desde la Web UI puedes:
1. Crear "Plantillas" de Sistema para inyectar personalidades maestras.
2. Intervenir un chat alterando manualmente bloques de texto (Message Editar).
3. Switch en vivo de motor (Transformers normal a Async AirLLM).

---

## 📜 Licencia
Construído adaptativamente por Void. MIT License.
