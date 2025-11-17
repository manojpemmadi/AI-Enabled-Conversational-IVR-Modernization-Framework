from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_complaint():
    payload = {
        "name": "Test User",
        "phone": "9999999999",
        "issue": "Train late"
    }
    response = client.post("/complaints/register", json=payload)
    assert response.status_code in [200, 201]
