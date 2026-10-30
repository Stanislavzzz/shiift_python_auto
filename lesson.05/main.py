import logging
import asyncio
from aiogram import Bot, Dispatcher

import config
from handlers.common import router as command_handler
from handlers.inline_handlers import router as inline_handler
from handlers.echo_message import router as text_handler
from handlers.career_choice import router as hr_handler



async def main():
    TOKEN_API = config.TOKEN_TG

    # Включаем логирование
    logging.basicConfig(level=logging.INFO)

    # Инициализация бота
    bot = Bot(token=TOKEN_API)
    dp = Dispatcher()

    dp.include_router(command_handler)
    dp.include_router(hr_handler)
    dp.include_router(text_handler)

    dp.include_router(inline_handler)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
