@echo off
:: =======================================
:: HERRAMIENTA DE REPARACION DE EMOJIS (WA)
:: =======================================
:: Las actualizaciones de Windows suelen corromper 
:: la FNTCACHE o desvincular los emojis.
:: =======================================

echo Deteniendo servicios de fuentes...
net stop fontcache
net stop fontcache3.0.0.0

echo.
echo Limpiando cachés corruptas...
del /A:S /Q "%windir%\System32\FNTCACHE.DAT" 2>nul
del /A:S /Q "%LOCALAPPDATA%\FontCache\*" 2>nul

echo.
echo Reiniciando servicios...
net start fontcache

echo.
echo Escaneando e instalando fuentes omitidas por Windows (SFC)...
sfc /scannow

echo.
echo ============================================================
echo [!] PROCESO COMPLETADO. Por favor, REINICIA TU LAPTOP. 
echo Si el problema de WhatsApp Desktop persiste tras reiniciar, 
echo actualiza la app de WhatsApp.
echo.
echo (Nota: En VoidWhisper los emojis ya los he reparado 
echo internamente forzando Noto Color Emoji sin reiniciar)
echo ============================================================
pause
