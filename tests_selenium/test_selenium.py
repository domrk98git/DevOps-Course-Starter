from dotenv import find_dotenv, load_dotenv
import requests
import os
import pytest
from threading import Thread
from selenium import webdriver
from todo_app import app



def create_trello_board():
    
    url = "https://api.trello.com/1/boards/"

    query = {
    'key': os.getenv("APP_KEY"),
    'token': os.getenv("APP_TOKEN"),
    'name': 'SELTEST'
    }

    response = requests.request(
    "POST",
    url,
    params=query
    ).json()
    os.environ["BOARDID"]=response['id']
    response = requests.get(f"https://api.trello.com/1/boards/{os.getenv('BOARDID')}/lists", params=query).json()
    os.environ["TODOID"]=response[0]['id']
    os.environ["PENDINGID"]=response[1]['id']
    os.environ["DONEID"]=response[2]['id']

def delete_trello_board():
    
    url = f"https://api.trello.com/1/boards/{os.getenv('BOARDID')}"

    query = {
    'key': os.getenv("APP_KEY"),
    'token': os.getenv("APP_TOKEN"),
    'name': 'SELTEST'
    }

    response = requests.request(
    "DELETE",
    url,
    params=query
    )

    

@pytest.fixture(scope='module')
def app_with_temp_board():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
# Create the new board & update the board id environment variable
    board_id = create_trello_board() 
# construct the new application 
    application = app.create_app()
# start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True 
    thread.start()
    yield app
# Tear Down
    thread.join(1) 
    delete_trello_board()

@pytest.fixture(scope="module") 
def driver():
    with webdriver.Chrome('./chromedriver') as driver: 
        yield driver

def test_task_journey(driver, app_with_temp_board): 
    driver.get('http://localhost:5000/')

    assert driver.title == 'To-Do App'