from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
<<<<<<< HEAD

# Import DB initialization
from app.db.database import initialize_all_tables

# Import all routers
=======
from app.db.database import initialize_all_tables
>>>>>>> origin/main
from app.api.routes.voice.twilio_voice_routes import router as twilio_router
from app.api.routes.pnr_status.pnr_status import router as pnr_router
from app.api.routes.complaints.complaints import router as complaints_router
from app.api.routes.emergency.emergency import router as emergency_router
from app.api.routes.train_schedule.train_schedule import router as train_schedule_router
from app.api.routes.seat_availability.seat_availability import router as seat_router
from app.api.routes.refunds.refunds import router as refunds_router

# -----------------------------------------------------------
# 1️⃣ Initialize FastAPI app
# -----------------------------------------------------------
app = FastAPI(
    title="Indian Railways IVR System",
    description="AI-enabled conversational IVR backend integrated with Twilio",
<<<<<<< HEAD
    version="1.0.0",
)

# -----------------------------------------------------------
# 2️⃣ Add CORS (for Twilio + local dev)
# -----------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
=======
    version="1.0.0"
)

# -----------------------------------------------------------
# 2️⃣ Add CORS middleware (for Twilio + local dev)
# -----------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later
>>>>>>> origin/main
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------
<<<<<<< HEAD
# 3️⃣ FastAPI Lifespan Startup Event
=======
# 3️⃣ Initialize database tables on startup
>>>>>>> origin/main
# -----------------------------------------------------------
@app.on_event("startup")
def startup_event():
    print("🚂 Initializing all database tables...")
    initialize_all_tables()
    print("✅ All database tables are ready.")

# -----------------------------------------------------------
<<<<<<< HEAD
# 4️⃣ Register All Routers
# -----------------------------------------------------------
app.include_router(twilio_router)
app.include_router(pnr_router)
app.include_router(complaints_router)
app.include_router(emergency_router)
app.include_router(train_schedule_router)
app.include_router(seat_router)
app.include_router(refunds_router)

# -----------------------------------------------------------
# 5️⃣ Root Endpoint
=======
# 4️⃣ Include all route modules
# -----------------------------------------------------------
app.include_router(twilio_router)          # Voice call routing via Twilio
app.include_router(pnr_router)             # PNR status service
app.include_router(complaints_router)      # Complaints registration service
app.include_router(emergency_router)       # Emergency helpdesk
app.include_router(train_schedule_router)  # Train schedule info
app.include_router(seat_router)            # Seat availability
app.include_router(refunds_router)         # Refund status tracking

# -----------------------------------------------------------
# 5️⃣ Root endpoint for testing
>>>>>>> origin/main
# -----------------------------------------------------------
@app.get("/")
def root():
    return {"message": "🚉 Indian Railways IVR API is running successfully!"}

# -----------------------------------------------------------
<<<<<<< HEAD
# 6️⃣ Health Check Endpoint (Needed for Unit Tests)
# -----------------------------------------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}

# -----------------------------------------------------------
# Run with:
#    uvicorn main:app --reload
# -----------------------------------------------------------
=======
# 6️⃣ Run using: uvicorn main:app --reload
# -----------------------------------------------------------
# Once running, connect ngrok to this port (default 8000)
# Example: ngrok http 8000
>>>>>>> origin/main
