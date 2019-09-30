# this script is used for running the application
# in Windows PowerShell

# assign the variables for
# - Flask Environment
$FLASK_ENV = $args[0]

# set some default values for the variables
if ("$FLASK_ENV" -eq "") {
    Write-Output "environment not set: setting to 'development'"
    $FLASK_ENV="development"
}

# set the flask environment variables
$env:FLASK_APP="microservice"
$env:FLASK_ENV="$FLASK_ENV"

Set-Location ../
# run the flask app (with autoreload)
python -m flask run