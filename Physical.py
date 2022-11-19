from abc import ABC
from copy import copy
from typing import Tuple

from pymunk import Shape, Body

from Camera import Camera
from Drawable import Drawable


class Physical(Drawable, ABC):

    def __init__(self, shape: Shape, window, camera: Camera):
        super().__init__(window, camera)
        self.shape = shape
        self.body = self.shape.body

    def get_pos(self) -> Tuple[float, float]:
        return self.shape.body.position

    def add_x_velocity(self, x_v):
        self.body.velocity = self.body.velocity[0] + x_v, self.body.velocity[1]

    def add_y_velocity(self, y_v):
        self.body.velocity = self.body.velocity[0], self.body.velocity[1] + y_v

    def add_velocity(self, x=0, y=0):
        self.add_x_velocity(x)
        self.add_y_velocity(y)

    def copy(self):
        ret = Physical(copy(self.shape), self.window, self.camera)
        # ret.shape = copy(self.shape)
        # ret.body = self.shape.body
        return ret
