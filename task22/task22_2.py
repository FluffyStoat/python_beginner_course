# 2. Запросить у пользователя координаты x и y двух точек на плоскости.
# Посчитать расстояние между заданными точками и вывести результат на консоль
# с точностью до трёх знаков после запятой (плавающей точки).
# Примечание: у каждой точки есть две координаты: x и y. Расстояние
# рассчитывается по формуле, которую вы с лёгкостью найдёте в Интернете.

from typing import List, Dict
from math import sqrt

msg = "Введите первую координаты {point_name} точки через [x:y]: "


def main():
    points_names: List[str] = ["А", "Б"]
    points: Dict[str, tuple] = {}

    for name in points_names:
        points[name] = input_point(name)

    point_a = points["А"]
    point_b = points["Б"]

    result = sqrt(pow(point_b[0] - point_a[0], 2) + pow(point_b[1] - point_a[1], 2))
    print("Растояние между точками равно {:.3f}".format(result))


def input_point(point_name: str) -> tuple:
    try:
        coordinate = input(msg.format(point_name=point_name)).split(':')
        point = tuple(int(crd.strip()) for crd in coordinate)
        return point
    except ValueError:
        print('Ошибка ввода координата будет равна [0, 0]')
    return 0, 0


if __name__ == "__main__":
    main()

