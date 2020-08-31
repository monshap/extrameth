from pytest import approx
from extrameth.sqrt import sqrt

def test_sqrt():
    assert sqrt(4.0) == approx(2.0)
