import pytest
from main import count_vowels


@pytest.mark.parametrize("test_input, expected", [
    # только гласные
    ("аеёиоуыэюяаеёиоуыэюя", 20),
    # ни одной гласной
    ("бвгджзйклмнпрстфхцчшщъь", 0),
    # смешанные строки
    ("Восемнадцатое июля", 9),
    ("ВоСеМнАдЦаТоЕ ИюЛя", 9),
    ("1234567890!@#$%?/*", 0),
])
def test_count_vowels(test_input, expected):
    assert count_vowels(test_input) == expected
