from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_emergency_help():
    resp = client.get("/emergency/help")
    assert resp.status_code == 200
    assert "Emergency support" in resp.json()["message"]
