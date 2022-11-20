from typing import Tuple

import pygame

class ImageLoader:
    def __init__(self):
        self.images = {}
        self.images["testgrass.png"] = pygame.image.load("testgrass.png")
        self.images["testgrass.png"].convert()
        self.images["szary.png"] = pygame.image.load("szary.png")
        self.images["szary.png"].convert()
        self.images["giraffe.png"] = pygame.image.load("giraffe.png")
        self.images["giraffe.png"].convert()
        self.images["giraffe_head.png"] = pygame.image.load("giraffe_head.png")
        self.images["giraffe_head.png"].convert()
        self.images["full_giraffe.png"] = pygame.image.load("full_giraffe.png")
        self.images["full_giraffe.png"].convert()
        self.images["full_loong_giraffe.png"] = pygame.image.load("full_loong_giraffe.png")
        self.images["full_loong_giraffe.png"].convert()
        self.images["full_loong_giraffe_head.png"] = pygame.image.load("full_loong_giraffe_head.png")
        self.images["full_loong_giraffe_head.png"].convert()
        self.images["full_loong_giraffe_body.png"] = pygame.image.load("full_loong_giraffe_body.png")
        self.images["full_loong_giraffe_body.png"].convert()

    def draw_on_pos(self, pos: Tuple[float, float], size: Tuple[float, float], image_name, display):
        display.blit(pygame.transform.scale(self.images[image_name], size), pygame.Rect(*pos, *size))