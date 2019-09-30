import argparse
from microservice import create_app

if __name__=='__main__':
    # parse command line arguments
    argparser = argparse.ArgumentParser(description="Microservice")
    subparsers = argparser.add_subparsers()

    argparser_production = subparsers.add_parser('start', help="Runs the service in the production environment")

    # the host and port of the text embedding microservice
    argparser_production.add_argument('-H', '--host', type=str, default='127.0.0.1', help="The host of the microservice")
    argparser_production.add_argument('-p', '--port', type=str, default='4000', help="The port of the microservice")
    argparser_production.add_argument('-e', '--env', type=str, default='production', help="The microservice environment")
    # TODO: the model parameters


    argparser_production.set_defaults(command='start')

    # parse the arguments and call whatever function was selected
    args = argparser.parse_args()

    if args.command == 'start':
        # get the arguments for creating the app
        arguments = {
            "host": args.host,
            "port": args.port,
            "env": args.env,
            # TODO: add additional arguments
        }
        # create the application
        app = create_app(args=arguments)
        # run the application
        app.run(host=arguments["host"], port=arguments["port"])

    else:
        raise Exception('Argument command is unknown: {}'.format(args.command))