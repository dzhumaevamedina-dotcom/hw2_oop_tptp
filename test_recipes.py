import pytest
from recipe import Ingredient

def test_ing():
    x = Ingredient("Масло",250,"мл")
    assert x.quantity == 250.0

def test_str():
    x = Ingredient("Яйцо",3,"шт")
    assert str(x) == "Яйцо: 3.0 шт"

def test_repr():
    x = Ingredient("Яйцо",3,"шт")
    assert repr(x) == "Ingredient('Яйцо',3.0,'шт')"

def test_eq():
    a = Ingredient("Сахар",100,"г")
    b = Ingredient("Сахар",200,"г")
    c = Ingredient("Мука",100,"г")
    d = Ingredient("Сахар",100,"кг")
    assert a == b
    assert a != c
    assert a != d

def test_err():
    x = Ingredient("Масло",250,"мл")
    with pytest.raises(ValueError, match="Количество должно быть положительным"):
        x.quantity = -25