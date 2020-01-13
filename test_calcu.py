import pytest
import calcu

def test_add():
    assert calcu.add(1,2) == 3

def test_mult():
    assert calcu.multiply(3,4) == 12
    
def test_minus():
    assert calcu.subtract(5,3) == 2