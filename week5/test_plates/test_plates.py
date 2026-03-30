from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True

def test_tooshort():
    assert is_valid("C") == False

def test_toolong():
    assert is_valid("CS50000000") == False

def test_wrongstart():
    assert is_valid("50CS") == False

def test_alpha_after_num():
    assert is_valid("CS50P") == False

def test_startzero():
    assert is_valid("CS05") == False

def test_symbol():
    assert is_valid("CS50¥") == False