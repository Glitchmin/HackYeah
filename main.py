import random
import pygame
from Game import Game
from Player import Player
from ground import Ground

pygame.display.set_caption("Camelopard Castle: Siege")

game = Game()


def main():
    clock = pygame.time.Clock()

    # ground
    # game.drawables.append(Ground(game.display, game.space, game.camera))

    while game.run:
        game.handle_input()
        game.calculate_physics()
        game.update_screen(clock)

    pygame.quit()


if __name__ == "__main__":
    main()
