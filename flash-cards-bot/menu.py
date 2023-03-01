from __future__ import annotations

import kb  # noqa: F401
from aiogram.types import CallbackQuery
from aiogram.types import Message
from decorators import ANSWER_TO_MARKUP


# Define the command handler
async def menu_handler(message: Message):
    reply_markup = ANSWER_TO_MARKUP['/menu']()

    await message.answer(
            'Это все доступные опции на данный момент',
            reply_markup=reply_markup,
        )


def register_menu(dp):
    dp.register_message_handler(menu_handler, commands=['menu'])
    dp.register_callback_query_handler(
            process_sets,
            lambda c: c.data == 'sets',
        )
    dp.register_callback_query_handler(
            process_callback_query,
            lambda c: c.data,
        )


async def process_sets(c: CallbackQuery):
    reply_markup = ANSWER_TO_MARKUP['sets']()
    await c.message.answer(
            'Это все доступные опции на данный момент',
            reply_markup=reply_markup,
        )


async def process_callback_query(c: CallbackQuery):
    callback_data = c.data
    await c.bot.answer_callback_query(c.id)
    await c.bot.send_message(
            c.from_user.id,
            f'You pressed {callback_data}',
        )
