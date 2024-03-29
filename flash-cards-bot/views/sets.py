from __future__ import annotations

import logging

from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.types import Message
from const import Markups
from const import MenuButtons
from const import SetButtons
from const import States
from data import db_session
from decorators import ANSWER_TO_MARKUP
from services import set_service
from services import user_service
from sqlalchemy.exc import IntegrityError
from views.menu import menu_handler


logger = logging.getLogger(__name__)


async def process_sets(c: CallbackQuery):
    session = db_session.create_session()

    user = user_service.get_user_by_id(c.from_user.id, session=session)
    reply_markup = ANSWER_TO_MARKUP[Markups.SET](user)
    await c.answer()

    await c.message.answer(
            'Все ваши наборы на данный момент',
            reply_markup=reply_markup,
        )


async def new_set(c: CallbackQuery):
    session = db_session.create_session()
    await c.bot.answer_callback_query(
            c.id,
            text='Введи имя нового сета')
    await c.message.answer(
            'Введи имя нового сета',
        )
    user_service.update_state(
            user_id=c.from_user.id,
            state=States.INPUT_SET_NAME,
            session=session,
        )


async def process_input_text(m: Message):
    logger.debug(f'Message = {m}')
    session = db_session.create_session()
    user = user_service.get_user_by_id(m.from_user.id, session=session)

    if user.state == States.INPUT_SET_NAME:
        try:
            set_ = set_service.new_set(
                    name=m.text,
                    user_id=m.from_user.id,
                    session=session,
                )
            text = f'сет добавлен {set_.name=}'
        except IntegrityError:
            text = 'Сет с таким названинием уже существует\nПопробуйте еще'
            await m.answer(text)
            return

    elif user.state == States.RENAME_SET and user.current_set is not None:
        try:
            set_ = set_service.rename_set(
                    name=m.text,
                    set_id=user.current_set,
                    session=session,
                )
            text = f'Новое название сета = "{set_.name}"'
        except IntegrityError:
            text = 'Такое имя уже занято\nПопробуйте еще'
            await m.answer(text)
            return

    elif user.state == States.DELETE_SET and user.current_set is not None:
        if m.text.lower() == 'да':
            set_service.delete_set(
                    set_id=user.current_set,
                    session=session,
                )
            text = 'Набор удален'
        else:
            user_service.change_current_set(
                    user_id=m.from_user.id,
                    set_id=None,
                    session=session,
                )
            text = 'Отмена'

    else:
        text = 'Unexpected state'

    await m.answer(text)

    user_service.update_state(
            user_id=m.from_user.id,
            state=States.DEFAULT,
            session=session,
        )
    await menu_handler(m)


async def select_set(c: CallbackQuery):
    logger.debug(f'Callback data = {c.data}')
    set_id = c.data.split(':')[-1]
    session = db_session.create_session()
    set_ = set_service.get_set_by_uuid(set_id=set_id, session=session)

    reply_markup = ANSWER_TO_MARKUP[Markups.WORK_WITH_SET](set_)
    await c.answer()

    time_ftm = '%d.%m.%Y - %H:%M'
    text = (
            'Информация про выбранный набор\n\n'
            f'Set name: {set_.name}\n'
            f'Set id: {set_.id[:10]}\n'
            f'Время создания: {set_.cdate.strftime(time_ftm)}\n'
            f'Время обновления: {set_.udate.strftime(time_ftm)}\n'
        )
    await c.message.answer(
            text,
            reply_markup=reply_markup,
        )


async def rename_set(c: CallbackQuery):
    logger.debug(f'Callback data = {c.data}')
    session = db_session.create_session()
    await c.answer()

    set_id = c.data.split(':')[-1]

    set_ = set_service.get_set_by_uuid(set_id=set_id, session=session)
    user_service.update_state(
            user_id=c.from_user.id,
            state=States.RENAME_SET,
            session=session,
        )
    user_service.change_current_set(
            user_id=c.from_user.id,
            set_id=set_id,
            session=session,
        )
    text = (
            f'Ты хочешь изменить название для набора с именем {set_.name}\n\n'
            'Введи новое название, имей ввиду, оно должно быть уникальным'
        )
    await c.message.answer(text)


async def delete_set(c: CallbackQuery):
    logger.debug(f'Callback data = {c.data}')
    session = db_session.create_session()
    await c.answer()

    set_id = c.data.split(':')[-1]

    set_ = set_service.get_set_by_uuid(set_id=set_id, session=session)
    user_service.update_state(
            user_id=c.from_user.id,
            state=States.DELETE_SET,
            session=session,
        )
    user_service.change_current_set(
            user_id=c.from_user.id,
            set_id=set_id,
            session=session,
        )
    text = (
            f'Ты хочешь набор с именем {set_.name}\n\n'
            'Это безвозвратно\n\n'
            'Уверен? Да/Нет'
        )
    await c.message.answer(text)


def register(dp: Dispatcher):
    dp.register_callback_query_handler(
            process_sets,
            lambda c: c.data == MenuButtons.WORK_WITH_SETS,
        )

    dp.register_callback_query_handler(
            new_set,
            lambda c: c.data == SetButtons.NEW_SET,
        )

    dp.register_callback_query_handler(
            select_set,
            lambda c: c.data.startswith('set'),
        )

    dp.register_callback_query_handler(
            rename_set,
            lambda c: c.data.startswith('rename_set'),
        )

    dp.register_callback_query_handler(
            delete_set,
            lambda c: c.data.startswith('delete_set'),
        )

    dp.register_message_handler(
            process_input_text,
        )
