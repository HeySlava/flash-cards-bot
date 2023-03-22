from __future__ import annotations

from typing import Union

from aiogram.types import CallbackQuery
from aiogram.types import Message
from const import Commands
from const import Markups
from decorators import ANSWER_TO_MARKUP
from views import kb  # noqa: F401


async def menu_handler(input: Union[Message, CallbackQuery]):
    if isinstance(input, CallbackQuery):
        message = input.message
        await input.answer()
    else:
        message = input

    reply_markup = ANSWER_TO_MARKUP[Markups.MENU]()

    await message.answer(
            'Это все доступные опции на данный момент',
            reply_markup=reply_markup,
        )


def register(dp):
    dp.register_message_handler(
            menu_handler,
            commands=Commands.MENU.value,
        )
    dp.register_callback_query_handler(
            menu_handler,
            lambda c: c.data == Commands.MENU,
        )
