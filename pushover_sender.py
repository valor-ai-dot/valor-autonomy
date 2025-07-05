
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_push(message):
    token = os.getenv("ag6yo1978huogazh76asj8cwmaktih")
    user_key = os.getenv("u7ivc7b8s2f2cwuq3sj6zmn2cthpfc")

    if not token or not user_key:
        raise ValueError("❌ PUSHOVER_TOKEN або USER_KEY не знайдено у .env")

    response = requests.post("https://api.pushover.net/1/messages.json", data={
        "token": token,
        "user": user_key,
        "message": message
    })

    if response.status_code != 200:
        raise Exception(f"❌ Помилка відправки: {response.text}")
