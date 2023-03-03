from __future__ import annotations

from enum import Enum


class MenuButtons(str, Enum):
    WORK_WITH_SETS = 'Работа с сетами'
    TESTS = 'Тесты'
    INPUT_TESTS = 'Тесты с вводом'


class Markups(str, Enum):
    MENU = 'menu'
    SET = 'set'


class SetButtons(str, Enum):
    NEW_SET = 'Создать новый сет'


class Commands(str, Enum):
    START = 'start'
    MENU = 'menu'
    HELP = 'help'


class States(str, Enum):
    INPUT_SET_NAME = 'Введи номер сета'
    DEFAULT = ''
