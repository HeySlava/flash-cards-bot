from __future__ import annotations

import functools


ANSWER_TO_MARKUP = {}


def register_markup(func=None, *, kw: str):
    if func is None:
        return lambda func: register_markup(func, kw=kw)

    ANSWER_TO_MARKUP[kw] = func

    @functools.wraps(func)
    async def inner(*args, **kwargs):
        await func(*args, **kwargs)

    return inner
