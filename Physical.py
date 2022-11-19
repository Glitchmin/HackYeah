from abc import ABC
from typing import Tuple

from pymunk import Shape, Body

from Camera import Camera
from Drawable import Drawable


class Physical(Drawable, ABC):

    def __init__(self, shape: Shape, body: Body, window, camera: Camera):
        super().__init__(window, camera)
        self.shape = shape
        self.body = body

    def get_pos(self) -> Tuple[float, float]:
        return self.shape.body.position
