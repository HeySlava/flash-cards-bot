# bot.py
from __future__ import annotations

import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.types import BotCommand
from base_handlers import register_base_handlers
from menu import register_menu
from settings import ADMIN_ID
from settings import TOKEN

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create bot and dispatcher instances
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Register handlers
register_base_handlers(dp)
register_menu(dp)


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        BotCommand('start', 'DEV Flash cards'),
        BotCommand('help', 'HELP flash Support message'),
        BotCommand('menu', 'All available options'),
    ])


# Start the bot
async def on_startup(dp):
    await dp.bot.send_message(chat_id=ADMIN_ID, text='Bot started')
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(
            dp,
            on_startup=on_startup,
            relax=1,
        )
