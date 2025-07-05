import os
import requests
from dotenv import load_dotenv

def send_push(message: str, title: str = "VALOR SYSTEM ⚙️"):
    load_dotenv()
    token = os.getenv("PUSHOVER_API_TOKEN")
    user = os.getenv("PUSHOVER_USER_KEY")

    if not token or not user:
        raise ValueError("Pushover credentials not found in .env")

    response = requests.post("https://api.pushover.net/1/messages.json", data={
        "token": token,
        "user": user,
        "title": title,
        "message": message,
    })

    if response.status_code != 200:
        raise Exception(f"Push failed: {response.status_code} - {response.text}")

    print("✅ Push notification sent successfully.")
