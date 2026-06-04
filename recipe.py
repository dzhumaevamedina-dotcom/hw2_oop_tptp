class Ingredient:
    def __init__(self,name,quantity,unit):
        self.name = name
        self.unit = unit
        self.quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self,val):
        k = float(val)
        if not k > 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = k

    def __str__(self):
        return f"{self.name}:{self.quantity}{self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}',{self.quantity},'{self.unit}')"

    def __eq__(self, obg):
        if not isinstance(obg, Ingredient):
            return False
        return (self.name == obg.name) and (self.unit == obg.unit)