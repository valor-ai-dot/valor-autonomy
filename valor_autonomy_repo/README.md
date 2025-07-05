# Автономна система Push-сповіщень через GitHub Actions

## Структура:
- main.py — надсилає push-повідомлення через Pushover
- .github/workflows/main.yml — запускає Python-скрипт при кожному push
- push_config.json — встав свої Pushover ключі

## Інструкція запуску:
1. Додай свої ключі у push_config.json
2. Закоміть у GitHub-репозиторій
3. Увімкни GitHub Actions
4. Зроби push або зміну файлу — отримаєш повідомлення
