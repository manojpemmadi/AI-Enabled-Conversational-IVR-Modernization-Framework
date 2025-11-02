# 🚆 AI-Enabled Conversational IVR Modernization Framework  
**Indian Railways Smart IVR System (FastAPI + Twilio + SQLite)**  

---

## 🧠 Project Overview  
The **AI-Enabled Conversational IVR System** modernizes the Indian Railways’ traditional IVR into a **smart, speech-driven platform**.  
Passengers can call a Twilio-powered number and interact using **natural voice commands**, enabling real-time access to essential services like:  
- 🎟️ **PNR Status Checking**  
- 📝 **Complaints Registration**  
- 🚨 **Emergency Assistance**  
- 🕓 **Train Schedule Inquiry**  
- 💺 **Seat Availability Checking**  
- 💰 **Refund Status Tracking**  

The backend uses **FastAPI** with a **SQLite database**, integrated with **Twilio Voice API** to manage speech input, transcriptions, and dynamic call routing.  

---

## ⚙️ Tech Stack  
| Component | Technology Used |
|------------|----------------|
| **Backend Framework** | FastAPI |
| **Database** | SQLite |
| **Voice Gateway** | Twilio Voice API |
| **Tunneling Tool** | Ngrok |
| **Programming Language** | Python 3.11 |
| **Environment Management** | python-dotenv |
| **Web Server** | Uvicorn |

---

## 🏗️ System Architecture  

The system follows a **modular and event-driven architecture** built around FastAPI routes.  
When a user makes a call through Twilio, the following sequence occurs:

1. **Call Initialization:**  
   Twilio forwards the incoming call request to the `/voice/incoming` endpoint of the FastAPI backend via the **Ngrok public URL**.

2. **Speech Capture and Transcription:**  
   The IVR greets the caller and records their query. Twilio automatically performs **speech-to-text transcription**.

3. **Intent Detection:**  
   The backend analyzes the transcribed text to detect the intent — e.g., whether the user wants to check PNR, file a complaint, or ask for emergency help.

4. **Dynamic Routing:**  
   Based on the intent, the system dynamically redirects the call to the corresponding route module (e.g., `/pnr_status`, `/complaints`, `/refunds`, etc.).

5. **Response Delivery:**  
   The system responds using Twilio’s **TwiML** (Twilio Markup Language), generating voice responses to guide the caller.

6. **Database Interaction:**  
   Data such as complaint details, PNR records, and refund queries are fetched or updated from the **SQLite database**.

This architecture ensures high modularity, easy debugging, and scalable extension for future services.

Traditional IVR systems used by Indian Railways are often slow, confusing, and rely on rigid keypad inputs, making it difficult for passengers to access information quickly. This project overcomes these issues by introducing an AI-enabled **conversational IVR system** that understands natural voice commands, automates responses, and intelligently routes queries—providing a faster, smarter, and more user-friendly experience.




