import asyncio
import logging
from codeop import compile_command
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F

from app.handlers import router
from config import TOKEN
from app import handlers, hand_foodmall, hand_prost, hand_pinterest, hand_museum



# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(TOKEN) ## https://t.me/susPiterbot
# Диспетчер
dp = Dispatcher()

# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(handlers.router)
    dp.include_router(hand_foodmall.router)
    dp.include_router(hand_prost.router)
    dp.include_router(hand_pinterest.router)
    dp.include_router(hand_museum.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())