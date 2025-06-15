# Location Share Web App

This is a web application that allows users to share their location via WhatsApp. The application uses FastAPI for the backend and a modern frontend with Tailwind CSS.

## Features

- Get user's current location
- Share location via WhatsApp
- Modern and responsive UI
- Real-time status updates

## Prerequisites

- Python 3.7+
- Twilio Account (for WhatsApp integration)
- WhatsApp Business API access

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with the following variables:
   ```
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_phone_number
   WHATSAPP_NUMBER=recipient_whatsapp_number
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Open your browser and navigate to `http://localhost:8000`

## Usage

1. Click the "Share Location" button
2. Allow location access when prompted by your browser
3. The location will be automatically shared via WhatsApp

## Security Notes

- Keep your `.env` file secure and never commit it to version control
- The application requires HTTPS in production for secure location sharing
- Always validate and sanitize user input

## License

MIT 