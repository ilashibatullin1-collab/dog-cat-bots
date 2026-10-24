import asyncio
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")
import telebot
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для собак и кошек!")

bot.polling(none_stop=True)

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
