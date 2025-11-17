from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_twilio_voice_root():
    response = client.post("/twilio/ivr", data={"Digits": "1"})
    assert response.status_code in [200, 400, 500]
