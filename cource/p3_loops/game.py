# Написать игру в "камень-ножницы-бумага" против компьютера.
# Запустить игру в бесконечном цикле. Запросить ввод от пользователя (R - камень, S - ножницы, P - бумага).
# Сгенерировать случайный выбор компьютера. Вывести выбор компьютера.
# Определить победителя, выведя соответствующую информацию. Спросить пользователя - хочет ли он повторить игру.
# Если хочет - повторить, не хочет - выйти из цикла.
from typing import List
from utils.console_colors import Colors

import random


items_list: List[str] = ["R", "S", "P"]

header: str = f"""
{Colors.light_yellow}********************************{Colors.reset_all}
{Colors.light_yellow}* Игра "камень-ножницы-бумага" *{Colors.reset_all}
{Colors.light_yellow}********************************{Colors.reset_all}
"""


def main():
    print(header)

    while True:
        item: str = input(f"Введите ({Colors.light_yellow}R{Colors.reset_all} - камень, "
                          f"{Colors.light_yellow}S{Colors.reset_all} - ножницы, "
                          f"{Colors.light_yellow}P{Colors.reset_all} - бумага, "
                          f"{Colors.light_yellow}Q{Colors.reset_all} - выход): ")

        if item not in items_list:
            if item == "Q":
                break
            else:
                print(f"{Colors.red}Выбран некорректный символ!{Colors.reset_all}\n"
                      f"Пожалуйста повторите выбор или выберите {Colors.light_yellow}'Q'{Colors.reset_all}\n")
        else:
            print(f"Ваш выбор: {Colors.light_yellow}{item}{Colors.reset_all}")
            print(f"Выбор компьютера: {Colors.light_yellow}{random.choice(items_list)}{Colors.reset_all}\n")


if __name__ == "__main__":
    main()
