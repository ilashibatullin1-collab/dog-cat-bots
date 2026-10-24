import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiohttp import TCPConnector
from aiogram.client.session.aiohttp import AiohttpSession

# Получаем токен из переменной окружения (НЕ из кода!)
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("Не найден BOT_TOKEN! Проверь настройки в GitHub Secrets.")

# Фикс сети: чтобы не было зависаний (таймаутов)
connector = TCPConnector()
session = AiohttpSession(connector=connector)
bot = Bot(token=TOKEN, session=session)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="🧥 Гардероб"))
    builder.add(types.KeyboardButton(text="🛍 Магазин"))
    builder.add(types.KeyboardButton(text="👤 Профиль"))

    await message.answer(
        "Привет! Выбирай, что хочешь:",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )

@dp.message(F.text.in_(["🧥 Гардероб", "🛍 Магазин", "👤 Профиль"]))
async def handle_buttons(message: types.Message):
    if message.text == "🧥 Гардероб":
        await message.answer("🎒 Тут будет твой гардероб: одежда для собаки и кошки!")
    elif message.text == "🛍 Магазин":
        await message.answer("💰 Магазин: покупай одежду за звёзды!")
    elif message.text == "👤 Профиль":
        await message.answer("👤 Твой профиль и баланс звёзд.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
