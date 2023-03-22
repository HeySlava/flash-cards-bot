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
