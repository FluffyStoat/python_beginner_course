# Крестики-нолики
#
# Вы попробуете реализовать игру в крестики-нолики размером 3х3 - самые что ни наесть обыкновенные.
#
# Сделайте метод, который выводит на каждом ходу текущее положение с линейками, крестиками и ноликами
# (используйте буквы X и O в качестве крестиков и ноликов) - так игрокам будет удобнее ориентироваться.
# Подсказка: если надо вывести строку без перевода каретки на новую строку, используйте функцию print
# и передавайте параметр end=''.
#
# Также вам понадобится реализовать способ проверки наличия выигрышной комбинации. Подсказка: договоримся,
# что клетки поля будут пронумерованы от 0 до 8 и пользователи будут вводить индекс поля, чтобы поставить
# там крестик или нолик.
#
# Для упрощения - тот кто ходит первым - ставит крестик.
from typing import Union

import pygame

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
SEA_GREEN = [46, 139, 87]
STEEL_BLUE = [70, 130, 180]
GREEN = [0, 128, 0]
YELLOW_GREEN = [154, 205, 50]


def main():
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([800, 800])
    pygame.display.set_caption("Крестики-нолики")

    font_36 = pygame.font.Font(None, 36)

    text_player1: Union = font_36.render('Игрок 1 (X)', True, (0, 80, 0))
    text_player2: Union = font_36.render('Игрок 2 (O)', True, (80, 80, 0))

    text_start: Union = font_36.render("Старт", True, WHITE)

    # Run until the user asks to quit
    running = True

    while running:
        mouse = pygame.mouse.get_pos()

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Todo: add calculation of field part
                print(f"mouse click: {mouse[0]}:{mouse[1]}")

        # Fill the background with white
        screen.fill((255, 255, 255))

        draw_menu(screen, text_player1, text_player2)
        draw_field(screen)

        # Todo: Should extract to function
        if 330 < mouse[0] < 470 and 730 < mouse[1] < 770:
            pygame.draw.rect(screen, GREEN, [330, 730, 140, 40])
        else:
            pygame.draw.rect(screen, YELLOW_GREEN, [330, 730, 140, 40])

        screen.blit(text_start, (365, 736))

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


# Todo: refactoring draw menu with initialization
def draw_menu(screen: pygame.Surface, text_player1: Union, text_player2: Union):
    screen.blit(text_player1, (50, 50))
    screen.blit(text_player2, (600, 50))


# Todo: refactor creation with array
def draw_field(screen: pygame.Surface):
    pygame.draw.line(screen, BLACK, [300, 100], [300, 700], 4)
    pygame.draw.line(screen, BLACK, [500, 100], [500, 700], 4)
    pygame.draw.line(screen, BLACK, [100, 300], [700, 300], 4)
    pygame.draw.line(screen, BLACK, [100, 500], [700, 500], 4)


if __name__ == "__main__":
    main()

