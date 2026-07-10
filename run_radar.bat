@echo off

cd /d D:\crypto\binance-futures-ai-radar

powershell -ExecutionPolicy Bypass -Command ".\.venv\Scripts\Activate.ps1; streamlit run app.py"

pause