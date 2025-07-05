import json
import datetime
import requests

def load_state():
    with open('memory/state.json', 'r') as f:
        return json.load(f)

def save_state(state):
    with open('memory/state.json', 'w') as f:
        json.dump(state, f, indent=2)

def load_tasks():
    with open('tasks/todo.json', 'r') as f:
        return json.load(f)

def log(message):
    timestamp = datetime.datetime.now().isoformat()
    with open('logs/last_run.log', 'a') as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)

def send_push(title, message):
    with open('push_config.json') as f:
        cfg = json.load(f)
    data = {
        "token": cfg["pushover_app_token"],
        "user": cfg["pushover_user_key"],
        "title": title,
        "message": message
    }
    requests.post("https://api.pushover.net/1/messages.json", data=data)

def main():
    state = load_state()
    tasks = load_tasks()
    log("🤖 Autonomy cycle started.")

    for task in tasks.get("pending", []):
        log(f"🧠 Task: {task}")
        send_push("Autonomy Task", f"Завдання виконано: {task}")
        state['last_completed'] = task

    tasks["completed"] += tasks["pending"]
    tasks["pending"] = []

    save_state(state)
    with open('tasks/todo.json', 'w') as f:
        json.dump(tasks, f, indent=2)

    log("✅ Autonomy cycle finished.")

if __name__ == "__main__":
    main()
