import pytest
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI!"}
def test_info():
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert data["project name"] == "Task Manager API"
    assert data["programming language"] == "Python"
def test_create_task_invalid_data():
    response = client.post(
        "/tasks",
        json={
            "title": "Learn FastAPI",
            "description": "Testing",
            "status": "Finished",
            "priority": "Urgent"})
    assert response.status_code == 422
@pytest.fixture
def created_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Learn Pytest",
            "description": "Practice CRUD testing",
            "status": "To Do",
            "priority": "High"})
    assert response.status_code == 200
    task_id = response.json()["task_id"]
    yield task_id
    client.delete(f"/tasks/{task_id}")
def test_create_task(created_task):
    response = client.get(f"/tasks/{created_task}")
    assert response.status_code == 200
    assert response.json()["title"] == "Learn Pytest"
def test_get_task_by_id(created_task):
    response = client.get(f"/tasks/{created_task}")
    assert response.status_code == 200
    assert response.json()["id"] == created_task
def test_update_task(created_task):
    response = client.put(
        f"/tasks/{created_task}",
        json={
            "title": "Learn Advanced FastAPI",
            "description": "Practice updating tasks",
            "status": "In Progress",
            "priority": "Medium"})
    assert response.status_code == 200
    assert response.json()["task"]["title"] == "Learn Advanced FastAPI"
def test_delete_task(created_task):
    response = client.delete(f"/tasks/{created_task}")
    assert response.status_code == 200
    get_response = client.get(f"/tasks/{created_task}")
    assert get_response.status_code == 404
def test_get_nonexistent_task():
    response = client.get("/tasks/-1")
    assert response.status_code == 404
def test_filter_tasks_by_status(created_task):
    response = client.get("/tasks/filter",params={"status": "To Do"})
    assert response.status_code == 200
    assert any(task["id"] == created_task for task in response.json())

def test_filter_tasks_by_priority(created_task):
    response = client.get("/tasks/filter",params={"priority": "High"})
    assert response.status_code == 200
    assert any(task["id"] == created_task for task in response.json())
def test_filter_tasks_by_both(created_task):
    response = client.get("/tasks/filter",params={"status": "To Do","priority": "High"})
    assert response.status_code == 200
    assert any(task["id"] == created_task for task in response.json())
def test_search_tasks(created_task):
    response = client.get(
        "/tasks/search",
        params={"keyword": "FastAPI"}
    )

    assert response.status_code == 200
    assert any(
        task["id"] == created_task for task in response.json())
def test_search_tasks_empty_keyword():
    response = client.get("/tasks/search",params={"keyword": "   "})
    assert response.status_code == 400
    assert response.json()["detail"] == "Search keyword cannot be empty"

