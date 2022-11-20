import math
from typing import Tuple

import pygame
from pymunk import Vec2d

class ImageLoader:
    def __init__(self):
        self.images = {}
        paths = ["testgrass.png", "szary.png", "weed.png", "giraffe.png",
                 "giraffe_head.png",
                 "full_giraffe.png",
                 "full_loong_giraffe.png",
                 "full_loong_giraffe_head.png",
                 "full_loong_giraffe_body.png"]
        for path in paths:
            self.images[path] = pygame.image.load(path)
            self.images[path].convert_alpha()

    def draw_on_pos(self, pos: Tuple[float, float], size: Tuple[float, float], image_name, display, angle=0):
        rotated_img = pygame.transform.rotate(pygame.transform.scale(self.images[image_name], size),
                                              math.degrees(-angle))
        offset = Vec2d(*rotated_img.get_size()) / 2
        pos = pos - offset
        display.blit(rotated_img, pygame.Rect(*pos, *size))
