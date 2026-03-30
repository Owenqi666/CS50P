from seasons import get_minutes, minutes_to_words
from datetime import date

def test_minutes_one_year():
    assert get_minutes("2025-03-30") == 365 * 24 * 60

def test_minutes_to_words():
    assert minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"

def test_invalid_date():
    try:
        get_minutes("not-a-date")
    except SystemExit:
        pass