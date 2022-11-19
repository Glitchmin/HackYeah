import random
import pygame
import GameStates
import pymunk as pm

from Camera import Camera
from Catapult import Catapult
from Circle import Circle

from ground import Ground
from Game import Game
from Player import Player

pygame.display.set_caption("Camelopard Castle: Siege")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60

game = Game()


def rect_clicked(click, rect):
    x, y = click

    return rect.x <= x <= rect.x + rect.width and rect.y <= y <= rect.y + rect.height


def calculate_physics():
    to_remove = []
    for drawable in game.drawables:
        # if drawable.get_pos()[1] > 400:
        #     to_remove.append(drawable)
        p = tuple(map(int, drawable.get_pos()))
        drawable.draw()
    for ball in to_remove:
        game.space.remove(ball.shape, ball.body)
        game.drawables.remove(ball)

    dt = 1.0 / 60.0
    for x in range(1):
        game.space.step(dt)


def update_screen(clock):
    pygame.display.update()
    game.display.fill(pygame.Color("white"))
    clock.tick(FPS)
    pygame.display.flip()


def handle_input(catapult: Catapult):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.run = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            circle = Circle(game.display, game.camera, pos)
            game.space.add(circle.shape, circle.body)
            game.drawables.append(circle)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            projectile = catapult.space_clicked()
            if projectile is not None:
                game.space.add(projectile.body, projectile.shape)


def main():
    clock = pygame.time.Clock()

    player = Player(True,game)
    player.playerTurn()
    game.drawables.append(player.catapult)
    game.drawables.append(Ground(game.display,game.space,game.camera))

    current_state = GameStates.PL_1_BUILDING

    while game.run:
        handle_input(player.catapult)
        calculate_physics()
        update_screen(clock)

    pygame.quit()


if __name__ == "__main__":
    main()
