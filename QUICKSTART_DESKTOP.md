# 🚀 Guía Rápida - Iniciar VoidWhisper desde el Escritorio

## Opción 1: Crear Atajo Automático (Recomendado)

1. Abre PowerShell como Administrador (Windows + X, luego 'A')
2. Navega al directorio de VoidWhisper:
   ```powershell
   cd C:\Users\Jack\Documents\GitHub\Experimentos\VoidWhisper
   ```

3. Ejecuta el script que crea el atajo:
   ```powershell
   .\CREATE_DESKTOP_SHORTCUT.bat
   ```

4. ¡Listo! Busca "VoidWhisper" en tu escritorio y haz doble clic para iniciar.

## Opción 2: Crear Atajo Manualmente

1. Haz clic derecho en el escritorio → Nuevo → Acceso directo
2. En la ubicación del elemento, pega:
   ```
   C:\Users\Jack\Documents\GitHub\Experimentos\VoidWhisper\RUN_VOIDWHISPER.bat
   ```
3. Dale el nombre "VoidWhisper"
4. Haz clic en Finalizar

## Opción 3: Uso Directo desde Línea de Comandos

Simplemente doble-clic en `RUN_VOIDWHISPER.bat` en la carpeta VoidWhisper.

---

## ¿Qué sucede cuando inicia?

El archivo `RUN_VOIDWHISPER.bat` automáticamente:
- ✅ Activa el entorno virtual Python
- ✅ Inicia el servidor Flask en `http://127.0.0.1:5000`
- ✅ Abre tu navegador automáticamente
- ✅ Muestra instrucciones en la terminal

## Acceso desde otros dispositivos

Una vez iniciado, puedes acceder desde otros dispositivos usando:
- **PC actual:** `http://127.0.0.1:5000`
- **Otra PC en red:** `http://192.168.0.215:5000` (o tu IP local)

## Detener la aplicación

Presiona `Ctrl+C` en la ventana negra del terminal para detener VoidWhisper.

## Troubleshooting Rápido

| Problema | Solución |
|----------|----------|
| "No se encontró app.py" | Asegúrate de ejecutar desde la carpeta VoidWhisper |
| "Entorno virtual no encontrado" | Crea con: `python -m venv void_env` |
| Puerto 5000 en uso | `taskkill /F /IM python.exe` |
| Navegador no abre | Abre manualmente `http://127.0.0.1:5000` |

---

**¡Listo! Ahora tienes una forma simple y rápida de iniciar VoidWhisper desde el escritorio.**
