from __future__ import annotations

from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from const import Markups
from const import MenuButtons
from const import SetButtons
from decorators import register_markup


@register_markup(kw=Markups.MENU)
def menu_markup() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    for b in MenuButtons:
        keyboard.add(InlineKeyboardButton(b, callback_data=b))
    return keyboard


@register_markup(kw=Markups.SET)
def set_markup() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    new_set = InlineKeyboardButton(
            SetButtons.NEW_SET,
            callback_data=SetButtons.NEW_SET,
        )
    keyboard.row(new_set)
    for i in range(1, 6):
        current = InlineKeyboardButton(
                f'Типо существующий сет {i}',
                callback_data='exists',
            )
        keyboard.row(current)
    return keyboard
