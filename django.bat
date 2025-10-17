@echo off
title Django Portable Environment v2.6 (EN/中文)
setlocal enabledelayedexpansion

REM === 取得啟動器所在磁碟 (不管是 E:\ F:\ G:\) ===
set "BASE=%~d0"

REM === 設定 Python 與 Django 專案路徑 ===
set "PYTHON=%BASE%\Python\python.exe"
set "PROJECT_DIR=%BASE%\mydjango"
set "VENV_DIR=%PROJECT_DIR%\venv"

echo ==================================================
echo [*] 可攜式 Python + Django 啟動器 v2.6 (EN/中文)
echo Portable Python + Django Launcher
echo 啟動器磁碟 (Base Drive): %BASE%
echo Python 位置 (Python Path): %PYTHON%
echo 專案路徑 (Project Path): %PROJECT_DIR%
echo ==================================================

REM === 檢查 Python 是否存在 ===
if not exist "%PYTHON%" (
    echo [!] 找不到 Python / Python not found: %PYTHON%
    echo 請確認 Python 資料夾與啟動器在同一層 / Make sure Python folder is next to launcher.
    pause
    exit /b
)

REM === 檢查虛擬環境是否存在，若沒有則建立 ===
if not exist "%VENV_DIR%" (
    echo [*] 建立虛擬環境... / Creating virtual environment...
    "%PYTHON%" -m venv "%VENV_DIR%"
    echo [?] 虛擬環境建立完成！ / Virtual environment created!
)

REM === 啟動虛擬環境 ===
call "%VENV_DIR%\Scripts\activate.bat"

:MENU
cls
echo ==================================================
echo [1] 啟動 Django 伺服器（自動尋找可用 Port） / Start Django server (auto port)
echo [2] 只進入虛擬環境 (命令列模式) / Enter virtual environment (CLI)
echo [3] 安裝 requirements.txt 套件 / Install requirements.txt packages
echo [4] 執行 makemigrations + migrate / Run makemigrations + migrate
echo [5] 自動安裝 Django / Install Django
echo [6] 離開 / Exit
echo ==================================================
set /p choice=請輸入選項 (1-6) / Please select option (1-6): 

if "%choice%"=="1" goto STARTSERVER
if "%choice%"=="2" goto ENTERVENV
if "%choice%"=="3" goto INSTALLREQ
if "%choice%"=="4" goto MIGRATE
if "%choice%"=="5" goto INSTALLDJANGO
if "%choice%"=="6" goto END
echo [!] 無效的選項 / Invalid option. Please try again.
pause
goto MENU

:STARTSERVER
cd /d "%PROJECT_DIR%"
REM === 預設 port ===
set "PORT=8000"

:CHECKPORT
netstat -ano | findstr :%PORT% >nul
if %errorlevel%==0 (
    echo [!] Port %PORT% 已被佔用，嘗試使用下一個... / Port %PORT% in use, trying next...
    set /a PORT=%PORT%+1
    goto CHECKPORT
)

echo [*] 啟動 Django 伺服器 (http://127.0.0.1:%PORT%) / Starting Django server...
start http://127.0.0.1:%PORT%
python manage.py runserver 127.0.0.1:%PORT%
pause
goto MENU

:ENTERVENV
echo [*] 你現在已進入虛擬環境，可以手動輸入指令。
echo [提示] 輸入 exit 可返回啟動器選單。
echo [*] You are now inside the virtual environment.
echo [Tip] Type 'exit' to return to menu.
cmd
goto MENU

:INSTALLREQ
cd /d "%PROJECT_DIR%"
if exist requirements.txt (
    echo [*] 偵測到 requirements.txt，開始安裝套件...
    echo [*] requirements.txt detected. Installing packages...
    pip install -r requirements.txt
    echo [?] 安裝完成 / Installation complete!
) else (
    echo [!] 沒找到 requirements.txt / File not found.
)
pause
goto MENU

:MIGRATE
cd /d "%PROJECT_DIR%"
echo [*] 執行 makemigrations... / Running makemigrations...
python manage.py makemigrations
echo [*] 執行 migrate... / Running migrate...
python manage.py migrate
echo [?] 資料庫遷移完成！ / Database migration complete!
pause
goto MENU

:INSTALLDJANGO
echo [*] 開始安裝 Django / Installing Django...
pip install django
if %errorlevel% neq 0 (
    echo [!] Django 安裝失敗 / Django installation failed. 請檢查網路或 pip 設定 / Check network or pip settings.
) else (
    echo [?] Django 安裝成功 / Django installed successfully!
    python -m django --version
)
pause
goto MENU

:END
echo [*] 離開 Django 啟動器 / Exiting Django Launcher
endlocal
exit
