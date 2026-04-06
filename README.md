# VoidWhisper

**VoidWhisper** es una interfaz local para conversar con un modelo de lenguaje en modo crudo, directo y sin filtros. Está diseñada para correr completamente en tu máquina, con personajes personalizables, múltiples chats y configuración completa desde la web.

---

## ✨ Características principales

- **Gestión completa de chats**
  - Crea, borra y resetea conversaciones.
  - Agrega notas de contexto a cada chat para controlar la narrativa.
- **Personajes 100% configurables**
  - Crea personajes nuevos desde cero.
  - Duplicar personajes existentes para modificarlos sin perder la base.
  - Edita el `system prompt` directamente desde la interfaz.
- **Control total del modelo**
  - Ajusta `model_name`, `temperature`, `top_p`, `max_length` y el prefijo no-limit desde la UI.
  - No hace falta tocar código para cambiar la experiencia.
- **Perfil de usuario persistente**
  - Guarda nombre, perfil, intereses y tono de usuario.
  - El modelo usa este perfil en cada conversación.
- **Almacenamiento local**
  - Base de datos SQLite para chats, personajes y ajustes.
  - Todo ocurre en tu PC.

---

## 🧠 Modelo de IA optimizado

VoidWhisper utiliza **Mistral-7B-Instruct** cuantizado a 4-bit con BitsAndBytes para máxima eficiencia:

- **Modelo:** `TheBloke/Mistral-7B-Instruct-v0.1-GGUF`
- **URL:** https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF
- **Tamaño descargado:** ~2.5 GB (después de quantización)
- **Requisitos VRAM:** Mínimo 2 GB (optimizado para hardware como NVIDIA MX450, laptops, etc.)
- **Características:**
  - Quantización 4-bit automática con BitsAndBytes
  - Sin censura, respuestas crudas y directas
  - Optimizado para inferencia rápida incluso en GPUs de baja potencia
  - Soporte para `device_map='auto'` para mejor distribución de memoria

### Optimizaciones implementadas:
- **BitsAndBytes 4-bit quantization:** Reduce VRAM un 75% mantiendo calidad
- **Low CPU memory usage:** Streaming eficiente de capas del modelo
- **Device mapping automático:** Distribuye el modelo entre CPU y GPU intelligentemente

### Hardware soportado:
- ✅ NVIDIA MX450, RTX 3050, RTX 4050 (laptops)
- ✅ Cualquier GPU con 2GB+ VRAM
- ✅ Procesadores Intel/AMD modernos (con CPU inference fallback)

> **Nota:** En la primera ejecución, el modelo se descargará (~2.5 GB) y se convertirá al formato cuantizado. Ten paciencia en esta primera carga.

---

## 🚀 Instalación rápida

1. Clona el repositorio:
   ```bash
   git clone https://github.com/JackStar6677-1/VoidWhisper.git
   cd VoidWhisper
   ```

2. Crea y activa el entorno virtual:
   ```bash
   python -m venv void_env
   .\void_env\Scripts\activate
   ```

3. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   pip install bitsandbytes transformers torch torchvision torchaudio
   ```

4. Ejecuta la app:
   ```bash
   python app.py
   ```

5. Abre tu navegador en:
   ```text
   http://tu_ip_local:5000/
   ```

   La app ahora corre en la red local. Para acceder desde otros dispositivos, usa la IP de tu máquina (ej: http://192.168.1.100:5000/).

   Usuario por defecto: admin, contraseña: admin123.

   Puedes registrar nuevos usuarios y recuperar contraseña via email.

---

## 🧩 Uso de la interfaz

### Crear un personaje

1. Ve a la sección `Personajes`.
2. Selecciona un personaje base para copiar su prompt si quieres partir de una plantilla.
3. Escribe un nombre y el `system prompt` del personaje.
4. Haz clic en `Crear Personaje`.

### Duplicar un personaje

- Usa el botón `Duplicar` en la lista de personajes.
- Luego edita la copia desde la UI.

### Crear un chat

1. Elige el personaje que quieras usar.
2. Escribe un nombre para el chat.
3. Agrega una nota de contexto o instrucción inicial para ese chat.
4. Crea el chat.

### Chatear

- Envía mensajes desde la ventana del chat.
- El sistema incluye toda la conversación previa y la nota de contexto para mantener el hilo.
- Puedes resetear el chat con `Resetear Chat` para empezar de nuevo sin eliminarlo.

### Ajustes del entorno

- Ve a `Configuración del entorno` desde la página principal o desde el chat.
- Cambia:
  - modelo usado
  - parámetros de generación
  - prompt de no-limit
  - datos del operador

---

## 🛠️ Estructura del proyecto

- `app.py` — aplicación Flask, lógica de chat, configuración y carga de modelo.
- `templates/` — interfaz web del proyecto.
- `templates/settings.html` — página de configuración.
- `voidwhisper.db` — base de datos SQLite creada automáticamente.
- `launch_voidwhisper.bat` — lanzador rápido para Windows.
- `requirements.txt` — dependencias.

---

## 💡 Optimización y Rendimiento

### Para hardware limitado (laptops, MX450, etc.)
- **Quantización está habilitada por defecto (4-bit)** en configuración
- Usa `device_map='auto'` para balance automático entre GPU/CPU
- Reduce `max_length` (300 caracteres es el default, puedes bajar a 200)
- Si el modelo va lento, es normal en primera carga o GPU débil

### Para sistemas potentes
- Cambia quantización a '8bit' en `settings.html` para mejor calidad
- O desactiva quantización completamente si tienes >8 GB VRAM
- Aumenta `temperature` (actualmente 0.8) para respuestas más creativas
- Reduce `top_p` (actualmente 0.9) para respuestas más coherentes

### En configuración del entorno:
```
model_name: TheBloke/Mistral-7B-Instruct-v0.1-GGUF  (cambiar si quieres otro modelo)
use_quantization: 4bit  (opciones: 'false', '4bit', '8bit')
temperature: 0.8  (0.0 = determinista, 2.0 = muy aleatorio)
top_p: 0.9  (0.5 = conservador, 0.99 = muy creativo)
max_length: 300  (caracteres máximo de respuesta)
```

### Modelos alternativos compatibles:
- `teknium/OpenHermes-2.5-Mistral-7B` (más pequeño, más rápido)
- `NousResearch/Hermes-2-Theta-Llama-3-8B` (mejor instrucción)
- `meta-llama/Llama-2-7b-chat-hf` (precisa token de HuggingFace)

---

## 🚰 Troubleshooting

### "CUDA out of memory"
- Baja `max_length` a 200
- Cambia quantización de '8bit' a '4bit'
- Reduce `batch_size` si estás procesando máltiples mensajes

### Modelo carga muy lento
- Normal en primera ejecución (descarga ~2.5 GB)
- En CPUs débiles: es lento por naturaleza, ten paciencia
- GPU débil (MX450): espera 30-60 segundos por respuesta

### "Model not found" en HuggingFace
- Comprueba tu token HF: `huggingface-cli login`
- Algunos modelos son privados, necesitan solicitud de acceso

### La app no inicia
- Comprueba que Puerto 5000 no esté en uso: `netstat -ano | findstr :5000`
- Mata procesos viejos: `taskkill /F /IM python.exe`
- Recrea el venv: `python -m venv void_env && .\void_env\Scripts\activate`

---

## 💡 Tips generales

- **Chat multi-dispositivo:** Accede desde cualquier dispositivo en tu red con la IP de tu PC
- **Personalización:** Crea personajes con prompts detallados para mejores respuestas
- **Notas de contexto:** Úsalas para guiar al modelo sobre el tema de la conversación
- **Resetear chat:** Borra solo esa conversación, no tus personajes
- **Exportar resultados:** Copia-pega desde el navegador para guardar chats
- **Privacidad total:** Todo ocurre localmente, nada se envía a servidores
- **Test rápido:** Primero prueba con personaje "Operador" para versiones técnicas

---

## 📌 Notas de seguridad

- Este sistema está diseñado para respuestas muy directas.
- No incluye validación avanzada de contenido. Úsalo bajo tu responsabilidad.

---

## 📜 Licencia

MIT License.
