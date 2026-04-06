@echo off
REM Script para crear un atajo de VoidWhisper en el Escritorio

setlocal enabledelayedexpansion

REM Obtener rutas
set "SCRIPT_DIR=%~dp0"
set "DESKTOP=%USERPROFILE%\Desktop"
set "BATCH_FILE=%SCRIPT_DIR%RUN_VOIDWHISPER.bat"

REM Verificar que el archivo batch existe
if not exist "%BATCH_FILE%" (
    echo [ERROR] No se encontró RUN_VOIDWHISPER.bat
    pause
    exit /b 1
)

cls
echo.
echo Creando atajo en el escritorio...
echo.

REM Crear atajo usando PowerShell (más confiable que VBScript en Win10+)
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    "$WshShell = New-Object -ComObject WScript.Shell; ^
    $Shortcut = $WshShell.CreateShortCut('%DESKTOP%\VoidWhisper.lnk'); ^
    $Shortcut.TargetPath = '%BATCH_FILE%'; ^
    $Shortcut.WorkingDirectory = '%SCRIPT_DIR%'; ^
    $Shortcut.Description = 'VoidWhisper - Chat con IA sin censura'; ^
    $Shortcut.IconLocation = 'C:\Windows\System32\cmd.exe,0'; ^
    $Shortcut.Save(); ^
    Write-Host '[OK] Atajo creado en Escritorio'"

echo.
echo [✓] Atajo creado exitosamente!
echo [✓] Busca "VoidWhisper" en tu escritorio
echo.
pause
