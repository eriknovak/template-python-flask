# Configuration

This folder contains the configuration files.

## Environment Variables

To avoid storing vulnerable data in the repository (such as tokens
and secrets) we have adopted the `.env` approach to feed the vulnerable data to
different components of the microservice. It uses the [12-factor](https://12factor.net/)
principles.

This approach requires the [python-dotenv](https://pypi.org/project/python-dotenv/)
module (which is installed by running the `pip install python-dotenv` command)
and an `.env` file saved in this folder. One must create the `.env` file by hand
since it is ignored in the project.

### .env
What follows is an example of the `.env` file. To get the right configs contact
one of the developers contributing to this project.

The parameters that can be set in this file can be found [here](../../README.md#Alternatives).


```bash
#######################################
### Production variables
#######################################

# session secret
PROD_SESSION_KEY=session-key

#######################################
### Development variables
#######################################

# session secret
DEV_SESSION_KEY=session-key

#######################################
### Test variables
#######################################

# session secret
TEST_SESSION_KEY=session-key

######################################
# Common variables
######################################

# comma separated origins that will access the service
CORS_ORIGINS=origin1,origin2,origin3 (optional)

```
