from typing import Tuple

import pygame

class ImageLoader:
    def __init__(self):
        self.images = {}
        self.images["testgrass.png"] = pygame.image.load("testgrass.png")
        self.images["testgrass.png"].convert()
        self.images["szary.png"] = pygame.image.load("szary.png")
        self.images["szary.png"].convert()

    def draw_on_pos(self, pos: Tuple[float, float], size: Tuple[float, float], image_name, display):
        display.blit(pygame.transform.scale(self.images[image_name], size), pygame.Rect(*pos, *size))