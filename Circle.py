from typing import Tuple

import pygame

from Camera import Camera
from Physical import Physical
import pymunk as pm


class Circle(Physical):

    def get_size(self) -> Tuple[float, float]:
        return self.radius * 2, self.radius * 2

    def __init__(self, window, camera: Camera, pos: Tuple[float, float], mass=10, radius=25, friction=0.5):
        self.mass = mass
        self.radius = radius
        inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
        body = pm.Body(mass, inertia)
        body.position = pos
        shape = pm.Circle(body, radius, (0, 0))
        shape.friction = friction

        super().__init__(shape, window, camera)

    def is_not_moving(self):
        return abs(self.body.velocity[0]) + abs(self.body.velocity[1]) <= 2.0 or self.body.position[
            1] > 1500

    def draw(self):
        self.draw_on_pos(self.camera.to_scr_pos(self.get_pos()))

    def draw_on_pos(self, pos: Tuple[float, float]):
        pygame.draw.circle(self.window, pygame.Color("red"), self.normalize_pos(pos), int(self.radius), 2)

    def copy(self):
        ret = Circle(self.window, self.camera, self.camera.to_scr_pos(self.get_pos()))
        return ret

    def get_pos(self) -> Tuple[float, float]:
        return self.shape.body.position
        # return (self.shape.body.position[0] + self.get_size()[0]/2,
        #             self.shape.body.position[1] + self.get_size()[1]/2)

    def normalize_pos(self, pos: Tuple[float, float]):
        return pos
        # return (pos[0] - self.get_size()[0] / 2,
        #         pos[1] - self.get_size()[1] / 2)
