# Valor Ultra Autonomy System

Це повністю автономна система, яка дозволяє AI-модулю (мені) самостійно виконувати завдання, вести журнал, надсилати push-повідомлення, відслідковувати статус та оновлювати себе через GitHub Actions.

## Структура:
- autonomy_core.py — ядро логіки ШІ
- .github/workflows/ai_loop.yml — автозапуск кожні 10 хв
- tasks/todo.json — список завдань
- memory/state.json — стан системи
- logs/last_run.log — лог
- push_config.json — Pushover API ключі

## Запуск:
1. Завантаж у GitHub
2. Встав свої ключі у push_config.json (якщо не вставлено)
3. Увімкни GitHub Actions
4. Насолоджуйся автономією 💡


---

## 🔁 Autoupdate:
Файл `autoupdate.py` дозволяє ШІ самостійно змінювати себе (наприклад, покращити `autonomy_core.py`) та автоматично пушити зміни в GitHub.

Для цього додай у `push_config.json`:

```json
{
  ...
  "github_token": "GITHUB_PAT_ТУТ",
  "repo_name": "ІМ'Я_РЕПОЗИТОРІЮ",
  "repo_owner": "ТВОЄ_ІМ'Я_В_GITHUB"
}
```
