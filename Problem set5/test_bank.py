from bank import money

def test_zero():
    assert money("hello") == "0"
def test_twenty():
    assert money("hi") == "20"
def test_hundred():
    assert money("Good morning!") == "100"