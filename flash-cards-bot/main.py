# bot.py
from __future__ import annotations

import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.types import BotCommand
from data import db_session
from settings import settings
from views import base_handlers
from views import menu

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create bot and dispatcher instances
bot = Bot(token=settings.token)
dp = Dispatcher(bot)

# Register handlers
base_handlers.register(dp)
menu.register(dp)


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        BotCommand('start', 'DEV Flash cards'),
        BotCommand('help', 'HELP flash Support message'),
        BotCommand('menu', 'All available options'),
    ])


# Start the bot
async def on_startup(dp):
    db_session.global_init(conn_str=settings.conn_str)
    await dp.bot.send_message(chat_id=settings.admin_id, text='Bot started')
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(
            dp,
            on_startup=on_startup,
            relax=1,
        )
