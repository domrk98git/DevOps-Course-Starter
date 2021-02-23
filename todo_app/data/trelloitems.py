import requests
import os


board_id= '6032b49b5e077170a897e557'
todo_id='6032b49b5e077170a897e558'

def create_item(title):

    url = "https://api.trello.com/1/cards"

    query = {
    'key': os.getenv('APP_KEY'),
    'token': os.getenv('APP_TOKEN'),
    'idList': '6032b49b5e077170a897e558',
    'name':title
    }

    response = requests.request(
    "POST",
    url,
    params=query
    )

    print(response.json())

def fetch_items():
    ##url = f"https://api.trello.com/1/boards/{board_id}/cards"
    url = f"https://api.trello.com/1/lists/{todo_id}/cards"

    query = {
    'key': os.getenv('APP_KEY'),
    'token': os.getenv('APP_TOKEN')
    }

    response = requests.request(
    "GET",
    url,
    params=query
    )

    return response.json()

def UpdateToDone(card_id):
    url = f"https://api.trello.com/1/cards/{card_id}"
    
    query = {
    'key': os.getenv('APP_KEY'),
    'token': os.getenv('APP_TOKEN'),
    'idList': '6032b49b5e077170a897e55a'
    }
  
    response = requests.request(
    "PUT",
    url,
    params=query
    )

    print(response.json())