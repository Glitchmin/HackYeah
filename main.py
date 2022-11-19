import pygame,pymunk
from shapes_collection import *
from ground import Ground
from Camera import Camera


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
space = pymunk.Space()
GRAVITY = 200
space.gravity = (0, GRAVITY)
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

# class Point:
#     def __init__(self):

VEL = 5
def pink_handle_movement(keys_pressed, red, ball):
    if keys_pressed[pygame.K_LEFT]:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL


def add_ball(pos, balls):
    new_ball = Ball(pos[0], pos[1])
    new_ball.add_to_space(space)
    new_ball.draw(WIN, BLACK)
    balls.append(new_ball)


def main():
    clock = pygame.time.Clock()
    run = True

    # WIN.blit(SPACE, (0, 0))

    WIN.fill(WHITE)
    #RECT = pygame.Rect(300, 0, 100, 50)
    #pygame.draw.rect(WIN, RED, RECT)

    placing = False
    balls = [Ball(100, 100)]
    ground = Ground(WIN, space)
    add_ball((), balls)

    camera = Camera((WIDTH, HEIGHT))
    camera.follow(balls[0])

    while run:
        pygame.display.update()

        clock.tick(FPS)
        space.step(1/FPS)
        WIN.fill(WHITE)

        for b in balls:
            b.draw(WIN, BLACK)
        ground.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                add_ball(pos, balls)

    pygame.quit()


if __name__ == "__main__":
    main()
