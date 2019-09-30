# Microservice Initialization Scripts

These scripts are used to run the flask application in different environments.

To run the microservice, one must run the following command in the corresponding
terminal.

## Development

Instead of running the sequence of commands to run the flask development server
run one of the following (depending on the terminal you are using).

#### Bash
```bash
sh flask-dev-run.sh
```

#### CMD
```cmd
flask-dev-run.bat
```

#### PowerShell
```cmd
flask-dev-run.ps1
```

## Production

There are two scripts which are used for running the application in production:

| Script           | Description                                                                   |
| ---------------- | ----------------------------------------------------------------------------- |
| gunicorn.conf.py | The script used to setup the common configurations for all gunicorn processes |
| environment.sh   | The script that activates the python virtualenv environment                   |
