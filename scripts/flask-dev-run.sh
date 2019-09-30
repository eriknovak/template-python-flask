#!/usr/bin/env python
# this script is used for running the application
# in Windows PowerShell

# assign the variables for
# - Flask Environment
FLASK_ENV=$1

# set some default values for the variables
if [$FLASK_ENV -eq ""]; then
    echo "environment not set: setting to 'development'"
    FLASK_ENV=development
fi

# set the flask environment variables
export FLASK_APP=microservice
export FLASK_ENV=$FLASK_ENV

cd ..
# run the flask app (with autoreload)
python -m flask run
