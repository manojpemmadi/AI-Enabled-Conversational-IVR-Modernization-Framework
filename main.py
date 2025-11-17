from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import DB initialization
from app.db.database import initialize_all_tables

# Import all routers
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
    version="1.0.0",
)

# -----------------------------------------------------------
# 2️⃣ Add CORS (for Twilio + local dev)
# -----------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------
# 3️⃣ FastAPI Lifespan Startup Event
# -----------------------------------------------------------
@app.on_event("startup")
def startup_event():
    print("🚂 Initializing all database tables...")
    initialize_all_tables()
    print("✅ All database tables are ready.")

# -----------------------------------------------------------
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
# -----------------------------------------------------------
@app.get("/")
def root():
    return {"message": "🚉 Indian Railways IVR API is running successfully!"}

# -----------------------------------------------------------
# 6️⃣ Health Check Endpoint (Needed for Unit Tests)
# -----------------------------------------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}

# -----------------------------------------------------------
# Run with:
#    uvicorn main:app --reload
# -----------------------------------------------------------
