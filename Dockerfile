from python:3.8.2-slim-buster as base

ENV APP_INSTALL=/app
ENV POETRY_HOME=/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}
ENV PYTHON_PATH=${APP_INSTALL}

# Install curl
RUN apt-get update && apt-get install curl -y

# Install poetry 
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python


# copy across app code
WORKDIR ${APP_INSTALL}
COPY . /app
RUN poetry install

# list all copied files
RUN ls -la ./


# define entry point , and default launch command

# for development
FROM base as development
EXPOSE 5002
CMD poetry run flask run --host 0.0.0.0

# for production
FROM base as production
EXPOSE 5001
CMD poetry run gunicorn --host 0.0.0.0

# ["gunicorn", "--bind", "0.0.0.0:5001", "--log-level=debug", "app:todo_app/app"]

#FROM base as prod
#ENV FLASK_ENV=production
#ENTRYPOINT poetry run gunicorn "app:create_app()" --bind 0.0.0.0:5000