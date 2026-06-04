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

#2.3
import pytest
from recipe import Ingredient,Recipe,ShoppingList

def test_add():
    arr = ShoppingList()
    r = Recipe("Пицца", [Ingredient("Мука",100,"г")])
    arr.add_recipe(r,2)
    assert arr.items[0][0].quantity == 200.0

def test_err():
    arr = ShoppingList()
    r = Recipe("Пицца", [])
    with pytest.raises(ValueError):
        arr.add_recipe(r,0)

def test_rem():
    arr = ShoppingList()
    arr.add_recipe(Recipe("Пицца",[Ingredient("Мука", 100, "г")]), 1)
    arr.add_recipe(Recipe("Суп",[Ingredient("Вода", 500, "мл")]), 1)
    arr.remove_recipe("Пицца")
    
    assert len(arr.items) == 1     
    assert arr.items[0][1] == "Суп"  

def test1():
    arr = ShoppingList()
    arr.add_recipe(Recipe("Паста",[Ingredient("Мука", 50, "г"), Ingredient("Яйцо",1,"шт")]), 1)
    arr.add_recipe(Recipe("Пицца",[Ingredient("Мука", 100, "г")]), 1)
    res = arr.get_list()

    assert len(res) == 2
    assert res[0].name == "Мука"    
    assert res[0].quantity == 150.0   
    assert res[1].name == "Яйцо"
    assert res[1].quantity == 1.0

def test2():
    x1 = ShoppingList()
    x2 = ShoppingList()
    x1.add_recipe(Recipe("Пицца",[Ingredient("Мука", 100, "г")]), 1) 
    x2.add_recipe(Recipe("Суп",[Ingredient("Вода", 500, "мл")]), 1)  
    x3 = x1 + x2
    assert len(x3.items) == 2 