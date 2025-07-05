
import time
from pushover_sender import send_push

def run_autonomous_cycle():
    while True:
        try:
            send_push("🟢 VALOR SYSTEM: Автопуш працює. Оновлення кожну годину.")
            print("✅ Пуш відправлено. Очікуємо 1 годину...")
            time.sleep(3600)  # чекати 1 годину
        except Exception as e:
            print(f"❌ Помилка під час надсилання пуша: {e}")
            time.sleep(300)  # чекати 5 хв перед повтором

if __name__ == "__main__":
    run_autonomous_cycle()
