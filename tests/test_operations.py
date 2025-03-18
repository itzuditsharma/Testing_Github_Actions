from src.math_operations import add, sub

def test_add():
    assert add(1,3) == 4
    assert add(2,5) == 7

def test_sub():
    assert sub(3,4) == -1
    assert sub(7,3) == 4