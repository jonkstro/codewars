from solution import is_square


def test_is_square_negative_number():
    assert is_square(-1) == False

def test_is_square_zero():
    assert is_square(0) == True

def test_is_square_non_square_number():
    assert is_square(3) == False

def test_is_square_perfect_square():
    assert is_square(4) == True
    assert is_square(25) == True

def test_is_square_non_perfect_square():
    assert is_square(26) == False
