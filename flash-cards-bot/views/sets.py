from __future__ import annotations

from aiogram.types import CallbackQuery
from aiogram.types import Message
from const import Markups
from const import MenuButtons
from const import SetButtons
from const import States
from decorators import ANSWER_TO_MARKUP
from services import set_service
from services import user_service
from sqlalchemy.exc import IntegrityError


async def process_sets(c: CallbackQuery):
    reply_markup = ANSWER_TO_MARKUP[Markups.SET]()
    await c.message.answer(
            'Это все доступные опции на данный момент',
            reply_markup=reply_markup,
        )


async def new_set(c: CallbackQuery):
    await c.bot.answer_callback_query(
            c.id,
            text='Введи имя нового сета')
    await c.message.answer(
            'Введи имя нового сета',
        )
    user_service.update_state(
            user_id=c.from_user.id,
            state=States.INPUT_SET_NAME,
        )


async def process_new_set(m: Message):
    try:
        set_ = set_service.new_set(name=m.text, user_id=m.from_user.id)
        text = f'сет добавлен {set_.name=}'
    except IntegrityError:
        text = 'Конфликт'

    await m.answer(text)

    user_service.update_state(
            user_id=m.from_user.id,
            state=States.DEFAULT,
        )


def register(dp):
    dp.register_callback_query_handler(
            process_sets,
            lambda c: c.data == MenuButtons.WORK_WITH_SETS,
        )
    dp.register_callback_query_handler(
            new_set,
            lambda c: c.data == SetButtons.NEW_SET,
        )
    dp.register_message_handler(
            process_new_set,
            lambda m: (
                user_service.get_user_by_id(
                    m.from_user.id).state == States.INPUT_SET_NAME,
            )
        )
