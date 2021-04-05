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
CMD poetry run gunicorn "todo_app.app:app" --bind 0.0.0.0

# testing stage FROM base as test ...
FROM base as test
RUN apt-get update
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
    apt-get install ./chrome.deb -y &&\
    rm ./chrome.deb

# Install Chromium WebDriver
# RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` &&\
#     echo "Installing chromium webdriver version ${LATEST}" &&\
#    curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
#     apt-get install unzip -y &&\
#      unzip ./chromedriver_linux64.zip
ENTRYPOINT ["poetry", "run", "pytest"]