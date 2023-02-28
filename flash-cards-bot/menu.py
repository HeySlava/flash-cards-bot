from __future__ import annotations

from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import Message


# Define the command handler
async def menu_handler(message: Message):
    sets = InlineKeyboardButton('Работа с сетами', callback_data='sets')
    tests = InlineKeyboardButton('Тесты', callback_data='tests')
    writing = InlineKeyboardButton('Тесты с вводом', callback_data='writing')
    keyboard = InlineKeyboardMarkup()
    keyboard.row(sets)
    keyboard.row(tests)
    keyboard.row(writing)

    await message.answer(
            'Это все доступные опции на данный момент',
            reply_markup=keyboard,
        )


async def process_sets(c: CallbackQuery):
    keyboard = InlineKeyboardMarkup()
    new_set = InlineKeyboardButton('Создать новый сет', callback_data='new_set')
    delete_set = InlineKeyboardButton('Удалить сет', callback_data='delete_set')
    current = InlineKeyboardButton('Выбрать существующий', callback_data='exists')
    keyboard.row(new_set)
    keyboard.row(delete_set)
    keyboard.row(current)

    await c.message.answer(
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
