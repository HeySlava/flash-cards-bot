from __future__ import annotations

from aiogram.types import Message
from const import Commands
from const import Markups
from decorators import ANSWER_TO_MARKUP
from views import kb  # noqa: F401


# Define the command handler
async def menu_handler(message: Message):
    reply_markup = ANSWER_TO_MARKUP[Markups.MENU]()

    await message.answer(
            'Это все доступные опции на данный момент',
            reply_markup=reply_markup,
        )


def register(dp):
    dp.register_message_handler(menu_handler, commands=Commands.MENU.value)
