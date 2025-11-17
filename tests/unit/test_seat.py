from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_seat_availability():
    resp = client.get("/seat/check?train_no=17001&date=2025-11-17")
    assert resp.status_code in [200, 404]
