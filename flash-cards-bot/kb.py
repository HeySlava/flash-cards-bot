from __future__ import annotations

from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from decorators import register_markup


@register_markup(kw='/menu')
def menu_markup() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    sets = InlineKeyboardButton('Работа с сетами', callback_data='sets')
    tests = InlineKeyboardButton('Тесты', callback_data='tests')
    writing = InlineKeyboardButton('Тесты с вводом', callback_data='writing')
    keyboard = InlineKeyboardMarkup()
    keyboard.row(sets)
    keyboard.row(tests)
    keyboard.row(writing)
    return keyboard


@register_markup(kw='sets')
def set_markup() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    new_set = InlineKeyboardButton('Создать новый сет', callback_data='new_set')
    delete_set = InlineKeyboardButton('Удалить сет', callback_data='delete_set')
    current = InlineKeyboardButton('Выбрать существующий', callback_data='exists')
    keyboard.row(new_set)
    keyboard.row(delete_set)
    keyboard.row(current)
    return keyboard
