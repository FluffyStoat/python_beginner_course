# Написать игру в "камень-ножницы-бумага" против компьютера.
# Запустить игру в бесконечном цикле. Запросить ввод от пользователя (R - камень, S - ножницы, P - бумага).
# Сгенерировать случайный выбор компьютера. Вывести выбор компьютера.
# Определить победителя, выведя соответствующую информацию. Спросить пользователя - хочет ли он повторить игру.
# Если хочет - повторить, не хочет - выйти из цикла.

import random
from typing import List, Dict

from utils.console_colors import Colors

items_list: List[str] = ["R", "S", "P"]
items_values: Dict[str, int] = {"R": 0, "S": 1, "P": 2}

# -1 - Поражение, 0 - Ничья, 1 - Победа
# "RR": "Ничья",      "RS": "Победа",     "RP": "Поражение",
# "SR": "Поражение",  "SS": "Ничья",      "SP": "Победа",
# "PR": "Победа",     "PS": "Поражение",  "PP": "Ничья",

rules_table: [int, int] = [[1, 1, -1],
                           [-1, 0, 1],
                           [1, -1, 0]]

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
                          f"{Colors.light_yellow}Q{Colors.reset_all} - выход): ").upper()

        if item not in items_list:
            if item == "Q":
                break
            else:
                print(f"{Colors.red}Выбран некорректный символ!{Colors.reset_all}\n"
                      f"Пожалуйста повторите выбор или выберите {Colors.light_yellow}'Q'{Colors.reset_all}\n")
        else:
            comp_item: str = random.choice(items_list)

            x: int = items_values[item]
            y: int = items_values[comp_item]

            print(f"Ваш выбор: {Colors.light_yellow}{item}{Colors.reset_all}")
            print(f"Выбор компьютера: {Colors.light_yellow}{comp_item}{Colors.reset_all}")

            result: int = rules_table[x][y]

            if result == -1:
                print(f"{Colors.red}Вы проиграли!{Colors.reset_all}\n")
            elif result == 0:
                print(f"{Colors.yellow}Ничья!{Colors.reset_all}\n")
            elif result == 1:
                print(f"{Colors.green}Вы победили!{Colors.reset_all}\n")


if __name__ == "__main__":
    main()
