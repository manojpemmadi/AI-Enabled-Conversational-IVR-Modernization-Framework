# 🚆 AI-Enabled Conversational IVR Modernization Framework  
### Smart Voice-Based IVR for Indian Railways  
#### (FastAPI + Twilio + SQLite + Render Deployment)

---

## 🌐 Live Deployment  
Your backend is deployed on Render and publicly accessible at:  

🔗 **https://ai-enabled-conversational-ivr-69hh.onrender.com**

---

## 🧠 Project Overview  
The **AI-Enabled Conversational IVR Modernization Framework** transforms the traditional Indian Railways IVR into an **intelligent, voice-driven conversational system**.  
Passengers can speak naturally, and the system automatically understands their request, processes it, and responds instantly.

### Supported Services  
- 🎟️ PNR Status Inquiry  
- 📝 Complaint Registration  
- 🚨 Emergency Assistance  
- 🕓 Train Schedule Inquiry  
- 💺 Seat Availability Check  
- 💰 Refund Status Tracking  

Built using **FastAPI**, integrated with **Twilio Voice API**, and powered by a **SQLite database**, the system delivers a faster and more user-friendly IVR experience.

---

## 🚀 Key Features  
- Fully **speech-enabled** IVR system  
- Automatic speech-to-text transcription (Twilio)  
- Smart **intent detection** and routing  
- Modular API structure  
- Real-time voice responses using **TwiML**  
- SQLite-backed complaint, refund, and PNR handling  
- **Cloud-hosted** on Render  
- Secure environment variable management (`.env`)  

---

## ⚙️ Tech Stack  
| Component | Technology |
|----------|------------|
| Backend Framework | FastAPI |
| Programming Language | Python 3.11 |
| Database | SQLite |
| Voice Gateway | Twilio Voice API |
| Cloud Hosting | Render |
| Local Tunneling | Ngrok |
| Web Server | Uvicorn |
| Environment Management | python-dotenv |

---

## 🏗️ System Architecture  

### 1. Incoming Call  
Caller contacts the Twilio number, and Twilio processes audio + transcription.
## 2. Twilio → FastAPI (Render URL)  
The webhook routes the call to:  

https://ai-enabled-conversational-ivr-69hh.onrender.com/voice/incoming

### 3. Speech Processing  
Twilio sends the transcribed text to `/process_speech`.

### 4. Intent Detection  
FastAPI extracts the user's intent (PNR, complaint, refund, etc.).

### 5. Dynamic Routing  
Each intent is handled by dedicated modules like:  
- `/pnr_status`  
- `/complaints`  
- `/refunds`  
- `/emergency`  
- `/train_schedule`  
- `/seat_availability`  

### 6. Voice Response  
FastAPI generates TwiML, Twilio speaks the response.

### 7. Database Storage  
SQLite stores complaints, PNR records (demo data), and refund info.

---

## 📦 Local Development Setup  

### 1. Clone the repo  
```sh
git clone <your-repo-url>
cd your-project-folder


### 2. Twilio → FastAPI (Render URL)  
The webhook routes the call to:  
