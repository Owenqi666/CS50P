from um import count

def test_single():
    assert count("um") == 1

def test_punctuation():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1

def test_multiple():
    assert count("Um, thanks, um...") == 2

def test_not_word():
    assert count("yummy") == 0
    assert count("album") == 0

def test_case_insensitive():
    assert count("UM") == 1
    assert count("Um") == 1