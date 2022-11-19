import random
import pygame
import pymunk as pm

from Camera import Camera
from Catapult import Catapult
from Circle import Circle
from ground import Ground

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Second Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60


# def add_block(cords, space, squares):
#     mass = 10
#     radius = 25
#     inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
#     body = pm.Body(mass, inertia)
#     x = cords[0]
#     body.position = x, cords[1]
#     shape = pm.Circle(body, radius, (0, 0))
#     space.add(body, shape)
#     squares.append(shape)


def rect_clicked(click, rect):
    x, y = click

    return rect.x <= x <= rect.x + rect.width and rect.y <= y <= rect.y + rect.height


def main():
    clock = pygame.time.Clock()
    run = True

    space = pm.Space()
    space.gravity = (0.0, 900.0)
    ch = space.add_collision_handler(0, 0)
    ch.data["surface"] = WIN

    camera = Camera((WIDTH, HEIGHT), (0, 0))

    drawables = []

    # WIN.blit(SPACE, (0, 0))

    WIN.fill(WHITE)
    RECT = pygame.Rect(300, 0, 100, 50)
    pygame.draw.rect(WIN, RED, RECT)

    catapult = Catapult(space,drawables,WIN,camera)
    drawables.append(catapult)

    placing = False

    ground = Ground(WIN, space, camera)
    drawables.append(ground)

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
                circle = Circle(WIN, camera, pos)
                space.add(circle.shape, circle.body)
                drawables.append(circle)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                projectile = catapult.space_clicked()
                if projectile is not None:
                    space.add(projectile.body, projectile.shape)
                    camera.follow(projectile)

        WIN.fill(pygame.Color("white"))

        to_remove = []
        for drawable in drawables:
            # if drawable.get_pos()[1] > 400:
            #     to_remove.append(drawable)
            p = tuple(map(int, drawable.get_pos()))
            drawable.draw()

        for ball in to_remove:
            space.remove(ball.shape, ball.body)
            drawables.remove(ball)

        ### Update physics
        dt = 1.0 / 60.0
        for x in range(1):
            space.step(dt)

        ### Flip screen
        pygame.display.flip()
        clock.tick(50)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))

    pygame.quit()


if __name__ == "__main__":
    main()
