:: this script is used for running the application
:: in Windows PowerShell
@echo off

:: assign the variables for
:: - Flask Environment
set FLASK_ENV=%1

:: set some default values for the variables
if "%FLASK_ENV%"=="" (
    ECHO "environment not set: setting to 'development'"
    set FLASK_ENV=development
)

:: set the flask environment variables
set FLASK_APP=microservice

cd ..
:: run the flask app (with autoreload)
python -m flask run