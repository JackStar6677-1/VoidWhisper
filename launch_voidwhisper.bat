@echo off
cd /d "%~dp0"
if not exist "void_env\Scripts\activate" (
    echo Virtual environment not found: void_env\Scripts\activate
    pause
    exit /b 1
)
call "void_env\Scripts\activate"
start "" "http://127.0.0.1:5000/"
python app.py
pause
