
@echo off
setlocal

set "TITAN007CRAWLER-HOME=..\titan007Crawler-"

set "VENV_PYTHON=%TITAN007CRAWLER-HOME%\.venv\Scripts\python.exe"
set "VENV_PYTHON_MERGE=.venv\Scripts\python.exe"


"%VENV_PYTHON%" "%TITAN007CRAWLER-HOME%\main.py" --company-id 3 --output titan007_data_Crow.xlsx
"%VENV_PYTHON%" "%TITAN007CRAWLER-HOME%\main.py" --company-id 8 --output titan007_data_36.xlsx
"%VENV_PYTHON%" "%TITAN007CRAWLER-HOME%\main.py" --company-id 14 --output titan007_data_Î°.xlsx
"%VENV_PYTHON%" "%TITAN007CRAWLER-HOME%\main.py" --company-id 17 --output titan007_data_Ã÷.xlsx
"%VENV_PYTHON%" "%TITAN007CRAWLER-HOME%\main.py" --company-id 24 --output titan007_data_12.xlsx
"%VENV_PYTHON%" "%TITAN007CRAWLER-HOME%\main.py" --company-id 31 --output titan007_data_Àû.xlsx
"%VENV_PYTHON%" "%TITAN007CRAWLER-HOME%\main.py" --company-id 35 --output titan007_data_Ó¯.xlsx
"%VENV_PYTHON%" "%TITAN007CRAWLER-HOME%\main.py" --company-id 42 --output titan007_data_18.xlsx



"%VENV_PYTHON_MERGE%" main.py

endlocal