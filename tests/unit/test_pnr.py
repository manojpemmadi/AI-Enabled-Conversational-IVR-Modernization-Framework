from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_pnr_status():
    resp = client.get("/pnr/check?pnr=1234567890")
    assert resp.status_code in [200, 404]
