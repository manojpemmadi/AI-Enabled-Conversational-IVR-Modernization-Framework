from fastapi import APIRouter, Request, Form
from fastapi.responses import Response
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from app.core.config import settings  # Twilio credentials from .env

router = APIRouter(prefix="/voice", tags=["Voice"])

# Initialize Twilio client
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

# -------------------------------------------------------------------------
# 1️⃣ Incoming call entry point
# -------------------------------------------------------------------------
@router.post("/incoming")
async def incoming_call(request: Request):
    """
    Handle incoming Twilio voice calls (caller speaks query).
    """
    response = VoiceResponse()

    # Greeting + instructions
    response.say(
        "Welcome to Indian Railways Interactive Voice Response System.",
        voice="man"
    )
    response.pause(length=1)
    response.say(
        "Please clearly state your query after the beep. "
        "You can say things like: Check P N R status, register a complaint, "
        "emergency help, train schedule, seat availability, or refund status.",
        voice="man"
    )

    # Record caller speech and automatically transcribe
    response.record(
        timeout=5,
        transcribe=True,  # Twilio does speech-to-text
        max_length=20,    # Limit recording time
        play_beep=True,
        # ✅ FIX: Use full public URL for action
        action="https://malissa-silvicultural-overwildly.ngrok-free.dev/voice/recording_complete"
    )

    return Response(content=str(response), media_type="application/xml")


# -------------------------------------------------------------------------
# 2️⃣ Twilio sends recorded + transcribed text here
# -------------------------------------------------------------------------
@router.post("/recording_complete")
async def recording_complete(request: Request):
    """
    Handle completed recording + transcription from Twilio.
    """
    form = await request.form()
    recording_url = form.get("RecordingUrl")
    transcription_text = form.get("TranscriptionText")

    print("\n--- Incoming Call Transcription ---")
    print(f"Recording URL: {recording_url}")
    print(f"Transcription: {transcription_text}")
    print("-----------------------------------\n")

    # --- Analyze what the caller said ---
    if not transcription_text:
        transcription_text = ""
    text = transcription_text.lower()

    # Identify which module the user is asking for
    if "pnr" in text or "status" in text:
        redirect_url = "https://malissa-silvicultural-overwildly.ngrok-free.dev/pnr_status"
        message = "Redirecting you to the P N R status department."
    elif "complaint" in text or "issue" in text or "problem" in text:
        redirect_url = "https://malissa-silvicultural-overwildly.ngrok-free.dev/complaints"
        message = "Redirecting you to the complaints department."
    elif "emergency" in text or "help" in text or "accident" in text:
        redirect_url = "https://malissa-silvicultural-overwildly.ngrok-free.dev/emergency"
        message = "Connecting you to emergency services."
    elif "schedule" in text or "time" in text or "train" in text:
        redirect_url = "https://malissa-silvicultural-overwildly.ngrok-free.dev/train_schedule"
        message = "Redirecting you to the train schedule department."
    elif "seat" in text or "availability" in text or "booking" in text:
        redirect_url = "https://malissa-silvicultural-overwildly.ngrok-free.dev/seat_availability"
        message = "Redirecting you to the seat availability department."
    elif "refund" in text or "cancel" in text or "money" in text:
        redirect_url = "https://malissa-silvicultural-overwildly.ngrok-free.dev/refunds"
        message = "Redirecting you to the refund department."
    else:
        redirect_url = None
        message = "Sorry, I could not understand your request."

    # --- Build TwiML response ---
    response = VoiceResponse()
    response.say(message, voice="man")

    if redirect_url:
        response.redirect(redirect_url)
    else:
        response.say("Please try again or contact customer service.", voice="man")
        response.hangup()

    return Response(content=str(response), media_type="application/xml")


# -------------------------------------------------------------------------
# 3️⃣ Optional outbound call endpoint
# -------------------------------------------------------------------------
@router.post("/make_call")
async def make_call(to_number: str = Form(...)):
    """
    Initiate an outbound call using Twilio.
    """
    call = client.calls.create(
        twiml="""
            <Response>
                <Say voice="man">Hello, this is the Indian Railways IVR system calling you.</Say>
            </Response>
        """,
        to=to_number,
        from_=settings.TWILIO_PHONE_NUMBER,
    )
    return {"status": "Call initiated", "call_sid": call.sid}
