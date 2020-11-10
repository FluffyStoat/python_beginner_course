# Мини-судоку. Напишите функцию any_duplicates, которая принимает двумерный массив размера 3х3 (9 элементов).
# Двумерный массив заполнен числами от 1 до 9. Функция должна вернуть False, если в массиве все числа от 1 до 9
# встречаются ровно один раз. В противном случае True.
#
# Примеры вызовов.
#
# ```
# any_duplicates([[1, 3, 2], [9, 7, 8], [4, 5, 6]]) -> False
# any_duplicates([[8, 9, 2], [5, 6, 1], [3, 7, 4]]) -> False
# any_duplicates([[1, 1, 3], [6, 5, 4], [8, 7, 9]]) -> True # 1 - дублируется
# any_duplicates([[1, 2, 3], [3, 4, 5], [9, 8, 7]]) -> True # 3 - дублируется
# ```
from typing import List


def any_duplicates(square: List[List[int]]) -> bool:
    expected: int = sum(range(1, 10))
    actual: int = 0

    for row in square:
        for col in row:
            actual += col

    return expected != actual


def main():
    print(f"[[1, 2, 3], [3, 4, 5], [9, 8, 7]] -> {any_duplicates([[1, 3, 2], [9, 7, 8], [4, 5, 6]])}")
    print(f"[[8, 9, 2], [5, 6, 1], [3, 7, 4]] -> {any_duplicates([[8, 9, 2], [5, 6, 1], [3, 7, 4]])}")
    print(f"[[1, 1, 3], [6, 5, 4], [8, 7, 9]] -> {any_duplicates([[1, 1, 3], [6, 5, 4], [8, 7, 9]])}")
    print(f"[[1, 2, 3], [3, 4, 5], [9, 8, 7]] -> {any_duplicates([[1, 2, 3], [3, 4, 5], [9, 8, 7]])}")


if __name__ == "__main__":
    main()
