import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Подключаем роутер с нашими обработчиками
    dp.include_router(router)
    
    print("✅ Бот-помощник успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("❌ Бот остановлен пользователем")