from __future__ import annotations

import logging

from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from const import Markups
from const import MenuButtons
from const import SetButtons
from data import db_session
from data.models import Set
from decorators import register_markup
from services import user_service


logger = logging.getLogger(__name__)


@register_markup(kw=Markups.MENU)
def menu_markup() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    for b in MenuButtons:
        keyboard.add(InlineKeyboardButton(b, callback_data=b))
    return keyboard


@register_markup(kw=Markups.SET)
def set_markup(user_id: int) -> InlineKeyboardMarkup:
    logger.debug(f'Message {user_id=}')
    session = db_session.create_session()

    user = user_service.get_user_by_id(
            user_id=user_id,
            session=session,
        )

    keyboard = InlineKeyboardMarkup()

    new_set = InlineKeyboardButton(
            SetButtons.NEW_SET,
            callback_data=SetButtons.NEW_SET,
        )
    keyboard.row(new_set)

    for s in user.sets:
        current = InlineKeyboardButton(
                f'{s.name=}',
                callback_data=f'set:{s.id}',
            )
        keyboard.row(current)
    return keyboard


@register_markup(kw=Markups.WORK_WITH_SET)
def existed_set_markup(set_: Set) -> InlineKeyboardMarkup:
    logger.debug(f'Message {set_.id=}')

    keyboard = InlineKeyboardMarkup()

    delete_set = InlineKeyboardButton(
            'Удалить',
            callback_data=f'delete_set:{set_.id}',
        )

    add_new_word = InlineKeyboardButton(
            'Добавить новое слово',
            callback_data=set_.name,
        )

    rename_set_name = InlineKeyboardButton(
            'Изменить название сета',
            callback_data=f'rename_set:{set_.id}',
        )
    keyboard.row(delete_set)
    keyboard.row(add_new_word)
    keyboard.row(rename_set_name)

    for c in set_.cards:
        current = InlineKeyboardButton(
                f'{c.term} - {c.definition}',
                callback_data=c.id,
            )
        keyboard.row(current)
    return keyboard
