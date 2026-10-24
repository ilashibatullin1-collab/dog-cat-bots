import asyncio
import os
from aiohttp import ClientSession

async def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN не найден! Проверь секреты в GitHub Actions.")

    async with ClientSession() as session:
        # Получаем обновления (getUpdates)
        # offset=0 означает, что мы хотим получить все старые сообщения, 
        # чтобы не застрять в цикле, если бот уже получал сообщения ранее.
        async with session.get(f"https://api.telegram.org/bot{token}/getUpdates?offset=0") as resp:
            data = await resp.json()
            print("Получены обновления:", data)

        # Пример отправки сообщения (замените CHAT_ID на свой ID или оставьте логику получения ID из getUpdates)
        # Для теста можно отправить сообщение самому себе, если знаешь свой chat_id
        # chat_id = "ТВОЙ_ID" 
        # async with session.post(f"https://api.telegram.org/bot{token}/sendMessage", 
        #                         json={"chat_id": chat_id, "text": "Бот на aiohttp работает!"}) as resp:
        #     print(await resp.json())

        print("Бот успешно выполнил запрос и завершил работу.")

if __name__ == "__main__":
    asyncio.run(main())

