import os
import pytest
import todo_app.app as app
from dotenv import find_dotenv, load_dotenv
import json
from todo_app.data.item import TrelloItem
from unittest.mock import patch, Mock

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version 
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client: 
        yield client

def test_index_page(mock_get_requests, client): 
    response = client.get('/')

@patch('requests.request')
def test_index_page(mock_get_requests, client):
# Replace call to requests.get(url) with our own function
    mock_get_requests.side_effect = mock_get_lists
    response = client.get('/')


def mock_get_lists(method,url, params):
    if url == f"https://api.trello.com/1/lists/{os.getenv('TODOID')}/cards":
        response = Mock()
        
# sample_trello_lists_response should point to some test response data
        response.json.return_value = str("""[{
                "id": "12345",
                "name": "Test to do item",
                "idList": "67890",
                "dateLastActivity": "2020-08-01T12:52:06.278Z"
            }]""")

        return response
    elif url == f"https://api.trello.com/1/lists/{os.getenv('DONEID')}/cards": 
        response = Mock()
        
# sample_trello_lists_response should point to some test response data
        response.json.return_value = str("""[{
                "id": "12345",
                "name": "Test doing item",
                "idList": "67890",
                "dateLastActivity": "2020-08-01T12:52:06.278Z"
            }]""")

        return response
    elif url == f"https://api.trello.com/1/lists/{os.getenv('PENDINGID')}/cards": 
        response = Mock()
        
# sample_trello_lists_response should point to some test response data
        response.json.return_value = str("""[{
                "id": "12345",
                "name": "Test done item",
                "idList": "67890",
                "dateLastActivity": "2020-08-01T12:52:06.278Z"
            }]""")

        return response
    return None
