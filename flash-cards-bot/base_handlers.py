from __future__ import annotations

from aiogram import types


async def start_handler(message: types.Message):
    await message.answer('Hi, I\'m a bot. How can I help you?')


async def help_handler(message: types.Message):
    await message.answer('This is a help message.')


def register_base_handlers(dp):
    dp.register_message_handler(start_handler, commands='start')
    dp.register_message_handler(help_handler, commands='help')
