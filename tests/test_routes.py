import pytest
import os
from fastapi.testclient import TestClient
from app.main import app
from dotenv import load_dotenv

load_dotenv()

client = TestClient(app)

API_KEY = os.getenv("X_API_KEY")  # Replace with your actual API key

@pytest.fixture(scope="module")
def test_client():
    """
    Fixture to create a TestClient instance for the FastAPI app.

    Returns:
        TestClient: The test client used to make requests to the FastAPI application.
    """
    return TestClient(app)

# Test the root endpoint
def test_read_root(test_client):
    """
    Test the root endpoint '/'.

    This test ensures that a GET request to the root endpoint returns a status code of 200
    and a JSON response with a welcome message.

    Args:
        test_client (TestClient): The test client used to make requests to the FastAPI application.

    Asserts:
        The response status code is 200.
        The response JSON is {"message": "Welcome to the FastAPI application"}.
    """
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI application"}

# Test adding memory
def test_add_memory(test_client):
    """
    Test the /api/add endpoint for adding a memory.

    Args:
        test_client (TestClient): The test client to simulate HTTP requests.

    Test Steps:
    1. Define the data payload with a query and user_id.
    2. Send a POST request to the /api/add endpoint with the data payload and authentication headers.
    3. Print the JSON response for debugging purposes.
    4. Assert that the response status code is 200.
    5. Assert that the response contains a JSON body.

    Expected Results:
    - The response status code should be 200.
    - The response should contain a JSON body.
    """
    data = {"query": "Test text", "user_id": "user_123"}
    headers = {"x-api-key": API_KEY}
    response = test_client.post("/api/add", json=data, headers=headers)
    print(response.json())
    assert response.status_code == 200
    assert response.json()

# Test searching memory
def test_search_memory(test_client):
    """
    Test the search memory endpoint.

    This test sends a POST request to the /api/search endpoint with a JSON payload
    containing a query and a user ID. It asserts that the response status code is 200
    and that the response contains a JSON body.

    Args:
        test_client (TestClient): The test client used to make requests to the API.

    Asserts:
        The response status code is 200.
        The response contains a JSON body.
    """
    headers = {"x-api-key": API_KEY}
    response = test_client.post(
        "/api/search",
        json={"query": "Test text", "user_id": "user_123"},
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()

# Test deleting all memory
def test_delete_all_memory(test_client):
    """
    Test the endpoint to delete all memory texts for a specific user.

    This test sends a DELETE request to the "/api/delete_all" endpoint with a user_id parameter.
    It asserts that the response status code is 200 and that the response JSON contains a success message.

    Args:
        test_client (TestClient): The test client used to make requests to the API.

    Asserts:
        The response status code is 200.
        The response JSON contains {"message": "All texts deleted successfully"}.
    """
    headers = {"x-api-key": API_KEY}
    response = test_client.delete("/api/delete_all", params={"user_id": "user_123"}, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "All texts deleted successfully"}
