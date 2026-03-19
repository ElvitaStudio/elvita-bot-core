import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.handlers.user import router as user_router

load_dotenv()

async def main():
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()

    # Подключаем наши обработчики (хэндлеры)
    dp.include_router(user_router)

    print("Бот запущен корректно (модульная структура)...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен.")