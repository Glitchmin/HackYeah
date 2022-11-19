import pygame, pymunk

from Camera import Camera
from Drawable import Drawable

GREEN = (0, 255, 0)


class Ground(Drawable):
    def __init__(self, window, space, camera: Camera, height=50):
        super().__init__(window, camera)
        self.space = space
        self.height = height
        self.width = window.get_width()
        self.color = GREEN

        self.pos = (0, self.window.get_height() - self.height)

    def draw(self):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        w, h = self.width, self.height

        body.position = self.pos[0] + w / 2, self.pos[1] + h / 2

        rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        pygame.draw.rect(self.window, GREEN, rect)

        vs = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]
        shape = pymunk.Poly(body, vs)

        self.space.add(body, shape)
