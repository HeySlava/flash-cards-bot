from __future__ import annotations

import logging

from aiogram.types import CallbackQuery
from aiogram.types import Message
from const import Commands
from const import States
from data import db_session
from services import user_service


logger = logging.getLogger(__name__)


async def start_handler(m: Message):
    logger.debug(f'Message from {m.from_user.id=} with {m.text}')
    session = db_session.create_session()

    user_service.init_user(
            user_id=m.from_user.id,
            state=States.DEFAULT,
            session=session,
        )
    await m.answer('Hi, I\'m a bot. How can I help you?')


async def help_handler(m: Message):
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
