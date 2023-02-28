from __future__ import annotations

from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import Message


new_set = InlineKeyboardButton('Работа с сетами', callback_data='new_set')
tests = InlineKeyboardButton('Тесты', callback_data='tests')
writing = InlineKeyboardButton('Тесты с вводом', callback_data='writing')

# Group the buttons into rows and columns
keyboard = InlineKeyboardMarkup()
keyboard.row(new_set)
keyboard.row(tests)
keyboard.row(writing)


# Define the command handler
async def menu_handler(message: Message):
    await message.answer(
            'Это все доступные опции на данный момент',
            reply_markup=keyboard,
        )


async def process_callback_query(c: CallbackQuery):
    callback_data = c.data
    await c.bot.answer_callback_query(c.id)
    await c.bot.send_message(
            c.from_user.id,
            f'You pressed {callback_data}',
        )
