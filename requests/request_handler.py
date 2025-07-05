from requests.get_price import get_token_price
from requests.send_alert import send_telegram_alert
from requests.fetch_news import fetch_latest_news

def handle_request(request_type, **kwargs):
    if request_type == "price":
        return get_token_price(kwargs.get("symbol"))
    elif request_type == "alert":
        return send_telegram_alert(kwargs.get("message"), kwargs.get("token"), kwargs.get("chat_id"))
    elif request_type == "news":
        return fetch_latest_news()