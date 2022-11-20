from typing import Tuple

import pygame
from Camera import Camera
from Drawable import Drawable
from ImageLoader import ImageLoader
from Physical import Physical


class TextureRectangle(Physical):
    def __init__(self,shape, body, display, image_name: str,image_loader: ImageLoader, camera: Camera, pos: Tuple[float, float], size: Tuple[float, float]):
        self.display = display
        self.size = size
        self.image_loader = image_loader
        self.image_name = image_name
        self.pos = pos
        super().__init__(shape, body, display, camera)

    def get_size(self) -> Tuple[float, float]:
        return self.size

    def draw(self):
        screen_position = self.camera.to_scr_pos(self.get_pos())
        self.image_loader.draw_on_pos(screen_position, self.get_size(), self.image_name, self.display)

    #def draw_on_pos(self, pos: Tuple[float, float]):
    #    self.display.blit(pygame.transform.scale(self.image, self.get_size()), pygame.Rect(*pos, *self.get_size()))
