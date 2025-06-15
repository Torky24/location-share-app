from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from twilio.rest import Client
import os
from dotenv import load_dotenv
from pydantic import BaseModel

# Load environment variables
load_dotenv()

app = FastAPI()

# Create static directory if it doesn't exist
static_dir = "static"
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")

class LocationData(BaseModel):
    latitude: float
    longitude: float
    accuracy: str = None
    city: str = None
    country: str = None
    method: str = None

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/share-location")
async def share_location(location: LocationData):
    try:
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # Create message with location
        location_info = f"Latitude: {location.latitude}\nLongitude: {location.longitude}"
        
        if location.city and location.country:
            location_info += f"\nLocation: {location.city}, {location.country}"
        
        if location.accuracy:
            location_info += f"\nAccuracy: {location.accuracy}"
        
        message_text = f"New location shared!\n{location_info}\nView on Google Maps: https://www.google.com/maps?q={location.latitude},{location.longitude}"
        
        # Send SMS message
        message = client.messages.create(
            body=message_text,
            from_=TWILIO_PHONE_NUMBER,
            to=WHATSAPP_NUMBER
        )
        
        return {"status": "success", "message": "Location shared successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 