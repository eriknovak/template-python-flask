# Main microservice script
# Retrieves, configures and connects all of the
# components of the microservice

import os

from flask import Flask
from flask_cors import CORS

from .config import config, config_logging

def create_app(args=None):
    # create and configure the app
    app = Flask(__name__, static_url_path='', static_folder='static', instance_relative_config=True)

    # add user provided configurations for the
    if args:
        app.config.update(
            HOST=args["host"],
            PORT=args["port"],
            # TODO: add additional enviroments
        )

    # set the service environment
    SERVICE_ENV = args["env"] if args else 'development'

    # setup the app configuration
    if SERVICE_ENV == 'production':
        app.config.from_object(config.ProductionConfig)
    elif SERVICE_ENV == 'development':
        app.config.from_object(config.DevelopmentConfig)
    elif SERVICE_ENV == 'testing':
        app.config.from_object(config.TestingConfig)

    # setup the cors configurations
    if app.config['CORS']['origins']:
        CORS(app, origins=app.config['CORS']['origins'])

    # add error handlers
    from .routes import error_handlers
    error_handlers.register(app)

    # create context: components are using app.config
    with app.app_context():
        # add logger configuration
        config_logging.init_app(app)

        # add index routes
        from .routes import index
        app.register_blueprint(index.bp)

        # add embedding routes
        from .routes import service
        app.register_blueprint(service.bp)

    # TODO: log start of the service
    # return the app
    return app
