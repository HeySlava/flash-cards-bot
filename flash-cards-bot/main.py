# bot.py
from __future__ import annotations

import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.types import BotCommand
from menu import menu_handler
from menu import process_callback_query
from module1 import help_handler
from module1 import start_handler
from module2 import message_handler
from settings import ADMIN_ID
from settings import TOKEN

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create bot and dispatcher instances
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Register handlers from modules
dp.register_message_handler(start_handler, commands=['start'])
dp.register_message_handler(help_handler, commands=['help'])
dp.register_message_handler(menu_handler, commands=['menu'])
dp.register_callback_query_handler(
        process_callback_query,
        lambda c: c.data == 'tests',
    )

dp.register_message_handler(message_handler)


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
