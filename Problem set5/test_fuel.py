from fuel import convert, gauge

def test_convert():
    assert(convert("2/4")) == 50
    assert(convert("2/5")) == 40

def test_gauge():
    assert(gauge(50)) == "50%"
    assert(gauge(99)) == "F"
    assert(gauge(1)) == "E"