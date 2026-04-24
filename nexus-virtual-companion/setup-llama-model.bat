@echo off
REM Nexus Virtual Companion - Llama Model Setup Script
REM This script pulls the Llama model from Ollama

echo.
echo ========================================
echo Nexus Virtual Companion - Model Setup
echo ========================================
echo.

REM Check if Ollama is installed
where ollama >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Ollama is not installed or not in PATH
    echo Please install Ollama first: https://ollama.ai
    echo.
    pause
    exit /b 1
)

echo [OK] Ollama found
ollama --version
echo.

REM Check if Ollama service is running
echo Checking if Ollama service is running...
tasklist | find /i "ollama" >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [WARNING] Ollama service not running
    echo Starting Ollama service...
    start cmd /k ollama serve
    timeout /t 5 /nobreak
) else (
    echo [OK] Ollama service is running
)

echo.
echo Available models:
echo 1) Mistral (RECOMMENDED - Fast, 7B params, 4GB)
echo 2) Llama2 (Capable, 7B params, 4GB)
echo 3) Llama2 13B (More powerful, 13B params, 8GB)
echo 4) Neural-Chat (Optimized for conversation, 7B params, 4GB)
echo.

set /p choice="Select model to download (1-4): "

if "%choice%"=="1" (
    echo Pulling Mistral model...
    ollama pull mistral
    set model_name=mistral
) else if "%choice%"=="2" (
    echo Pulling Llama2 7B model...
    ollama pull llama2
    set model_name=llama2
) else if "%choice%"=="3" (
    echo Pulling Llama2 13B model...
    echo [NOTE] This requires ~8GB storage space
    ollama pull llama2:13b
    set model_name=llama2:13b
) else if "%choice%"=="4" (
    echo Pulling Neural-Chat model...
    ollama pull neural-chat
    set model_name=neural-chat
) else (
    echo [ERROR] Invalid choice. Using Mistral as default.
    ollama pull mistral
    set model_name=mistral
)

echo.
echo ========================================
echo Model Downloaded Successfully!
echo ========================================
echo.
echo Next steps:
echo 1. Update .env file: LLAMA_MODEL=%model_name%
echo 2. Start the Flask app: python app.py
echo 3. Chat with your AI companion!
echo.
echo [TIP] Ollama will continue running in the background
echo [TIP] First conversation takes 1-2 minutes (model loads to memory)
echo.

ollama list

echo.
pause
