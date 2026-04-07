@echo off
REM Script para crear un atajo de VoidWhisper en el Escritorio

setlocal enabledelayedexpansion

REM Obtener rutas
set "SCRIPT_DIR=%~dp0"
set "DESKTOP=%USERPROFILE%\Desktop"
set "BATCH_FILE=%SCRIPT_DIR%RUN_VOIDWHISPER.bat"
set "SHORTCUT_FILE=%DESKTOP%\VoidWhisper.lnk"

REM Verificar que el archivo batch existe
if not exist "%BATCH_FILE%" (
    cls
    color 4F
    echo.
    echo [ERROR] No se encontró RUN_VOIDWHISPER.bat
    echo Ruta esperada: %BATCH_FILE%
    echo.
    pause
    exit /b 1
)

cls
echo.
echo Creando atajo en el escritorio...
echo Ruta: %SHORTCUT_FILE%
echo.

REM Crear una archivo VBScript temporal para crear el acceso directo
(
@echo Set WshShell = CreateObject("WScript.Shell")
@echo Set Shortcut = WshShell.CreateShortCut("%SHORTCUT_FILE%")
@echo Shortcut.TargetPath = "%BATCH_FILE%"
@echo Shortcut.WorkingDirectory = "%SCRIPT_DIR%"
@echo Shortcut.Description = "VoidWhisper - Chat con IA sin censura"
@echo Shortcut.IconLocation = "C:\Windows\System32\cmd.exe,0"
@echo Shortcut.Save
) > create_shortcut.vbs

REM Ejecutar el script VBScript
cscript.exe create_shortcut.vbs

REM Limpiar archivo temporal
del create_shortcut.vbs

echo.
echo [OK] Atajo creado exitosamente!
echo [✓] Busca "VoidWhisper" en tu escritorio
echo [✓] Haz doble clic para iniciar la aplicación
echo [✓] Se abrirá automáticamente en tu navegador
echo.
pause

