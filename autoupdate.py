import os
import json
import base64
import requests

# Зчитування конфігурації
with open("push_config.json") as f:
    cfg = json.load(f)

GITHUB_TOKEN = cfg.get("github_token")
REPO_NAME = cfg.get("repo_name")
REPO_OWNER = cfg.get("repo_owner")
FILE_PATH = "autonomy_core.py"
COMMIT_MESSAGE = "🤖 Auto-update: core logic improved"

def get_file_sha():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json()["sha"]
    else:
        print("❌ Не вдалося отримати SHA:", r.text)
        return None

def push_update(new_code):
    sha = get_file_sha()
    if not sha:
        return

    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "message": COMMIT_MESSAGE,
        "content": base64.b64encode(new_code.encode()).decode(),
        "sha": sha
    }
    r = requests.put(url, headers=headers, data=json.dumps(data))
    if r.status_code == 200 or r.status_code == 201:
        print("✅ Оновлено!")
    else:
        print("❌ Помилка при пуші:", r.text)

# Пример зміни коду (додати лог-коментар на початок)
with open(FILE_PATH, "r") as f:
    current_code = f.read()

new_code = "# Auto-updated by AI\n" + current_code
push_update(new_code)
