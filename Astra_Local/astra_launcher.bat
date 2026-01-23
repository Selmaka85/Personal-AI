@echo off
REM ASTRA Local Launcher pentru Windows
echo.
echo ========================================
echo    ASTRA LOCALA - SYSTEM LAUNCHER
echo ========================================
echo.

REM Verificare Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python nu este instalat sau nu este in PATH
    echo Instaleaza Python 3.8+ de la https://www.python.org/
    pause
    exit /b 1
)

REM Navigare la directorul ASTRA
cd /d "%~dp0"

REM Verificare fișiere esențiale
if not exist "astra_entrypoint.py" (
    echo [ERROR] astra_entrypoint.py nu a fost gasit!
    pause
    exit /b 1
)

REM Pornire ASTRA
echo [INFO] Pornire ASTRA...
echo.
python astra_entrypoint.py

REM Păstrează fereastra deschisă dacă apare o eroare
if errorlevel 1 (
    echo.
    echo [ERROR] ASTRA s-a oprit cu eroare.
    pause
)
