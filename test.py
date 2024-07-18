import pytest
from main import count_vowels


@pytest.mark.parametrize("test_input, expected", [
    ("аеёиоуыэюяаеёиоуыэюя", 20),
    ("бвгджзйклмнпрстфхцчшщъь", 0),
    ("Восемнадцатое июля", 9),
    ("ВоСеМнАдЦаТоЕ ИюЛя", 9),
    ("1234567890!@#$%?/*", 0),
])
def test_count_vowels(test_input, expected):
    assert count_vowels(test_input) == expected
