from fastapi import FastAPI, Request
from starlette.responses import Response  # <-- use this instead of XMLResponse

app = FastAPI()

@app.post("/twilio/voice")
async def twilio_voice(request: Request):
    return Response(
        content="""
        <Response>
            <Say voice="alice">Hello! This is your FastAPI Twilio test call.</Say>
        </Response>
        """,
        media_type="text/xml"
    )
