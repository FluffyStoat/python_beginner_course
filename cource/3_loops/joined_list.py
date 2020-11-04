# На вход подаются два списка чисел длины N.
# Задача: взять из первого списка все нечётные числа, из второго чётные и объединить их в новом списке
# с названием joined_list.
from typing import List


def main():
    first_lst: List[int] = [5, 4, 7, 4, 3, 4]
    second_lst: List[int] = [3, 6, 5, 2, 8, 7]
    joined_list: List[int] = []

    if len(first_lst) != len(second_lst):
        print("Длина списков должна быть одинаковая")
        raise

    for num in range(len(first_lst)):
        if first_lst[num] % 2 != 0:
            joined_list.append(first_lst[num])
        if second_lst[num] % 2 == 0:
            joined_list.append(second_lst[num])

    return joined_list


if __name__ == "__main__":
    main()
