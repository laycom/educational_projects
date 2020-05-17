# Задача № 1

import collections
import math
import typing
from decimal import Decimal


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


class FoodInfo(object):
    def __init__(self, proteins: Decimal = Decimal(0), fats: Decimal = Decimal(0), carbohydrates: Decimal = Decimal(0), food_value: Decimal = Decimal(0)):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates
        self.food_value = food_value

    def __mul__(self, other: Decimal):
        assert isinstance(other, Decimal)

        return FoodInfo(self.proteins * other, self.fats * other, self.carbohydrates * other, self.food_value * other)

    def __add__(self, other):
        assert isinstance(other, FoodInfo)

        return FoodInfo(
            self.proteins + other.proteins,
            self.fats + other.fats,
            self.carbohydrates + other.carbohydrates,
            self.food_value + other.food_value
        )


class AmountFoodInfo(object):
    def __init__(self, amount, food_info):
        self.amount = amount
        self.food_info = food_info


class Ingredient(object):
    def __init__(self, name: str, amount: Amount):
        self.name = name
        self.amount = amount


class CatalogIngredientInfo(object):
    def __init__(self, name: str, price: int, amount: Amount):
        self.name = name
        self.price = price
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


def read_catalog():
    ingredient_count = int(input())

    catalog = {}
    for _ in range(ingredient_count):
        name, price, amount, unit = input().split(' ')
        catalog[name] = CatalogIngredientInfo(
            name=name,
            price=int(price),
            amount=Amount(Decimal(amount), unit)
        )

    return catalog


def read_food_info():
    info_count = int(input())

    food_info = {}
    for _ in range(info_count):
        name, amount, unit, proteins, fats, carbohydrates, food_value = input().split(' ')
        food_info[name] = AmountFoodInfo(
            amount=Amount(
                count=Decimal(amount),
                unit=unit
            ),
            food_info=FoodInfo(
                proteins=Decimal(proteins),
                fats=Decimal(fats),
                carbohydrates=Decimal(carbohydrates),
                food_value=Decimal(food_value)
            )
        )

    return food_info


def main():
    dishes = read_dishes()
    catalog = read_catalog()
    food_info = read_food_info()

    need_ingredients = collections.defaultdict(Decimal)
    need_ingredients_count = collections.defaultdict(int)
    dish_info = collections.defaultdict(FoodInfo)
    for dish in dishes:
        for ingredient in dish.ingredients:
            converted_amount = ingredient.amount.convert_to(catalog[ingredient.name].amount.unit)
            converted_food_info_amount = food_info[ingredient.name].amount.convert_to(catalog[ingredient.name].amount.unit)
            need_ingredients[ingredient.name] += converted_amount.count * dish.count
            dish_info[dish.name] += food_info[ingredient.name].food_info * (converted_amount.count / converted_food_info_amount.count)

    total_price = Decimal(0)
    for ingredient_name, need_ingredient in need_ingredients.items():
        need_count = need_ingredient // catalog[ingredient_name].amount.count
        if need_count * catalog[ingredient_name].amount.count < need_ingredient:
            need_count += 1

        need_ingredients_count[ingredient_name] = need_count
        total_price += catalog[ingredient_name].price * need_count

    print(total_price)
    for name in catalog.keys():
        print(name, need_ingredients_count[name])

    for name, info in dish_info.items():
        print(name, info.proteins, info.fats, info.carbohydrates, info.food_value)


if __name__ == '__main__':
    main()
