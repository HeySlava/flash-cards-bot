from __future__ import annotations

from aiogram import types


async def start_handler(message: types.Message):
    await message.answer('Hi, I\'m a bot. How can I help you?')


async def help_handler(message: types.Message):
    await message.answer('This is a help message.')
