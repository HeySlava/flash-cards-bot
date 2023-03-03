from __future__ import annotations

from aiogram.types import CallbackQuery
from aiogram.types import Message
from const import Commands
from services import user_service


async def start_handler(m: Message):
    user_service.init_user(user_id=m.from_user.id)
    await m.answer('Hi, I\'m a bot. How can I help you?')


async def help_handler(m: Message):
    user_service.init_user(user_id=m.from_user.id)
    await m.answer('This is a help message.')


async def process_callback_query(c: CallbackQuery):
    callback_data = c.data
    await c.bot.answer_callback_query(c.id)
    await c.bot.send_message(
            c.from_user.id,
            f'You pressed {callback_data}',
        )


def register(dp):
    dp.register_message_handler(start_handler, commands=Commands.START.value)
    dp.register_message_handler(help_handler, commands=Commands.HELP.value)
    # dp.register_callback_query_handler(
    #         process_callback_query,
    #         lambda c: c.data,
    #     )
