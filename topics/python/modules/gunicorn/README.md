# Gunicorn

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [WSGI](#wsgi)
- [Pre-fork Worker Model](#prefork-worker-model)
- [Installation](#installation)
- [Usage](#usage)
	- [Workers](#workers)
	- [Specify Server Socket to Bind to](#specify-server-socket-to-bind-to)
	- [Working Directory](#working-directory)
	- [TLS](#tls)

<!--TOC_END-->
## Overview
Gunicorn is a type of Web Server Gateway Interface (WSGI) HTTP server.

## WSGI
There are many different frameworks that are available for Python to develop web applications, because of this compatibility issues arise.
WSGI provides a specification ([PEP 3333](https://www.python.org/dev/peps/pep-3333)) to adhere to, making any servers that use compatible with any frameworks that also use it.

## Pre-fork Worker Model
Gunicorn uses a pre-fork worker model which is a master process which controls 1 or more worker processes:
- The master process knows nothing about the client connections to the worker processes.
- Process signals are sent between the workers & master to determine whether a new worker needs to be booted.
- If a worker process crashes from a fatal exception, then another worker can be booted to replace it.

## Installation
Gunicorn can be installed by using `pip`:
```bash
pip install gunicorn
```

## Usage
You can start an application by running the command below, this would work for an application written in a file called `app.py` with the application set to an `app` variable:
```bash
# gunicorn [APP_MODULE]:[VARIABLE_NAME]
gunicorn app:app 
```
- `APP_MODULE`
  This is will be module (Python file) that the application is in.
- `VARIABLE_NAME`
  By default, Gunicorn will look for a variable called `application`, if yours is defined as something else then it may be specified here.

### Workers
The amount of workers can be specified with the `-w` or `--workers` options.
The Gunicorn documentation reccommends that you use 2-4 workers per core the server you are using has:
```bash
# gunicorn --workers [NUMBER]  app:app
gunicorn --workers 4 app:app
```

### Specify Server Socket to Bind to
You may provide a server socket in the form of `[HOST]` or `[HOST]:[PORT]` with the `-b` or `--bind` options.
There are other protocols you can bind to such as `unix` sockets as well.

To allow traffic from anywhere on port `8001` you can use the following:
```bash
# gunicorn --bind=[HOST]:[PORT] app:app
gunicorn --bind=0.0.0.0:8001 app:app
```

### Working Directory
Gunicorn can operate in a specified directory using the `--chdir` option, this would typically be the application root:
```bash
# gunicorn --chdir=[DIRECTORY] app:app
gunicorn --chdir=/opt/project app:app
```

### TLS
The Gunicorn server can be configured to use certificates by providing the `--certfile` and `--keyfile` options:
```bash
# gunicorn --certifile=[CERT_FILE] --keyfile=[KEY_FILE]
gunicorn --certifile=~/server.crt --keyfile=~/server.key
```

### SystemD Service Configuration

