from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_refund_status():
    resp = client.get("/refunds/status?ticket_id=1001")
    assert resp.status_code in [200, 404]
