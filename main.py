import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Second Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60

def add_block(cords):
    x, y = cords
    rect = pygame.Rect(x, y, 20, 20)
    pygame.draw.rect(WIN, BLACK, rect)


def rect_clicked(click, rect):
    x, y = click

    return rect.x <= x <= rect.x + rect.width and rect.y <= y <= rect.y + rect.height


def main():
    clock = pygame.time.Clock()
    run = True


    # WIN.blit(SPACE, (0, 0))

    WIN.fill(WHITE)
    RECT = pygame.Rect(300, 0, 100, 50)
    pygame.draw.rect(WIN, RED, RECT)

    placing = False

    while run:
        pygame.display.update()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                add_block(pos)


    pygame.quit()


if __name__ == "__main__":
    main()
