from test_twttr.twttr import shorten
    
def test_lower():
    assert shorten("shit") == "sht"

def test_upper():
    assert shorten("SHIT") == "SHT"

def test_num():
    assert shorten("shit666") == "sht666"

def test_symbol():
    assert shorten("shit_!") == "sht_!"

    
