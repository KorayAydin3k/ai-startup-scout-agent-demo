@echo off
REM Launch script for AI Startup Scouting Agent
REM This script starts the Streamlit web application

echo.
echo ========================================
echo  AI Startup Scouting Agent
echo ========================================
echo.
echo Starting web interface...
echo.

REM Check if venv exists
if not exist "venv\Scripts\python.exe" (
    echo Error: Virtual environment not found.
    echo Please run: pip install -r requirements.txt
    pause
    exit /b 1
)

REM Launch Streamlit
"venv\Scripts\python.exe" -m streamlit run app.py

pause
