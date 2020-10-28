# Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку,
# сворачивая соседние по числовому ряду числа в диапазоны.
#
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"
from typing import List


def check(values: List[int]):
    print(values)

    values.sort()

    ranges: List[str] = []
    start: int = values[0]

    for num, val in enumerate(values, start=1):
        print(f"start={start} len={len(values)} num={num} val={val}")

        if len(values) == num:
            if num == len(values):
                if start != val:
                    ranges.append(f"{start}-{val}")
                else:
                    ranges.append(f"{val}")
            break
        if val + 1 != values[num]:
            if start != val:
                ranges.append(f"{start}-{val}")
            else:
                ranges.append(f"{val}")
            start = values[num]

    print(f"Result: {ranges}")


def main():
    check([1, 4, 5, 2, 3, 9, 8, 11, 0])
    check([1, 4, 3, 2])
    check([1, 4])


if __name__ == "__main__":
    main()

