from __future__ import annotations

from data.models import Set
from sqlalchemy.orm import Session


def new_set(
        name: str,
        user_id: int,
        session: Session,
) -> Set:
    set_ = Set(name=name, user_id=user_id)
    session.add(set_)
    session.commit()
    return set_


def get_set_by_uuid(
        set_id: str,
        session: Session,
) -> Set:
    return session.query(Set).where(Set.id == set_id).one()
