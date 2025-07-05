import requests
import json

def send_telegram_alert(message, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    requests.post(url, json=data)

def send_pushover_alert(message, user_key, app_token):
    url = "https://api.pushover.net/1/messages.json"
    data = {"token": app_token, "user": user_key, "message": message}
    requests.post(url, data=data)