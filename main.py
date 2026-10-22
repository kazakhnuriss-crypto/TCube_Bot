import asyncio, logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
import config
from handlers import start, casino, chat, ref

async def main():
    bot = Bot(token=config.TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(casino.router)
    dp.include_router(chat.router)
    dp.include_router(ref.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
