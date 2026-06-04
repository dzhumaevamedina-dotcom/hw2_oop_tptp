import pytest
from recipe import Ingredient

def test_ing():
     obj = Ingredient("Масло",250,"мл")
    assert obj.quantity == 250.0