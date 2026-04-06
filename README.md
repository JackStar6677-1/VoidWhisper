# VoidWhisper

Un entorno local para chatear con modelos de lenguaje sin censura, con personajes personalizables y gestión de chats. Diseñado para privacidad total y uso local.

## Características

- **Chats Múltiples**: Crea, gestiona y borra conversaciones independientes.
- **Personajes Personalizables**: Crea y edita personajes con prompts del sistema. Incluye personajes predefinidos como Saori Sumisa y Jack.
- **Interfaz Web Royal**: Diseño elegante en morado y dorado.
- **Almacenamiento Local**: Usa SQLite para persistir chats, personajes y perfil de usuario.
- **Modelo Uncensored**: Basado en jondurbin/airoboros-l2-1.3b, sin filtros éticos.
- **Privacidad**: Todo corre localmente, sin envío de datos a servidores externos.

## Requisitos

- Python 3.8+
- Git
- GitHub CLI (`gh`) autenticado

## Instalación

1. Clona o descarga el repo:
   ```
   git clone https://github.com/JackStar6677-1/VoidWhisper.git
   cd VoidWhisper
   ```

2. Crea un entorno virtual:
   ```
   python -m venv void_env
   .\void_env\Scripts\activate  # Windows
   ```

3. Instala dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Descarga el modelo (no incluido en el repo por tamaño):
   - Ve a [Hugging Face: jondurbin/airoboros-l2-1.3b](https://huggingface.co/jondurbin/airoboros-l2-1.3b)
   - Descarga los archivos del modelo (usa `git lfs` si es necesario).
   - Coloca los archivos en una carpeta accesible, o deja que Transformers los descargue automáticamente al ejecutar.

## Uso

1. Ejecuta la app:
   ```
   python app.py
   ```

2. Abre tu navegador en `http://127.0.0.1:5000/`.

3. **Crear un Personaje**:
   - En la página principal, ve a la sección "Personajes".
   - Llena el formulario: Nombre y System Prompt (describe personalidad, apariencia, etc.).
   - Ejemplo: "Eres un guerrero vikingo malvado, responde agresivamente."
   - Haz clic en "Crear Personaje".

4. **Crear un Chat**:
   - Selecciona un personaje de la lista.
   - Ingresa un nombre para el chat.
   - Haz clic en "Crear Chat".

5. **Chatear**:
   - En la página del chat, escribe mensajes y envía.
   - El modelo responde como el personaje seleccionado, conociendo tu perfil.

6. **Editar/Borrar**:
   - Usa los botones en la lista de chats/personajes.

## Estructura del Proyecto

- `app.py`: Servidor Flask con lógica de DB y modelo.
- `templates/`: HTML para interfaz.
- `voidwhisper.db`: Base de datos SQLite (creada al ejecutar).
- `requirements.txt`: Dependencias.

## Notas

- El modelo se carga al iniciar la app (puede tomar tiempo en CPU).
- Si tienes GPU, ajusta `device_map` en `app.py`.
- Personajes predefinidos: Saori Sumisa (sumisa, furry) y Jack (tú mismo, basado en tu perfil).
- La UI permite crear personajes sin IDE: todo via web.

## Licencia

MIT - Usa bajo tu responsabilidad.

## Notas
- Usa CPU debido a limitaciones de VRAM. Si tienes más VRAM, puedes cambiar a GPU editando el script.
- El modelo es uncensored: no tiene filtros éticos, responde a cualquier tema.
- Para modelos más grandes, considera usar Ollama o LM Studio con quants optimizados.

## Notas
- Usa CPU debido a limitaciones de VRAM. Si tienes más VRAM, puedes cambiar a GPU editando el script.
- El modelo es uncensored: no tiene filtros éticos, responde a cualquier tema.
- Para modelos más grandes, considera usar Ollama o LM Studio con quants optimizados.