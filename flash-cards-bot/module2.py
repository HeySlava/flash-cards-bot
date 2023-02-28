from __future__ import annotations

from aiogram import types


async def message_handler(message: types.Message):
    await message.answer('I received a message!')
