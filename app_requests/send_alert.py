import requests

def send_push(title, message):
    data = {
        "token": "your_token",
        "user": "your_user_key",
        "title": title,
        "message": message
    }
    requests.post("https://api.pushover.net/1/messages.json", data=data)
