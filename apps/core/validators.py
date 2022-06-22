import re

from django.core.exceptions import ValidationError


def name_validator(name):
    """Проверяет написание ФИО.

    ФИО может быть написано с использованием букв русского и английского
    алфавита, тире и пробела (последние два - необязательны).
    """
    pattern = r"^[a-zA-Zа-яА-ЯёЁ]+[a-zA-Zа-яА-ЯёЁ\s-]*[a-zA-Zа-яА-ЯёЁ]+$"
    match = re.match(pattern, name)
    if match is None:
        raise ValidationError(
            "Это поле может содержать только буквы русского или английского алфавита, "
            "между ними может присутствовать тире и пробел"
        )


def nickname_validator(nickname):
    """Проверяет написание имени/псевдонима.

    Пснвдоним может быть написано с использованием букв русского и английского
    алфавита, цифр, тире и подчеркивания, между ними может присутствовать тире и пробел.
    """
    pattern = r"^[0-9a-zA-Zа-яА-ЯёЁ_-]+[0-9a-zA-Zа-яА-ЯёЁ\s_-]*[0-9a-zA-Zа-яА-ЯёЁ_-]+$"
    match = re.match(pattern, nickname)
    if match is None:
        raise ValidationError(
            "Это поле может содержать только буквы русского или английского алфавита, "
            "цифры, тире и подчеркивания, между ними может присутствовать пробел"
        )
