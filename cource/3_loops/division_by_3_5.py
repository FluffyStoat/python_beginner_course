# Построить цикл от 0 до введённого числа (включительно) и посчитать сумму всех чисел, делимых без остатка на 3 или 5.
# Вывести на консоль это число.

def main():
    try:
        count: int = int(input("Введите кол-во: "))
        amount: int = 0
        for num in range(count + 1):
            if num % 3 == 0 or num % 5 == 0:
                amount = amount + num
    except ValueError:
        print('Ошибка ввода! Нужно вводить число!')

    print(f"Результат: {amount}")


if __name__ == "__main__":
    main()
