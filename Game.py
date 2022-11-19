import ctypes

import pygame
import pymunk as pm

from Camera import Camera


class Game:
    def __init__(self):
        user32 = ctypes.windll.user32
        self.space = pm.Space()
        self.space.gravity = (0.0, 900.0)
        self.ch = self.space.add_collision_handler(0, 0)
        self.width, self.height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.display = pygame.display.set_mode((self.width, self.height))
        self.ch.data["surface"] = self.display
        self.camera = Camera((self.width, self.height), (0, 0))
        self.drawables = []
        self.run = True