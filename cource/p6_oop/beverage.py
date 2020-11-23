# Создать класс Beverage, который при конструировании принимает список ингредиентов
#
# - поддерживает атрибут ingredients, возвращающий список ингредиентов, переданных при конструировании инстанции класса
# - поддерживает функцию get_cost, вычисляющую итоговую стоимость всех ингредиентов напитка (получается себестоимость
# напитка)
# - поддерживает функцию get_price, вычисляющую цену напитка посредством умножения себестоимости на 2.5
# - поддерживает функцию get_name, которая возвращает строку, перечисляющую ингредиенты, сортируя их в алфавитном
# порядке. Если ингредиентов больше одного, то в конце добавляет слово 'Fusion', иначе добавляет слово 'Smoothie'.
# Эта функция также должна заменять 'berries' на 'berry'.
#
# Ингредиенты и их себестоимость:
#
# ```
# Strawberries $1.50
# Banana       $0.50
# Mango        $2.50
# Blueberries  $1.00
# Raspberries  $1.00
# Apple        $1.75
# Pineapple    $3.50
# ```
#
# Примеры вызовов и возвратов:
# ```
# s1 = Beverage(["Banana"])
# s1.ingredients -> ["Banana"]
# s1.get_cost() -> "$0.50"
# s1.get_price() -> "$1.25"
# s1.get_name() -> "Banana Smoothie"
#
# s2 = Beverage(["Blueberries", "Strawberries", "Blueberries"])
# s2.ingredients -> [["Blueberries", "Strawberries", "Blueberries"]]
# s2.get_cost() -> "$3.50"
# s2.get_price() -> "$8.75"
# s2.get_name() -> "Blueberry Raspberry Strawberry Fusion"
from typing import Dict, List


class Beverage:
    prices: Dict[str, int] = {
        "Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5,
        "Blueberries": 1, "Raspberries": 1, "Apple": 1.75,
        "Pineapple": 3.5
    }

    def __init__(self, ingredients: List[str]):
        self.ingredients = ingredients

    def get_cost(self):
        cost: float = 0

        for item in self.ingredients:
            cost += Beverage.prices.get(item)

        return "${:.2f}".format(cost)

    def get_price(self):
        price: float = 0.0

        for item in self.ingredients:
            price += 2.5 * Beverage.prices.get(item)

        return "${:.2f}".format(price)

    # noinspection PyMethodMayBeStatic
    def get_name(self):
        names: str = ' '.join(sorted(self.ingredients))
        names += " Smoothie" if len(self.ingredients) == 1 else " Fusion"
        return names.replace("berries", "berry")


def main():
    s1 = Beverage(["Banana"])
    print(f"{s1.ingredients}")
    print(f"{s1.get_cost()}")
    print(f"{s1.get_price()}")
    print(f"{s1.get_name()}")

    s2 = Beverage(["Raspberries", "Strawberries", "Blueberries"])
    print(f"{s2.ingredients}")
    print(f"{s2.get_cost()}")
    print(f"{s2.get_price()}")
    print(f"{s2.get_name()}")


if __name__ == "__main__":
    main()
