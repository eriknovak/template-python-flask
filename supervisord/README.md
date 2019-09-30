# Supervisor File Creation

This folder contains all of the information for automatically create and copy the
supervisor configurations for running multiple services with different parameters.

## Configurations

The scripts that create the supervisor configuration file all ready from a single
file - the `supervisor_config.json` file. This file has the following structure:


```js
{

  "microservice": {
    "program": {string: program-name (must-be-unique)},
    "port": {number: port-number},
    "workers": {number: number-of-workers}
  }

}
```

An example of such file is presented bellow:
```js
{
  "microservice": {
    "program": "microservice",
    "port": 6000,
    "workers": 1
  }
}
```

## Creation Script

Once the configuration file is created, one can simply create the supervisor configuration
file with a simple command. The parameters it receives are:

| Parameter    | Description                                                                                                                          |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| -u or --user | The username that has access to the repository and will start the services                                                           |
| -c or --copy | Copies the created `microservice.conf` to the `/etc/supervisord/conf.d` folder. User needs `sudo` privilages to do this (optional) |

```bash
[sudo] python create_supervisor_file.py -u {username} [--copy]
```
