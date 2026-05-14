@echo off
echo ========================================
echo AI Interview Preparation System
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created.
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if .env exists
if not exist ".env" (
    echo Creating .env file...
    copy .env.example .env
    echo.
    echo IMPORTANT: Please add your Groq API key to the .env file
    echo Get your API key from: https://console.groq.com/
    echo.
    pause
)

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Run migrations
echo.
echo Running database migrations...
python manage.py makemigrations
python manage.py migrate

REM Start server
echo.
echo ========================================
echo Starting development server...
echo Open your browser to: http://127.0.0.1:8000/
echo Press Ctrl+C to stop the server
echo ========================================
echo.
python manage.py runserver
