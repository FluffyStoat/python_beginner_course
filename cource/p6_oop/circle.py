# Создайте класс Circle который конструируется с передачей радиуса в качестве аргумента.
# Класс Circle должен предоставлять две
# функции:
# - get_area, которая возвращает площадь круга
# - get_perimeter, которая возвращает длину окружности
#
# Примеры использования:
# ```
# circle = Circle(10)
# circle.get_area()  # Возвращает прощадь
# circle.get_perimeter()  # Возрващает периметер
# ```

import math


class Circle:

    def __init__(self, radius: int):
        self.radius = radius

    def get_area(self):
        return math.pi * pow(self.radius, 2)

    def get_perimeter(self):
        return 2 * math.pi * self.radius


def main():
    circle = Circle(10)

    print(f'{circle.get_area()}')
    print(f'{circle.get_perimeter()}')


if __name__ == "__main__":
    main()
