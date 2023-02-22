from calc import Calc
import pytest


@pytest.fixture
def calc():
    # all setup for calc here
    return Calc()


def test_add(calc):
    assert calc.add(10, 5) == 15
    assert calc.add(-1, 1) == 0
    assert calc.add(-1, -1) == -2


def test_subtract(calc):
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(-1, 1) == -2
    assert calc.subtract(-1, -1) == 0


def test_multiply(calc):
    assert calc.multiply(10, 5) == 50
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(-1, -1) == 1


def test_dived(calc):
    assert calc.divide(10, 5) == 2
    assert calc.divide(-1, 1) == -1
    assert calc.divide(-1, -1) == 1
    assert calc.divide(5, 2) == 2.5

    with pytest.raises(ValueError) as exc_info:
        calc.divide(10, 0)

    assert str(exc_info.value) == 'Can not divide by zero!'