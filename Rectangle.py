from typing import Tuple

import pygame
from pymunk import Shape, Vec2d

from Camera import Camera
from ImageLoader import ImageLoader
from Physical import Physical
import pymunk as pm

from TextureRectangle import TextureRectangle


class Rectangle(Physical):
    def get_size(self) -> Tuple[float, float]:
        return self.size

    def __init__(self, window, camera: Camera, pos: Tuple[float, float], size: Tuple[float, float],
                 image_loader: ImageLoader, image_name: str, mass=10,
                 friction=1, static: bool = False, render_image: bool = True):
        self.render_image = render_image
        self.mass = mass
        self.size = size
        body = None
        if static:
            body = pm.Body(body_type=pm.Body.STATIC)
        else:
            inertia = pm.moment_for_box(mass, size)
            body = pm.Body(mass, inertia)
        body.position = pos
        shape = pm.Poly.create_box(body, size, .1)
        shape.friction = friction
        self.image_loader = image_loader
        self.image_name = image_name
        self.color = pygame.Color("grey")
        self.texture = TextureRectangle(shape, window, self.image_name, self.image_loader, camera, pos, size)

        super().__init__(shape, window, camera)

    def draw(self):
        screen_position = self.camera.to_scr_pos(self.get_pos())
        self.draw_on_pos(screen_position)

    def draw_on_pos(self, pos: Tuple[float, float]):
        if (self.render_image):
            self.texture.draw()
        else:
            pygame.draw.rect(self.window, self.color, rect=pygame.Rect(*(pos - Vec2d(*self.size)/2), *self.get_size()))

    def copy(self):
        ret = Rectangle(self.window, self.camera, self.get_pos(), self.size, image_loader=self.image_loader,
                        image_name=self.image_name)
        return ret
