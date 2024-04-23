from plates import is_valid

def test_length():
    assert is_valid("OUTATIME") == False

def test_first_two():
    assert is_valid("32aaaa") == False
    assert is_valid("FD3432") == True

def test_no_first_zero():
    assert is_valid("CS0343") == False
    assert is_valid("CS3043") == True

def test_no_symbols():
    assert is_valid("CS34%4") == False

def test_no_mid_digits():
    assert is_valid("CS234S") == False