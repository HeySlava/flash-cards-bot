from __future__ import annotations

from aiogram import types
from bot import dp


async def start_handler(message: types.Message):
    await message.answer('Hi, I\'m a bot. How can I help you?')


async def help_handler(message: types.Message):
    await message.answer('This is a help message.')

# Register handlers from this module
dp.register_message_handler(start_handler, commands='start')
dp.register_message_handler(help_handler, commands='help')
