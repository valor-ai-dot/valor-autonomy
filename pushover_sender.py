
import os
import requests

def send_pushover(title, message):
    token = os.getenv("PUSHOVER_API_TOKEN")
    user_key = os.getenv("PUSHOVER_USER_KEY")

    if not token or not user_key:
        print("❌ Pushover credentials not found in environment variables.")
        return

    payload = {
        "token": token,
        "user": user_key,
        "title": title,
        "message": message
    }

    response = requests.post("https://api.pushover.net/1/messages.json", data=payload)
    if response.status_code == 200:
        print("✅ Pushover message sent successfully.")
    else:
        print(f"❌ Failed to send Pushover message: {response.text}")
