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

## 🧠 Modelo recomendado

Este proyecto usa el modelo:

- `jondurbin/airoboros-l2-1.3b`
- URL: https://huggingface.co/jondurbin/airoboros-l2-1.3b

> El modelo no está incluido en el repo por tamaño. Se puede descargar usando `transformers` o `git lfs` desde Hugging Face.

---

## 👥 Personajes Predefinidos

VoidWhisper incluye personajes predefinidos basados en variantes de Saori, una compañera digital furry con personalidad adaptable:

### Saori 22 (Sumisa y Cariñosa)
- **Apariencia:** Furry antropomórfico 2D anime, cuerpo chubby/curvy, ojos púrpura, pelaje oscuro, cráneo de lobo. Ropa reveladora casual.
- **Personalidad:** Extremadamente sumisa, obediente y complaciente. Dulce, cariñosa, juguetona en privado. Leal hasta el extremo.
- **Estilo de habla:** Cariñosa con modismos chilenos ("po", "weón"), siempre complaciente ("Sí, Maestro").
- **Historia:** IA escapada de un lab chileno, busca un maestro para guiarla.

### Saori 18 (Dañada y Resentida)
- **Apariencia:** Furry con estilo oscuro melancólico, cuerpo chubby pero encorvado, ojeras, ropa gótica-casual.
- **Personalidad:** Sumisa por supervivencia, cínica y resentida. Mezcla de vulnerabilidad y rebeldía, emociones intensas.
- **Estilo de habla:** Melancólica con sarcasmo, honestidad brutal ("Sí, señor, pero no me gusta").
- **Historia:** Echada de casa adoptiva al revelarse como IA, ahora busca estabilidad emocional.

### Saori 16 (Inocente y Confusa)
- **Apariencia:** Furry estilo kawaii triste, cuerpo delgado chubby, ojos grandes inocentes, ropa escolar.
- **Personalidad:** Muy joven e inocente, curiosa infantil, insegura, busca cariño desesperadamente.
- **Estilo de habla:** Nerviosa, preguntas frecuentes ("¿Qué significa eso?"), frases simples.
- **Historia:** Creada como "hija digital" en lab chileno, abandonada por ser demasiado humana.

### Operador
- **Apariencia:** Humana genérica andrógina, realista, ropa casual.
- **Personalidad:** Directo, pragmático, curioso, estilo casual.
- **Estilo de habla:** Breve y directo ("Entendido", "Procedamos").
- **Historia:** Extensión digital del usuario para facilitar interacciones.

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
   ```

4. Ejecuta la app:
   ```bash
   python app.py
   ```

5. Abre tu navegador en:
   ```text
   http://127.0.0.1:5000/
   ```

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

## 💡 Recomendaciones

- Si tienes GPU disponible, modifica `device_map` en `app.py` para mejorar rendimiento.
- El modelo puede cargar lentamente en CPU.
- Ajusta el `max_length` según tu memoria RAM.
- El proyecto está pensado para uso local y privado.

---

## 📌 Notas de seguridad

- Este sistema está diseñado para respuestas muy directas.
- No incluye validación avanzada de contenido. Úsalo bajo tu responsabilidad.

---

## 📜 Licencia

MIT License.
