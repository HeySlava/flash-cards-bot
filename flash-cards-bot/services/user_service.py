from __future__ import annotations

import datetime as dt

from const import States
from data import db_session
from data.models import User
from sqlalchemy.orm import Session


def init_user(
        user_id: int,
) -> User:
    session: Session = db_session.create_session()

    user = session.query(User).where(User.id == user_id).one_or_none()
    if not user:
        user = User(id=user_id)
    user.udate = dt.datetime.utcnow()
    session.add(user)
    session.commit()
    return user


def update_state(
        user_id: int,
        state: States,
) -> User:
    session: Session = db_session.create_session()

    user = session.query(User).where(User.id == user_id).one()
    user.state = state.value
    user.udate = dt.datetime.utcnow()
    session.add(user)
    session.commit()
    return user


def get_user_by_id(
        user_id: int,
) -> User:
    session: Session = db_session.create_session()

    return session.query(User).where(User.id == user_id).one()
