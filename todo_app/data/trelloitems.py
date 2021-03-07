import requests
import os

from todo_app.data.item import TrelloItem


board_id= os.getenv('BOARDID')
todo_id=os.getenv('TODOID')
pending_id=os.getenv('PENDINGID')
done_id=os.getenv('DONEID')

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

def fetch_items_board():
    url = f"https://api.trello.com/1/boards/{board_id}/cards"
    
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

def fetch_lists_board():
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    
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

def fetch_items(listid, status):
    url = f"https://api.trello.com/1/lists/{listid}/cards"

    query = {
    'key': os.getenv('APP_KEY'),
    'token': os.getenv('APP_TOKEN')
    }

    response = requests.request(
    "GET",
    url,
    params=query
    )
    items=[]
    for item in response.json():
        items.append(TrelloItem(item['id'],status,item['name'],update_time=item['dateLastActivity']))

    return items

def UpdateToDone(card_id):
    url = f"https://api.trello.com/1/cards/{card_id}"
    
    query = {
    'key': os.getenv('APP_KEY'),
    'token': os.getenv('APP_TOKEN'),
    'idList': os.getenv('DONEID')
    }
  
    response = requests.request(
    "PUT",
    url,
    params=query
    )
