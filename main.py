import random
import pygame
import GameStates
import pymunk as pm

from Camera import Camera
from Catapult import Catapult
from Circle import Circle
from Game import Game
from Player import Player
from ground import Ground

pygame.display.set_caption("Camelopard Castle: Siege")

game = Game()

def main():
    clock = pygame.time.Clock()

    player = Player(True,game)
    player.playerTurn()
    game.drawables.append(player.catapult)
    game.drawables.append(Ground(game.display,game.space,game.camera))

    current_state = GameStates.PL_1_BUILDING

    while game.run:
        game.handle_input(player.catapult)
        game.calculate_physics()
        game.update_screen(clock)

    pygame.quit()


if __name__ == "__main__":
    main()
