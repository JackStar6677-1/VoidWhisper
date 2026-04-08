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

> **Modelo por defecto**: `teknium/OpenHermes-2.5-Mistral-7B`
> Se descartó `mistralai/Mistral...` para garantizar 0% censura y descarga instantánea.

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
