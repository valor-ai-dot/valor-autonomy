import json
import requests

with open('push_config.json') as f:
    config = json.load(f)

user_key = config["pushover_user_key"]
app_token = config["pushover_app_token"]

message = "🔔 Автоматичне повідомлення з GitHub Actions!"

data = {
    "token": app_token,
    "user": user_key,
    "message": message
}

requests.post("https://api.pushover.net/1/messages.json", data=data)
