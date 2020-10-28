# 3. На ферме есть куры, коровы и свиньи. У курицы две ноги, у свиньи - четыре,
# у коровы - четыре. Запросить у пользователя (фермера) ввод кол-ва кур, свиней и коров,
# просуммировать кол-во ног всех животных и вывести результат на консоль.
from typing import Dict


def main():
    print("Веселая ферма!")

    farm_info: Dict[str, int] = {
        "chicken": 2,
        "pig": 4,
        "cow": 4
    }

    try:
        chickens_count: int = int(input("Введите кол-во кур:"))
        pigs_count: int = int(input("Введите кол-во свиней:"))
        cows_count: int = int(input("Введите кол-во коров:"))

        legs_count = farm_info["chicken"] * chickens_count + farm_info["pig"] * pigs_count + \
            farm_info["cow"] * cows_count

        print(f"Кол-во ног равно {legs_count}")
    except ValueError:
        print('Ошибка ввода! Нужно вводить число!')


if __name__ == "__main__":
    main()
