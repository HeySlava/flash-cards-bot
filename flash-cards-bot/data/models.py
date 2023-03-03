from __future__ import annotations

import datetime as dt

import sqlalchemy as sa
from const import States
from data.basemodel import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
# import uuid


class Set(Base):
    __tablename__ = 'sets'

    # # Try to use name as primary_key
    # id: Mapped[str] = mapped_column(
    #         primary_key=True,
    #         default=lambda: str(uuid.uuid4()).replace('-', ''),
    #     )
    name: Mapped[str] = mapped_column(primary_key=True)
    cdate: Mapped[dt.datetime] = mapped_column(
            sa.DateTime,
            default=dt.datetime.utcnow,
        )
    udate: Mapped[dt.datetime] = mapped_column(
            sa.DateTime,
            default=dt.datetime.utcnow,
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
