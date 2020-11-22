# Создайте класс Calculator который поддерживает:
# - сложение двух чисел
# - вычисление разницы между двумя числами
# - умножение двух чисел
# - деление одного числа на другое
#
# Примеры вызовов и возвратов:
# ```
# calculator = Calculator()
# calculator.add(10, 5) -> 15
# calculator.subtract(10, 5) -> 5
# calculator.multiply(10, 5) -> 50
# calculator.divide(10, 5) -> 2
# ```

class Calculator:

    @staticmethod
    def add(op1: int, op2: int) -> int:
        return op1 + op2

    @staticmethod
    def subtract(op1: int, op2: int) -> int:
        return op1 - op2

    @staticmethod
    def multiply(op1: int, op2: int) -> float:
        return op1 * op2

    @staticmethod
    def divide(op1: int, op2: int) -> float:
        return op1 / op2


def main():
    print(f"{Calculator.add(10, 5)}")
    print(f"{Calculator.subtract(10, 5)}")
    print(f"{Calculator.multiply(10, 5)}")
    print(f"{Calculator.divide(10, 5)}")


if __name__ == "__main__":
    main()
