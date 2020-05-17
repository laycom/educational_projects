class Amount(object):
    def __init__(self, count: Decimal, unit: str):
        self.count = count
        self.unit = unit

    def convert_to(self, unit: str):
        multipliers_dict = {
            'g': 1,
            'kg': 1000,
            'ml': 1,
            'l': 1000,
            'cnt': 1,
            'tens': 10
        }
        assert self.is_compatible(self.unit, unit)

        return Amount(self.count * multipliers_dict[self.unit] / multipliers_dict[unit], unit)

    @staticmethod
    def is_compatible(unit1, unit2):
        unit_classes = [
            ('g', 'kg'),
            ('ml', 'l'),
            ('cnt', 'tens')
        ]

        for unit_class in unit_classes:
            if unit1 in unit_class:
                return unit2 in unit_class
        return False
        
class Ingredient(object):
    def __init__(self, name: str, amount: Amount):
        self.name = name
        self.amount = amount
        
class Dish(object):
    def __init__(self, name: str, count: int, ingredients: typing.List[Ingredient]):
        self.name = name
        self.count = count
        self.ingredients = ingredients

def read_dishes():
    dish_count = int(input())

    dishes = []
    for _ in range(dish_count):
        dish_name, dish_count, ingredient_count = input().split(' ')
        ingredient_count = int(ingredient_count)

        ingredients = []
        for _ in range(ingredient_count):
            ingredient_name, amount, unit = input().split(' ')
            ingredients.append(Ingredient(name=ingredient_name, amount=Amount(Decimal(amount), unit)))

        dishes.append(Dish(name=dish_name, ingredients=ingredients, count=int(dish_count)))

    return dishes