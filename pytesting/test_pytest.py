import pytest

def testing():
    a = 5
    b = 4
    assert a * b == 20, "It doesn't work it should be 20"
    assert a * b == 3, "Failed, should be 3"
