import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Загружаем переменные из .env
load_dotenv()

async def main():
    # Инициализация бота и диспетчера
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()

    # Простейший хэндлер прямо тут (позже вынесем в папку handlers)
    @dp.message(CommandStart())
    async def cmd_start(message: types.Message):
        await message.answer(f"Привет! Это официальный бот Elvita Studio. 🚀\nЧем я могу помочь?")

    print("Бот запущен и готов к работе...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен.")