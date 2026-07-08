import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from calculatrice import additionner, soustraire, multiplier, diviser, modulo
import pytest


def test_additionner():
    assert additionner(2, 3) == 5
    assert additionner(-1, 1) == 0


def test_soustraire():
    assert soustraire(10, 4) == 6
    assert soustraire(0, 5) == -5


def test_multiplier():
    assert multiplier(3, 4) == 12
    assert multiplier(-2, 3) == -6


def test_diviser():
    assert diviser(10, 2) == 5.0
    assert diviser(7, 2) == 3.5


def test_diviser_par_zero():
    with pytest.raises(ValueError, match="Division par zéro impossible"):
        diviser(5, 0)


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(9, 3) == 0


def test_modulo_par_zero():
    with pytest.raises(ValueError, match="Modulo par zéro impossible"):
        modulo(5, 0)
