# Напишите функцию whos_first, которая принимает две строки и возвращает имя игрока,
# который выстрелил первым.
# Если игроки выстрелили одновременно, то вернуть строку "tie".
#
# **Пример:**
# p1: "               Bang   "
# p2: "          Bang        "
#
# Примечание: передаваемые строки - могут быть различной длины! (то есть содержать различное количество пробелов)

def main():
    p1: str = "               Bang   "
    p2: str = "          Bang        "

    print(f"{whos_first(p1, p2)}")


def whos_first(p1: str, p2: str) -> str:
    first_shooter: int = get_shot(p1)
    second_shooter: int = get_shot(p2)

    if first_shooter == second_shooter:
        return "tie"

    if first_shooter < second_shooter:
        return "p1"

    if first_shooter > second_shooter:
        return "p2"

    return "none"


def get_shot(player: str) -> int:
    for num, s in enumerate(player):
        if s != " ":
            return num
    return -1


if __name__ == "__main__":
    main()
