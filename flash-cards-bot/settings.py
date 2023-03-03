from __future__ import annotations

from pathlib import Path
from typing import NamedTuple


with open('.env') as f:
    env_dict = {}
    for line in f:
        line = line.strip()
        if line.startswith('#') or not line:
            continue
        key, value = line.split('=', 1)
        env_dict[key] = value


_BASE_DIR = Path(__file__)
_DB_DIR = _BASE_DIR / 'db'
_conn_str = 'sqlite:///' + (_DB_DIR / 'flash.sqlite').as_posix()


class Settings(NamedTuple):
    admin_id: str
    token: str
    base_dir: Path
    conn_str: str


settings = Settings(
        admin_id=env_dict['ADMIN_ID'],
        token=env_dict['FLASH_BOT_TOKEN'],
        conn_str=_conn_str,
        base_dir=_BASE_DIR,
    )
