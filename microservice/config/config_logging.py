# Logging config script
# Contains the methods for establishing and
# calling the logging function across the service

# imporkt the logger function
from ..library.logger import configure_timed_rotating_log


def init_app(app):
    """Initializes the application and adds the methods for handling the logger"""
    app.logger = configure_timed_rotating_log(path='./log/microservice.log')