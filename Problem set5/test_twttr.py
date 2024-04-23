from twttr import shorten

def test_shorten():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("I love you") == " lv y"
    assert shorten("TIMCHANWSH") == "TMCHNWSH"

