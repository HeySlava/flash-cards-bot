from __future__ import annotations

import sqlalchemy as sa
from alembic import command
from alembic.config import Config
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

    engine = sa.create_engine(
            conn_str,
            echo=debug,
            connect_args={
                'check_same_thread': False,
            }
        )

    _factory = sessionmaker(engine)

    alembic_cfg = Config('alembic.ini')
    command.upgrade(alembic_cfg, 'head')
    alembic_cfg.attributes['configure_logger'] = False


def create_session() -> orm.Session:
    global _factory

    if not _factory:
        raise Exception('You have to init your db with global_init()')

    session: orm.Session = _factory()

    try:
        return session
    finally:
        session.close()
