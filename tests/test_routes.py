import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.request_models import QueryRequest

client = TestClient(app)

@pytest.fixture(scope="module")
def test_client():
    return TestClient(app)

# Test the root endpoint
def test_read_root(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI application"}

# Test adding memory
def test_add_memory(test_client):
    data = {"text": "Test text", "user_id": "user_123"}
    response = test_client.post("/api/add", json=data)
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"message": "Text added successfully"}

# Test searching memory
def test_search_memory(test_client):
    response = test_client.get("/api/search", params={"query": "Test text", "user_id": "user_123"})
    assert response.status_code == 200
    # Replace this with the actual structure of the search results
    assert "results" in response.json()

# Test deleting all memory
def test_delete_all_memory(test_client):
    response = test_client.delete("/api/delete_all", params={"user_id": "user_123"})
    assert response.status_code == 200
    assert response.json() == {"message": "All texts deleted successfully"}
