from __future__ import annotations

from aiogram.types import CallbackQuery
from aiogram.types import Message
from const import CURRENT_STATE
from const import Markups
from const import MenuButtons
from const import SetButtons
from const import States
from decorators import ANSWER_TO_MARKUP


list_sets = []


async def process_sets(c: CallbackQuery):
    reply_markup = ANSWER_TO_MARKUP[Markups.SET]()
    await c.message.answer(
            'Это все доступные опции на данный момент',
            reply_markup=reply_markup,
        )


async def new_set(c: CallbackQuery):
    global CURRENT_STATE
    await c.message.answer(
            'Введи имя нового сета',
        )
    print('before', CURRENT_STATE)
    CURRENT_STATE = States.INPUT_SET_NAME
    print('after', CURRENT_STATE)


async def process_new_set(m: Message):
    global CURRENT_STATE
    list_sets.append(m.text)

    await m.answer(
            f'Your set name is {m.text}\n\n{str(list_sets)}',
        )
    print('before', CURRENT_STATE)
    CURRENT_STATE = None
    print('after', CURRENT_STATE)


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
            lambda _: CURRENT_STATE == States.INPUT_SET_NAME
        )
