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

import pygame

BLACK = [0, 0, 0]


def main():
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([600, 600])
    pygame.display.set_caption("Крестики-нолики")

    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Hello Привет', True, (180, 0, 0))

    # Run until the user asks to quit
    running = True

    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))

        screen.blit(text1, (10, 50))
        draw_field(screen)

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


def draw_field(screen: pygame.Surface):
    pygame.draw.line(screen, BLACK, [200, 0], [200, 600], 4)
    pygame.draw.line(screen, BLACK, [400, 0], [400, 600], 4)
    pygame.draw.line(screen, BLACK, [0, 200], [600, 200], 4)
    pygame.draw.line(screen, BLACK, [0, 400], [600, 400], 4)


if __name__ == "__main__":
    main()

