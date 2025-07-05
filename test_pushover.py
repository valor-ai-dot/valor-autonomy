import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("PUSHOVER_TOKEN")
USER_KEY = os.getenv("PUSHOVER_USER_KEY")

resp = requests.post("https://api.pushover.net/1/messages.json", data={
    "token": TOKEN,
    "user": USER_KEY,
    "message": "🧠 Сигнал від ШІ: Pushover підключено успішно!",
})

print("✅ Відправлено" if resp.status_code == 200 else f"❌ Помилка: {resp.text}")
