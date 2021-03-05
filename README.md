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

## Trello API TOKEN:  
APP_KEY and APP_TOKEN added to .env file which will be ignored by .gitignore to upload to git repository, not uploaded during GIT push.

Trello website. 
https://trello.com/b/hewBwugd/module2
add .json to above to lookup boardid, listid details 


## Add development build stage to dockerfile
 docker build --target development --tag module5:dev .

 ## Running the App in dev environment

(base) RaviDommatas-Mac-mini:DevOps-Course-Starter rkdommata$ docker run -p 5000:5000 --env-file .env module5
 * Serving Flask app "todo_app/app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 307-202-561

with mount bind on docker run :
docker run -p 5000:5000 --mount type=bind,source="$(pwd)",target=/app --env-file .env module5
 ## Running the App in PROD environment
 ## added below entry to pyproject.toml
 gunicorn = "20.0.4"

## Add production build stage to dockerfile
(base) RaviDommatas-Mac-mini:DevOps-Course-Starter rkdommata$ docker build --target production --tag module5:prod .
....
Successfully built 7b4498ed3446
Successfully tagged module5:prod

## Running the App in prod environment 

(base) RaviDommatas-Mac-mini:DevOps-Course-Starter rkdommata$ docker run -p 5002:8000 --env-file .env  module5:prod
[2021-02-20 02:46:10 +0000] [6] [INFO] Starting gunicorn 20.0.4
[2021-02-20 02:46:10 +0000] [6] [INFO] Listening at: http://0.0.0.0:8000 (6)
[2021-02-20 02:46:10 +0000] [6] [INFO] Using worker: sync
[2021-02-20 02:46:10 +0000] [10] [INFO] Booting worker with pid: 10

Accessed production at http://0.0.0.0:5002

## mount bind on docker run : prod and dev
(base) RaviDommatas-Mac-mini:DevOps-Course-Starter rkdommata$ docker run -p 5003:8000 --mount type=bind,source="$(pwd)",target=/todo_app.app --env-file .env  module5:prod
[2021-02-20 04:13:01 +0000] [7] [INFO] Starting gunicorn 20.0.4
[2021-02-20 04:13:01 +0000] [7] [INFO] Listening at: http://0.0.0.0:8000 (7)
[2021-02-20 04:13:01 +0000] [7] [INFO] Using worker: sync
[2021-02-20 04:13:01 +0000] [11] [INFO] Booting worker with pid: 11

(base) RaviDommatas-Mac-mini:DevOps-Course-Starter rkdommata$ docker run -p 5000:5000 --mount type=bind,source="$(pwd)",target=/todo_app.app --env-file .env  module5
 * Serving Flask app "todo_app/app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 163-123-678
172.17.0.1 - - [20/Feb/2021 04:22:35] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [20/Feb/2021 04:22:45] "POST /Add HTTP/1.1" 302 -
172.17.0.1 - - [20/Feb/2021 04:22:45] "GET / HTTP/1.1" 200 -


