import asyncio
import os
import requests  # ✅ Правильно

# 1. Получаем токен
token = os.getenv("BOT_TOKEN")

# 2. КРИТИЧЕСКИ ВАЖНО: Проверяем, что токен вообще есть
if not token:
    print("❌ ОШИБКА: Переменная окружения BOT_TOKEN не найдена!")
    print("👉 Проверь Settings -> Secrets and variables -> Actions в репозитории.")
    exit(1) # Останавливаем скрипт, чтобы не слать мусор в Telegram

# 3. Формируем URL
url = f"https://api.telegram.org/bot{token}/getUpdates"

# 4. Делаем запрос
response = requests.get(url)
data = response.json()

# 5. Выводим ответ в лог, чтобы видеть, что пришло
print(f"📡 Ответ от Telegram: {data}")

if not data.get("ok"):
    print(f"⚠️ Telegram вернул ошибку: {data}")
