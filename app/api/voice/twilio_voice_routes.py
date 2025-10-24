from fastapi import APIRouter, Request, Form
from fastapi.responses import Response
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from app.core.config import settings

router = APIRouter(prefix="/voice", tags=["Voice"])

# Initialize Twilio client
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


@router.post("/incoming")
async def incoming_call(request: Request):
    """Handle incoming Twilio voice calls."""
    response = VoiceResponse()
    response.say("Welcome to Indian Railways IVR System.")
    response.pause(length=1)
    response.say("Please say your query after the beep.")
    response.record(
        timeout=5,
        transcribe=True,
        max_length=20,
        play_beep=True,
        action="/voice/recording_complete"
    )
    return Response(content=str(response), media_type="application/xml")


@router.post("/recording_complete")
async def recording_complete(request: Request):
    """Handle recorded user audio after Twilio captures it."""
    form = await request.form()
    recording_url = form.get("RecordingUrl")
    transcription_text = form.get("TranscriptionText")
    print(f"Recording URL: {recording_url}")
    print(f"Transcript: {transcription_text}")

    response = VoiceResponse()
    response.say("Thank you. We have received your query. Goodbye.")
    response.hangup()
    return Response(content=str(response), media_type="application/xml")


@router.post("/make_call")
async def make_call(to_number: str = Form(...)):
    """Initiate an outbound call using Twilio."""
    call = client.calls.create(
        twiml="<Response><Say>Hello, this is Indian Railways IVR system calling you.</Say></Response>",
        to=to_number,
        from_=settings.TWILIO_PHONE_NUMBER,
    )
    return {"status": "Call initiated", "call_sid": call.sid}
