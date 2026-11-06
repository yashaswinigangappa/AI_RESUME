@echo off
echo ========================================================
echo   Starting TalentAI FastAPI Backend (Port 8000)
echo ========================================================

REM Free port 8000 if occupied by dangling processes
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000 ^| findstr LISTENING') do (
    echo Freeing port 8000 from PID %%a...
    taskkill /f /pid %%a >nul 2>&1
)

cd backend
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
pause
