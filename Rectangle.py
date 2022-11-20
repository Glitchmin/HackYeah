from typing import Tuple

import pygame
from pymunk import Shape

from Camera import Camera
from Physical import Physical
import pymunk as pm


class Rectangle(Physical):
    def get_size(self) -> Tuple[float, float]:
        return self.size

    def __init__(self, window, camera: Camera, pos: Tuple[float, float], size: Tuple[float, float], mass=10,
                 friction=1, static: bool = False):
        self.mass = mass
        self.size = size
        body = None
        if static:
            body = pm.Body(body_type=pm.Body.STATIC)
        else:
            inertia = pm.moment_for_box(mass, size)
            body = pm.Body(mass, inertia)
        body.position = pos
        shape = pm.Poly.create_box(body, size)
        shape.friction = friction
        self.color = pygame.Color("blue")

        super().__init__(shape, window, camera)

    def draw(self):
        screen_position = self.camera.to_scr_pos(self.get_pos())
        self.draw_on_pos(screen_position)

    def draw_on_pos(self, pos: Tuple[float, float]):
        pygame.draw.rect(self.window, self.color, rect=pygame.Rect(*pos, *self.get_size()))

    def copy(self):
        ret = Rectangle(self.window, self.camera, self.get_pos(), self.size)
        return ret
