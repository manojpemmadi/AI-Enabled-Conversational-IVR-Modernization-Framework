from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_schedule_lookup():
    resp = client.get("/train/schedule?train_no=17001")
    assert resp.status_code in [200, 404]
