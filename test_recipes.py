#2.1
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

#2.2
import pytest
from recipe import Ingredient,Recipe

def test_in():
    rec = Recipe("Суп",[])
    assert rec.title == "Суп"
    assert len(rec) == 0

def test_add1():
    rec = Recipe("Суп",[])
    ing1 = Ingredient("Вода",500,"мл")
    rec.add_ingredient(ing1)
    assert len(rec) == 1
    assert rec.ings[0].quantity == 500.0

def test_add2():
    rec = Recipe("Суп",[])
    rec.add_ingredient(Ingredient("Вода",500,"мл"))
    rec.add_ingredient(Ingredient("Вода",200,"мл"))
    
    assert len(rec) == 1
    assert rec.ings[0].quantity == 700.0

def test_scale1():
    rec = Recipe("Суп",[])
    rec.add_ingredient(Ingredient("Вода",500,"мл"))
    rec2 = rec.scale(2)
    
    assert rec2.ings[0].quantity == 1000.0
    assert rec.ings[0].quantity == 500.0

def test_scale2():
    rec = Recipe("Суп", [])
    with pytest.raises(ValueError):
        rec.scale(0)

def test_len():
    rec = Recipe("Суп", [])
    rec.add_ingredient(Ingredient("Вода",500,"мл"))
    rec.add_ingredient(Ingredient("Соль",10,"г"))
    assert len(rec) == 2

def test_str():
    rec = Recipe("Суп", [])
    rec.add_ingredient(Ingredient("Вода",500,"мл"))
    rec.add_ingredient(Ingredient("Соль",10,"г"))
    expected = "Суп: Вода: 500.0 мл, Соль: 10.0 г"
    assert str(rec) == expected
