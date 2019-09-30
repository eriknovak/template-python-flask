# for directory creation
import os

# the main logging function
import logging
# the timed rotating file handler
from logging.handlers import TimedRotatingFileHandler


def __create_folder_dir(path):
    """Creates the folder structure associated with the `path`

    Args:
        path (str): The path to the given file.
    """

    # get the folder structure path
    normpath = os.path.normpath(path)
    split_path = normpath.split(os.sep)
    del split_path[-1]
    # reconstruct the folder structure and create
    # the directories if they do not exist yet
    directory = os.sep.join(split_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def configure_timed_rotating_log(path, name="microservice"):
    """Configures the logging

    Args:
        path (str): The path to the log file.
        name (str): The name of the logger. (Default = "microservice")

    Returns:
        obj: the logger object.
    """

    # create the folder structure
    __create_folder_dir(path)
    # create the logger instance and set its level
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # create a new rotating logger handler
    handler = TimedRotatingFileHandler(path,
                                       interval=1,
                                       when="midnight",
                                       backupCount=0)

    # set the logger format and assign it to the handlers
    formatter = logging.Formatter(
        '%(name)-12s %(levelname)-8s [%(asctime)-12s]: %(message)s'
    )
    handler.setFormatter(formatter)
    # add handler
    logger.addHandler(handler)
    # return the logger object
    return logger
