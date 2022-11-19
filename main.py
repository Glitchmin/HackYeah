import random
import pygame
import GameStates
import pymunk as pm

from Camera import Camera
from Catapult import Catapult
from Circle import Circle
from Game import Game

pygame.display.set_caption("Camelopard Castle: Siege")

game = Game()

def main():
    clock = pygame.time.Clock()

    catapult = Catapult(game.space, game.drawables, game.display, game.camera)
    game.drawables.append(catapult)
    current_state = GameStates.PL_1_BUILDING

    while game.run:
        game.handle_input(catapult)
        game.calculate_physics()
        game.update_screen(clock)

    pygame.quit()


if __name__ == "__main__":
    main()
