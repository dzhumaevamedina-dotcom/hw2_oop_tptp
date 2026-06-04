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
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}',{self.quantity},'{self.unit}')"

    def __eq__(self, obg):
        if not isinstance(obg, Ingredient):
            return False
        return (self.name == obg.name) and (self.unit == obg.unit)
    


class Recipe:
    def __init__(self,title,ingredients):
        self.title = title
        self.ings = ingredients

    def add_ingredient(self,ing):
        for it in self.ings:
            if it.name == ing.name and it.unit == ing.unit:
                it.quantity += ing.quantity
                return
        self.ings.append(ing)

    @staticmethod
    def is_valid_ratio(ratio):
        try:
            return float(ratio) > 0
        except (TypeError,ValueError):
            return False

    def scale(self,ratio):
        if not self.is_valid_ratio(ratio):
            raise ValueError()
        arr = []
        for it in self.ings:
            arr.append(Ingredient(it.name,it.quantity * ratio,it.unit))
        return Recipe(self.title,arr)

    def __len__(self):
        return len(self.ings)

    def __str__(self):
        s = self.title + ": "
        for it in self.ings:
            s += str(it) + ", "
        return s[:-2]