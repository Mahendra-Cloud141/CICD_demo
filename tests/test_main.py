from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to CI/CD demo!"}

def test_add():
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {"sum": 5}
