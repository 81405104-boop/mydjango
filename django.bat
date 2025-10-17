@echo off
title Django Portable Environment v2.6 (EN/����)
setlocal enabledelayedexpansion

REM === ���o�Ұʾ��Ҧb�Ϻ� (���ެO E:\ F:\ G:\) ===
set "BASE=%~d0"

REM === �]�w Python �P Django �M�׸��| ===
set "PYTHON=%BASE%\Python\python.exe"
set "PROJECT_DIR=%BASE%\mydjango"
set "VENV_DIR=%PROJECT_DIR%\venv"

echo ==================================================
echo [*] �i�⦡ Python + Django �Ұʾ� v2.6 (EN/����)
echo Portable Python + Django Launcher
echo �Ұʾ��Ϻ� (Base Drive): %BASE%
echo Python ��m (Python Path): %PYTHON%
echo �M�׸��| (Project Path): %PROJECT_DIR%
echo ==================================================

REM === �ˬd Python �O�_�s�b ===
if not exist "%PYTHON%" (
    echo [!] �䤣�� Python / Python not found: %PYTHON%
    echo �нT�{ Python ��Ƨ��P�Ұʾ��b�P�@�h / Make sure Python folder is next to launcher.
    pause
    exit /b
)

REM === �ˬd�������ҬO�_�s�b�A�Y�S���h�إ� ===
if not exist "%VENV_DIR%" (
    echo [*] �إߵ�������... / Creating virtual environment...
    "%PYTHON%" -m venv "%VENV_DIR%"
    echo [?] �������ҫإߧ����I / Virtual environment created!
)

REM === �Ұʵ������� ===
call "%VENV_DIR%\Scripts\activate.bat"

:MENU
cls
echo ==================================================
echo [1] �Ұ� Django ���A���]�۰ʴM��i�� Port�^ / Start Django server (auto port)
echo [2] �u�i�J�������� (�R�O�C�Ҧ�) / Enter virtual environment (CLI)
echo [3] �w�� requirements.txt �M�� / Install requirements.txt packages
echo [4] ���� makemigrations + migrate / Run makemigrations + migrate
echo [5] �۰ʦw�� Django / Install Django
echo [6] ���} / Exit
echo ==================================================
set /p choice=�п�J�ﶵ (1-6) / Please select option (1-6): 

if "%choice%"=="1" goto STARTSERVER
if "%choice%"=="2" goto ENTERVENV
if "%choice%"=="3" goto INSTALLREQ
if "%choice%"=="4" goto MIGRATE
if "%choice%"=="5" goto INSTALLDJANGO
if "%choice%"=="6" goto END
echo [!] �L�Ī��ﶵ / Invalid option. Please try again.
pause
goto MENU

:STARTSERVER
cd /d "%PROJECT_DIR%"
REM === �w�] port ===
set "PORT=8000"

:CHECKPORT
netstat -ano | findstr :%PORT% >nul
if %errorlevel%==0 (
    echo [!] Port %PORT% �w�Q���ΡA���ըϥΤU�@��... / Port %PORT% in use, trying next...
    set /a PORT=%PORT%+1
    goto CHECKPORT
)

echo [*] �Ұ� Django ���A�� (http://127.0.0.1:%PORT%) / Starting Django server...
start http://127.0.0.1:%PORT%
python manage.py runserver 127.0.0.1:%PORT%
pause
goto MENU

:ENTERVENV
echo [*] �A�{�b�w�i�J�������ҡA�i�H��ʿ�J���O�C
echo [����] ��J exit �i��^�Ұʾ����C
echo [*] You are now inside the virtual environment.
echo [Tip] Type 'exit' to return to menu.
cmd
goto MENU

:INSTALLREQ
cd /d "%PROJECT_DIR%"
if exist requirements.txt (
    echo [*] ������ requirements.txt�A�}�l�w�ˮM��...
    echo [*] requirements.txt detected. Installing packages...
    pip install -r requirements.txt
    echo [?] �w�˧��� / Installation complete!
) else (
    echo [!] �S��� requirements.txt / File not found.
)
pause
goto MENU

:MIGRATE
cd /d "%PROJECT_DIR%"
echo [*] ���� makemigrations... / Running makemigrations...
python manage.py makemigrations
echo [*] ���� migrate... / Running migrate...
python manage.py migrate
echo [?] ��Ʈw�E�������I / Database migration complete!
pause
goto MENU

:INSTALLDJANGO
echo [*] �}�l�w�� Django / Installing Django...
pip install django
if %errorlevel% neq 0 (
    echo [!] Django �w�˥��� / Django installation failed. ���ˬd������ pip �]�w / Check network or pip settings.
) else (
    echo [?] Django �w�˦��\ / Django installed successfully!
    python -m django --version
)
pause
goto MENU

:END
echo [*] ���} Django �Ұʾ� / Exiting Django Launcher
endlocal
exit
