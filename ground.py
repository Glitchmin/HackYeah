from typing import Tuple

import pygame, pymunk

from Camera import Camera
from Drawable import Drawable

GREEN = (0, 255, 0)


class Ground(Drawable):
    def __init__(self, window, space, camera: Camera, height=50):
        super().__init__(window, camera)
        self.space = space
        self.height = height
        self.width = 100 * window.get_width()
        self.color = GREEN

        self.pos = (0, self.window.get_height() - self.height)

        body = pymunk.Body(body_type=pymunk.Body.STATIC)

        camera_position = self.camera.to_scr_pos(self.pos)

        w, h = self.width, self.height
        body.position = camera_position[0] + w / 2, camera_position[1] + h / 2
        vs = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]
        shape = pymunk.Poly(body, vs)
        shape.friction = 1

        self.shape = shape
        self.body = body

        self.space.add(body, shape)

    def draw(self):
        camera_position = self.camera.to_scr_pos(self.pos)

        self.draw_on_pos(camera_position)

    def draw_on_pos(self, pos: Tuple[float, float]):
        rect = pygame.Rect(*pos, self.width, self.height)
        pygame.draw.rect(self.window, GREEN, rect)

    def get_pos(self) -> Tuple[float, float]:
        return self.pos
