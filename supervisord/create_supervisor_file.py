#################################################
# Create the Supervisor file
# This script reads the supervisor microservice
# config file and creates a supervisor config
# file
#

import os
import json
import re

from shutil import copyfile
import argparse

def create_supervisor_file(user):
    """Creates the supervisor file

    Args:
        user (str): The user that has access to the repository and will run the services.

    """

    # get the absolute path of the repository
    _ROOT = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..'))

    # open the supervisor microservice configuration file
    with open("./supervisor_config.json") as f:
        config = json.load(f)

    # create a placeholder for the text embedding config file
    microservice_conf = [";/etc/supervisor/conf.d/microservice.conf"]

    if "microservice" in config:
        # TODO: change the required attributes for running the microservice
        # get the interfaced parameters
        program = config["microservice"]["program"]
        port = config["microservice"]["port"]
        workers = config["microservice"]["workers"]

       # create the service configuration file
        microservice_config = """
            [program:{}]
            user = {}
            directory = {}
            command = sh ./scripts/environment.sh gunicorn -w {} -b 127.0.0.1:{} -c ./scripts/gunicorn.conf.py 'microservice:create_app(args={{ "host":"127.0.0.1", "port":{}, "env":"production" }})'

            priority = 900
            autostart = true
            autorestart = true
            stopsignal = TERM

            redirect_stderr = true
            stdout_logfile = {}/log/%(program_name)s.log
            stderr_logfile = {}/log/%(program_name)s.log
        """.format(program, user, _ROOT, workers, port, port, _ROOT, _ROOT)

        # format the configuration string
        microservice_config = re.sub(' +', ' ', microservice_config)
        microservice_config = re.sub('\n ', '\n', microservice_config)

        # append to the existing configurations
        microservice_conf.append(microservice_config)

    # join the text embedding configurations
    microservice_conf = "\n".join(microservice_conf)
    # create and write the text_embeddings.conf file
    with open("./microservice.conf", "w+") as w:
        w.write(microservice_conf)


def copy_supervisor_file():
    """
    Copies the generated text_embeddings.conf file to the appropriate supervisor file

    """

    # check if the supervisor file exists
    if not os.path.isfile("./microservice.conf"):
        return Exception("File microservice.conf does not exist")

    # otherwise check if the supervisor folder exists
    if not os.path.exists("/etc/supervisor/conf.d"):
        return Exception("Supervisor is not installed or folder /etc/supervisor/conf.d does not exist")

    # copy the file to the final destination
    copyfile("./microservice.conf", "/etc/supervisor/conf.d/microservice.conf")


#################################################
# Helper function
#################################################

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__=='__main__':
    # parse command line arguments
    argparser = argparse.ArgumentParser(description="Creates the supervisor script file and potentially copy it to the appropriate folder")
    subparsers = argparser.add_subparsers()

    argparser_create = subparsers.add_parser('create', help="Runs the service in the production environment")

    # the script creation files
    argparser_create.add_argument('-u', '--user', type=str, help="The user that will start the microservices")
    argparser_create.add_argument('--copy', type=str2bool, nargs='?', const=True, default=False, help="If the generated file needs to be copied to the supervisord folder")
    argparser_create.set_defaults(command='create')

    # parse the arguments and call whatever function was selected
    args = argparser.parse_args()

    if args.command == 'create':
        # creates the supervisor file for the given user
        create_supervisor_file(args.user)
        if args.copy:
            # copy the supervisor file
            copy_supervisor_file()

    else:
        raise Exception('Argument command is unknown: {}'.format(args.command))