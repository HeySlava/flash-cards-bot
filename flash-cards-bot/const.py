from __future__ import annotations

from enum import Enum
from enum import IntEnum


class MenuButtons(str, Enum):
    WORK_WITH_SETS = 'Работа с сетами'
    # TESTS = 'Тесты'
    # INPUT_TESTS = 'Тесты с вводом'


class MenuLevels(IntEnum):
    GREETING = 0


class Markups(str, Enum):
    MENU = 'menu'
    SET = 'set'
    WORK_WITH_SET = 'Process my set'


class SetButtons(str, Enum):
    NEW_SET = 'Создать новый сет'
    CHANGE_SET_NAME = 'Введи новое имя сета'


class Commands(str, Enum):
    START = 'start'
    MENU = 'menu'
    HELP = 'help'


class States(str, Enum):
    INPUT_SET_NAME = 'Введи номер сета'
    RENAME_SET = 'Изменить название сета'
    DELETE_SET = 'Удалить набор полностью'
    DEFAULT = None
