# Семи-карточный техасский покер. На столе лежат пять карт и в руке две карты.
# Необходимо определить есть ли комбинация, называемая флеш (Flush).
# Комбинация флеш определяется наличием пяти карт одной масти (среди всех карт: и тех, что лежат на столе
# и тех что в руке)
#
# Стол = ["A_S", "J_H", "7_D", "8_D", "10_D"], Рука = ["J_D", "3_D"]
#
# "Номинал_Масть" (Возможные значения: S (пики), H (черви), D (буби), C (трефы))
from typing import List, Dict


def main():
    hand_cards: List[str] = ["A_S", "J_H", "7_D", "8_D", "10_D"]
    table_cards: List[str] = ["J_D", "3_D"]

    suits: Dict[str, int] = {"S": 0, "H": 0, "D": 0, "C":0}

    for card in hand_cards + table_cards:
        parsed_card: (str, str) = card.split("_")
        if parsed_card[0] is not None and parsed_card[1] is not None:
            suits[parsed_card[1]] = suits[parsed_card[1]] + 1

    for count in suits.values():
        if count >= 5:
            print("Flush!")
            return

    print("No Flush!")


if __name__ == "__main__":
    main()

