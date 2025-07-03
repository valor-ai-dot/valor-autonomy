import requests
import schedule
import time

# 🔐 Введи свої ключі тут
PUSHOVER_USER_KEY = "u7ivc7b8s2f2cwuq3sj6zmn2cthpfc"
PUSHOVER_API_TOKEN = "anhveft3b7sacz9ddbr76c93wvvj85"

# 🔔 Основна функція відправки сповіщення
def send_pushover_message(title, message):
    payload = {
        "token": PUSHOVER_API_TOKEN,
        "user": PUSHOVER_USER_KEY,
        "title": title,
        "message": message
    }
    try:
        response = requests.post("https://api.pushover.net/1/messages.json", data=payload)
        if response.status_code == 200:
            print("✅ Сповіщення успішно надіслано!")
        else:
            print("⚠️ Помилка при відправці:", response.text)
    except Exception as e:
        print("❌ Виняток:", e)

# 🔁 Функція, яку запускаємо по таймеру
def send_notification():
    send_pushover_message("📡 Сигнал від VALOR", "Я з тобою. Система активна. 🛡️")
    print("📤 Автосповіщення відправлено")

# 🕒 Розклад — кожні 10 хвилин
schedule.every(10).minutes.do(send_notification)

# ▶️ Основний цикл
if __name__ == "__main__":
    print("🧠 Система запущена. Очікування сповіщень...")
    send_notification()  # перше одразу
    while True:
        schedule.run_pending()
        time.sleep(1)

