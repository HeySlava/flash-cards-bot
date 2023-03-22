from __future__ import annotations

import datetime as dt
import uuid
from typing import List
from typing import Optional

import sqlalchemy as sa
from const import States
from data.basemodel import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Set(Base):
    __tablename__ = 'sets'

    id: Mapped[str] = mapped_column(
            primary_key=True,
            default=lambda: str(uuid.uuid4()).replace('-', ''),
        )
    name: Mapped[str] = mapped_column(unique=True)
    cdate: Mapped[dt.datetime] = mapped_column(
            sa.DateTime,
            default=dt.datetime.utcnow,
        )
    udate: Mapped[dt.datetime] = mapped_column(
            sa.DateTime,
            default=dt.datetime.utcnow,
        )
    user_id: Mapped[int] = mapped_column(sa.ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='sets')
    cards: Mapped[List['Card']] = relationship(
            back_populates='set_',
            cascade='all, delete',
        )


class Card(Base):
    __tablename__ = 'cards'

    term: Mapped[str] = mapped_column(
            primary_key=True,
        )
    definition: Mapped[str] = mapped_column(sa.String, nullable=True)
    cdate: Mapped[dt.datetime] = mapped_column(
            sa.DateTime,
            default=dt.datetime.utcnow,
        )
    udate: Mapped[dt.datetime] = mapped_column(
            sa.DateTime,
            default=dt.datetime.utcnow,
        )
    set_id: Mapped[int] = mapped_column(sa.ForeignKey('sets.id'))
    set_: Mapped['Set'] = relationship(back_populates='cards')


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
            primary_key=True,
        )
    state: Mapped[States] = mapped_column(nullable=True)
    cdate: Mapped[dt.datetime] = mapped_column(
            sa.DateTime,
            default=dt.datetime.utcnow,
        )
    udate: Mapped[dt.datetime] = mapped_column(
            sa.DateTime,
            default=dt.datetime.utcnow,
        )
    current_set: Mapped[Optional[str]] = mapped_column(nullable=True)
    sets: Mapped[List['Set']] = relationship(
            back_populates='user',
        )
