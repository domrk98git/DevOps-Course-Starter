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

@patch('requests.request')
def test_index_page(mock_get_requests, client):
# Replace call to requests.get(url) with our own function
    mock_get_requests.side_effect = mock_get_lists
    response = client.get('/')
    assert response.status_code == 200
    assert '12345' in response.data.decode()

def mock_get_lists(method,url, params):
    if url == f"https://api.trello.com/1/lists/{os.getenv('TODOID')}/cards":
        response = Mock()
        
# sample_trello_lists_response should point to some test response data
        response.json.return_value = [{
                "id": "12345",
                "name": "Test to do item",
                "dateLastActivity": "2021-02-21T19:30:30.101Z"
            }]

        return response
    elif url == f"https://api.trello.com/1/lists/{os.getenv('PENDINGID')}/cards": 
        response = Mock()
        
# sample_trello_lists_response should point to some test response data
        response.json.return_value = [{
                "id": "123456",
                "name": "Test doing item",
                "dateLastActivity": "2021-02-21T19:30:30.101Z"
            }]

        return response
    elif url == f"https://api.trello.com/1/lists/{os.getenv('DONEID')}/cards": 
        response = Mock()
        
# sample_trello_lists_response should point to some test response data
        response.json.return_value = [{
                "id": "1234567",
                "name": "Test done item",
                "dateLastActivity": "2021-02-21T19:30:30.101Z"
            }]

        return response
    return None
