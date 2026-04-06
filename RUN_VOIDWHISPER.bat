@echo off
REM VoidWhisper - Iniciar aplicación local con IA
REM Este archivo ejecuta VoidWhisper automáticamente desde el escritorio

setlocal enabledelayedexpansion

REM Obtener la ruta del script
set "SCRIPT_DIR=%~dp0"

REM Verificar que estamos en el directorio correcto
if not exist "%SCRIPT_DIR%app.py" (
    color 4F
    cls
    echo.
    echo [ERROR] No se encontró app.py en %SCRIPT_DIR%
    echo Asegúrate de ejecutar este archivo desde la carpeta VoidWhisper.
    echo.
    pause
    exit /b 1
)

REM Limpiar pantalla
cls
color 0B

echo.
echo ========================================
echo   VOIDWHISPER - IA Local sin Censura
echo ========================================
echo.
echo [i] Iniciando aplicación...
echo.

REM Navegar al directorio
cd /d "%SCRIPT_DIR%"

REM Verificar si existe el entorno virtual
if not exist "void_env" (
    color 4F
    echo [ERROR] Entorno virtual no encontrado.
    echo Ejecuta primero: python -m venv void_env
    echo.
    pause
    exit /b 1
)

REM Activar entorno virtual e iniciar Flask
call void_env\Scripts\activate.bat

REM Mostrar información de inicio
echo [✓] Entorno virtual activado
echo [✓] Iniciando servidor Flask...
echo.
echo ========================================
echo   URLs de acceso:
echo   • Local:     http://127.0.0.1:5000
echo   • Red:       http://192.168.0.215:5000
echo ========================================
echo.
echo Abre tu navegador en cualquiera de las URLs superiores.
echo.
echo Presiona Ctrl+C en esta ventana para detener el servidor.
echo.

REM Esperar 2 segundos y abrir navegador automáticamente
timeout /t 2 /nobreak

REM Intentar abrir el navegador (funciona si está disponible)
start "" http://127.0.0.1:5000

REM Iniciar la aplicación Flask
python app.py

REM Si el programa termina, mostrar mensaje
color 4F
echo.
echo [!] VoidWhisper se ha detenido.
echo.
pause
