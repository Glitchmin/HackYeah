import pygame,pymunk
from shapes_collection import *
import typing
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
space = pymunk.Space()
GRAVITY = 200
#space.gravity = (0, GRAVITY)
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

class wall():
    pass

def main():
    clock = pygame.time.Clock()
    run = True

    # WIN.blit(SPACE, (0, 0))

    WIN.fill(WHITE)
    #RECT = pygame.Rect(300, 0, 100, 50)
    #pygame.draw.rect(WIN, RED, RECT)

    placing = False
    balls = []
    dummy_ball = None
    adding = False
    while run:
        pygame.display.update()

        clock.tick(FPS)
        space.step(1/FPS)
        WIN.fill(WHITE)
        for b in balls:
            b.draw(WIN, BLACK)
        if(adding):
            pos = pygame.mouse.get_pos()
            x, y = pos
            dummy_ball = Ball(x, y)
            dummy_ball.add_to_space(space)
            dummy_ball.shape.collision_type = 3
            dummy_ball.shape.density = 0
            dummy_ball.draw(WIN, RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP  and event.button == 1:
                pos = pygame.mouse.get_pos()
                x, y = pos
                new_ball = Ball(x, y)
                new_ball.add_to_space(space)
                new_ball.draw(WIN, BLACK)
                balls.append(new_ball)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                adding = True

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                adding = False




    pygame.quit()


if __name__ == "__main__":
    main()
