from __future__ import annotations

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.orm import sessionmaker

_factory = None


def global_init(
        conn_str: str,
        debug: bool = False,
) -> None:
    global _factory

    if _factory is not None:
        return

    if not conn_str or not conn_str.strip():
        raise ValueError(f'Wrong conn_str ({conn_str=})')

    engine = sa.create_engine(conn_str, echo=debug)

    _factory = sessionmaker(engine)


def create_session() -> orm.Session:
    global _factory

    if not _factory:
        raise Exception('You have to init your db with global_init()')

    session: orm.Session = _factory()

    try:
        return session
    finally:
        session.close()