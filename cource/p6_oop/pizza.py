# Создайте класс Pizza, который принимает список ингредиентов.
#
# Класс поддерживает:
# - атрибут order_number, который возвращает текущий номерзаказа
# (подсказка: используйте статический атрибут в качестве сквозного счётчика)
# - атрибут ingredients, который возвращает список, принятый в конструкторе
# - функции(garden_feast, hawaiian, meat_festival) создания видов пицц, ингредиенты которых
# заранее известны(см.таблицу)
#
# Name            Ingredients
# hawaiian        - ham, pineapple
# meat_festival   - beef, meatball, bacon
# garden_feast    - spinach, olives, mushroom
#
# Примеры вызовов и возвратов:
# ```
# p1 = Pizza(['bacon', 'parmesan', 'ham'])
# p2 = Pizza.garden_feast()
# p1.ingredients -> ['bacon', 'parmesan', 'ham']
# p2.ingredients -> ['spinach', 'olives', 'mushroom']
# p1.order_number -> 1
# p2.order_number -> 2
# ```
from typing import List, Dict


class Pizza:
    pizza_ingredients: Dict[str, List[str]] = {
        'hawaiian': ['ham', 'pineapple'],
        'meat_festival': ['beef', 'meatball', 'bacon'],
        'garden_feast': ['spinach', 'olives', 'mushroom'],
    }
    current_number: int = 1

    def __init__(self, ingredients: List[str]):
        self.ingredients = ingredients
        self.order_number = Pizza.current_number
        Pizza.current_number += 1

    @staticmethod
    def hawaiian():
        return Pizza(Pizza.pizza_ingredients['hawaiian'])

    @staticmethod
    def meat_festival():
        return Pizza(Pizza.pizza_ingredients['meat_festival'])

    @staticmethod
    def garden_feast():
        return Pizza(Pizza.pizza_ingredients['garden_feast'])


def main():
    p1 = Pizza(['bacon', 'parmesan', 'ham'])
    p2 = Pizza.garden_feast()
    print(f'{p1.ingredients}')
    print(f'{p2.ingredients}')
    print(f'{p1.order_number}')
    print(f'{p2.order_number}')


if __name__ == "__main__":
    main()
