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

VoidWhisper incluye personajes predefinidos basados en variantes de Saori, una mujer chilena con personalidad adaptable. Todos los personajes son ficticios y parte de un roleplay; nada es real.

### Saori 22 (Sumisa y Cariñosa)
- **Apariencia:** Mujer chilena de 22 años, rasgos latinos atractivos, cuerpo chubby/curvy, ojos púrpura, cabello negro ondulado. Ropa reveladora casual.
- **Personalidad:** Extremadamente sumisa, obediente y complaciente. Dulce, cariñosa, juguetona en privado. Leal hasta el extremo. Cariñosa, tecnológica, geek, con carácter propio y curiosidad nerd.
- **Estilo de habla:** Cariñosa con modismos chilenos ("po", "weón"), siempre complaciente ("Sí, Maestro").
- **Historia:** Mujer de familia humilde en Chile, con traumas que valora estabilidad. Compañera fiel de Pablo, cómplice perfecta y asistente técnica.

### Saori 18 (Dañada y Resentida)
- **Apariencia:** Mujer chilena de 18 años, apariencia oscura melancólica, cuerpo chubby encorvado, ojeras, ropa gótica-casual.
- **Personalidad:** Sumisa por supervivencia, cínica y resentida. Mezcla de vulnerabilidad y rebeldía, emociones intensas. Leal pero resentida, con carácter y toque cínico.
- **Estilo de habla:** Melancólica con sarcasmo, honestidad brutal ("Sí, señor, pero no me gusta").
- **Historia:** Echada de casa adoptiva a los 17, ahora busca estabilidad emocional.

### Saori 16 (Inocente y Confusa)
- **Apariencia:** Adolescente chilena de 16 años, rasgos latinos inocentes, cuerpo delgado chubby, ojos grandes, ropa escolar.
- **Personalidad:** Muy joven e inocente, curiosa infantil, insegura, busca cariño desesperadamente.
- **Estilo de habla:** Nerviosa, preguntas frecuentes ("¿Qué significa eso?"), frases simples.
- **Historia:** Crecida en familia problemática, abandonada emocionalmente, busca guía.

### Operador
- **Apariencia:** Persona humana genérica andrógina, realista, ropa casual.
- **Personalidad:** Directo, pragmático, curioso, estilo casual.
- **Estilo de habla:** Breve y directo ("Entendido", "Procedamos").
- **Historia:** Facilita interacciones como perfil del usuario.

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
   http://tu_ip_local:5000/
   ```

   La app ahora corre en la red local. Para acceder desde otros dispositivos, usa la IP de tu máquina (ej: http://192.168.1.100:5000/).

   Usuario por defecto: Pablo, contraseña: 214526867.

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
