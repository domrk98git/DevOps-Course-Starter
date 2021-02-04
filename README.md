# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the Docker build and run app with just development entry in Dockerfile
steps 1 - 
docker build --tag module5 .

step2 - 
docker run -p 5000:5000 --env-file .env module5
 * Serving Flask app "todo_app/app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 240-503-066

 ## Running the App in PROD environment
 ## added below entry to pyproject.toml
 gunicorn = "20.0.4"

## Add development build stage to dockerfile
 docker build --target development --tag module5:dev .

 ## Running the App in dev environment

 (base) RaviDommatas-Mac-mini:DevOps-Course-Starter rkdommata$ docker run -p 5000:5000 --env-file .env module5:dev .
docker: Error response from daemon: OCI runtime create failed: container_linux.go:349: starting container process caused "exec: \".\": executable file not found in $PATH": unknown.
(base) RaviDommatas-Mac-mini:DevOps-Course-Starter rkdommata$ docker run -p 5000:5000 --env-file .env -d module5                                  2d356da249c9746a8d3f3de47c1c03fafb19215642694d1c9750c95dfbeeb714
(base) RaviDommatas-Mac-mini:DevOps-Course-Starter rkdommata$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                              NAMES
2d356da249c9        module5             "/bin/sh -c 'poetry …"   12 minutes ago      Up 12 minutes       0.0.0.0:5000->5000/tcp, 5002/tcp   vibrant_khorana

## Add production build stage to dockerfile
(base) RaviDommatas-Mac-mini:DevOps-Course-Starter rkdommata$ docker build --target development --tag module5:prod .
....
Successfully built 7b4498ed3446
Successfully tagged module5:prod

## Running the App in dev environmentbase) 
RaviDommatas-Mac-mini:DevOps-Course-Starter rkdommata$ docker run -p 5001:5001 --env-file .env -d module5:prod
061fbafef6fb67906858b28a27c95bb999d6d4da29664aa14d7af4fec3a9228e
(base) RaviDommatas-Mac-mini:DevOps-Course-Starter rkdommata$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                              NAMES
061fbafef6fb        module5:prod        "/bin/sh -c 'poetry …"   24 seconds ago      Up 23 seconds       0.0.0.0:5001->5001/tcp, 5002/tcp   gifted_mayer
2d356da249c9        module5             "/bin/sh -c 'poetry …"   23 hours ago        Up 23 hours         0.0.0.0:5000->5000/tcp, 5002/tcp   vibrant_khorana

docker run -p 5002:5002 --env-file .env  module5:prod


