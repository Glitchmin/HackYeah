from typing import Tuple

import pygame
from pymunk import Shape

from Camera import Camera
from Physical import Physical
import pymunk as pm


class Rectangle(Physical):
    def get_size(self) -> Tuple[float, float]:
        return self.size

    def __init__(self, window, camera: Camera, pos: Tuple[float, float], size: Tuple[float, float],  mass=10):
        self.mass = mass
        self.size = size
        inertia = pm.moment_for_box(mass, size)
        body = pm.Body(mass, inertia)
        body.position = pos
        shape = pm.Poly.create_box(body, size)

        super().__init__(shape, body, window, camera)

    def draw(self):
        pygame.draw.rect(self.window, pygame.Color("blue"), rect=pygame.Rect(*self.get_pos(), *self.get_size()))
