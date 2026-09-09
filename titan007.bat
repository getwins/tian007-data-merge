
@REM @echo off
setlocal enabledelayedexpansion

rem This file is UTF-8 encoded, so we need to update the current code page while executing it
for /f "tokens=2 delims=:." %%a in ('"%SystemRoot%\System32\chcp.com"') do (
    set _OLD_CODEPAGE=%%a
)
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" 65001 > nul
)

cd /d "%~dp0"
set "MERGE_PROJECT_HOME=%~dp0"
set "MERGE_VENV_PYTHON=%MERGE_PROJECT_HOME%\.venv\Scripts\python.exe"

rem Use the sibling crawler project and its own virtual environment.
for %%I in ("%MERGE_PROJECT_HOME%..") do set "PARENT_DIR=%%~fI"
set "CRAWLER_PROJECT_HOME=%PARENT_DIR%\titan007Crawler-"
set "CRAWLER_VENV_PYTHON=%CRAWLER_PROJECT_HOME%\.venv\Scripts\python.exe"
set "CRAWLER_APP=%CRAWLER_PROJECT_HOME%\main.py"

if not exist "%CRAWLER_VENV_PYTHON%" (
    echo Error: missing crawler venv at %CRAWLER_VENV_PYTHON%
    exit /b 1
)
if not exist "%CRAWLER_APP%" (
    echo Error: missing crawler main.py at %CRAWLER_APP%
    exit /b 1
)

"%CRAWLER_VENV_PYTHON%" "%CRAWLER_APP%" --company-id 3 --output titan007_data_Crow.xlsx
"%CRAWLER_VENV_PYTHON%" "%CRAWLER_APP%" --company-id 8 --output titan007_data_36.xlsx
"%CRAWLER_VENV_PYTHON%" "%CRAWLER_APP%" --company-id 14 --output titan007_data_伟.xlsx
"%CRAWLER_VENV_PYTHON%" "%CRAWLER_APP%" --company-id 17 --output titan007_data_明.xlsx
"%CRAWLER_VENV_PYTHON%" "%CRAWLER_APP%" --company-id 24 --output titan007_data_12.xlsx
"%CRAWLER_VENV_PYTHON%" "%CRAWLER_APP%" --company-id 31 --output titan007_data_利.xlsx
"%CRAWLER_VENV_PYTHON%" "%CRAWLER_APP%" --company-id 35 --output titan007_data_盈.xlsx
"%CRAWLER_VENV_PYTHON%" "%CRAWLER_APP%" --company-id 42 --output titan007_data_18.xlsx

@REM "%MERGE_VENV_PYTHON%" "%MERGE_PROJECT_HOME%\main.py" --basedir "%MERGE_PROJECT_HOME%" 
"%MERGE_VENV_PYTHON%" "%MERGE_PROJECT_HOME%\main.py"

:END
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" %_OLD_CODEPAGE% > nul
    set _OLD_CODEPAGE=
)
