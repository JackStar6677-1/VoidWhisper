# VoidWhisper - The Uncensored Core

**VoidWhisper** es una interfaz local de Inteligencia Artificial diseñada desde cero para correr nativamente en tu entorno privado ofreciendo rol y chat textual sin filtros. Con enfoque en estéticas oscuras (Glassmorphism), alta portabilidad, y optimización estricta de memoria para permitir la ejecución de modelos potentes en hardware casero moderado.

---

## ✨ Características Premium Frontend
El sistema incluye una interfaz gráfica moderna puramente orquestada en HTML/Vanilla CSS optimizada para inmersión rápida.
- **Glassmorphism UI**: Efectos de cristales, tarjetas flotantes, y sombras sutiles.
- **Responsive Bubbles**: Chat dinámico inspirado en apps de mensajería (identidad visual para la IA y para el usuario).
- **Indicador de Pensamiento**: Efectos asincrónicos mientras la terminal procesa.
- **Hotbar Unificada**: Navegación de una sola página sin recargar innecesariamente estilos redundantes gracias a `base.html` con Jinja2.

---

## 🧠 Arquitectura de IA & Optimizaciones (Hardware Limitado)

El sistema carga modelos causal-LM usando `transformers` y `bitsandbytes`. 
Para evitar ahogar tu tarjeta gráfica (probado en entornos de VRAM modesta como NVIDIA MX450 / 2GB) se aplica por defecto:

1. **4-Bit Quantization**: El modelo se carga en memoria dividiendo su dimensión original mediante quantización hiper-optimizada.
2. **Auto CPU-Offload**: Integrado nativamente en el `BitsAndBytesConfig`, lo que significa que de faltar VRAM, las siguientes redes neuronales *se delegaran automáticamente* a la memoria RAM regular (CPU) para eludir el clásico error `CUDA out of memory`.

> **Modelo por defecto**: `teknium/OpenHermes-2.5-Mistral-7B`
Se descartó `mistralai/Mistral...` base porque HuggingFace introdujo candados (*Gated Repo*). Hemos transitado a una variante OpenHermes para 0% censura, 100% público, lo que acelera su descarga instantánea.

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

3. Instala los cimientos y Transformers:
   ```bash
   pip install -r requirements.txt
   ```

### Iniciando (Un clic)
Hemos incluido un generador de Atajos directo a tu escritorio:
Ejecuta el script: `CREATE_DESKTOP_SHORTCUT.bat`

Luego solo debes hacer doble clic en el ícono de **VoidWhisper** en tu fondo de pantalla y se activará localmente el motor de generación.
> **NOTA INICIAL:** En tu primer uso (si nunca has usado OpenHermes), el sistema lo bajará en ~30s-1min a la caché privada (`~/.cache/huggingface`).

---

## 🧩 Modos de Uso

### Base de Datos Central Local
La base de datos se orquesta en `voidwhisper.db` basada en SQLite (se migró toda la sintaxis al estándar moderno de SQLAlchemy 2.0+). 

### Gestión de Operadores & Identidades
Desde la Web UI puedes:
1. Crear "Plantillas" de Sistema para inyectar personalidades únicas.
2. Intervenir un chat modificando los mensajes de la IA para corregir el rumbo (Bypass).
3. Escribir formato de rol (`*suspiro*`) o susurros (`_hablando bajo_`). El frontend lo pintará diferente de los mensajes de sistema normal.

---

## 📜 Licencia
Dominio y código adaptado de libre uso. Construído sobre Mistral, adaptado por Void. MIT License.
