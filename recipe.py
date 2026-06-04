#1.1
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
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, obg):
        if not isinstance(obg, Ingredient):
            return False
        return (self.name == obg.name) and (self.unit == obg.unit)
    

#1.2
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
        mn = [str(it) for it in self.ings]
        return self.title + ": " + ", ".join(mn)
    
#1.3
class ShoppingList:
    def __init__(self):
        self.items = []

    def add_recipe(self,recipe,portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        ar = recipe.scale(portions)
        for it in ar.ings:
            self.items.append((it,recipe.title))

    def remove_recipe(self, title):
        new = []
        for ing,t in self.items:
            if t != title:
                new.append((ing,t))
        self.items = new

    def get_list(self):
        d = {}
        for ing,t in self.items:
            key = (ing.name,ing.unit)
            if key in d:
                d[key] += ing.quantity
            else:
                d[key] = ing.quantity
        res = []
        for (name,unit), q in d.items():
            res.append(Ingredient(name,q, unit))
        return sorted(res, key=lambda x: x.name)


    def __add__(self,obg):
        res = ShoppingList()
        res.items = self.items + obg.items
        return res

#1.4
class DietaryRecipe(Recipe):
    def __init__(self,title,diet_type,ingredients = None):
        if ingredients is None:
            ingredients = []
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self,ratio):
        if not self.is_valid_ratio(ratio):
            raise ValueError()
        arr = super().scale(ratio)
        return DietaryRecipe(self.title, self.diet_type, arr.ings)

    def __str__(self):
        return "[" + self.diet_type + "] " + super().__str__()