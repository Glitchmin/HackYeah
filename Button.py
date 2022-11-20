from typing import Tuple

import pygame

from Drawable import Drawable


class Button(Drawable):
    def __init__(self, window, camera, pos, size=(100, 50), color=pygame.Color("RED")):
        super(Button, self).__init__(window, camera)
        self.pos = pos
        self.size = size
        self.color = color
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def get_pos(self) -> Tuple[float, float]:
        return self.pos

    def get_size(self) -> Tuple[float, float]:
        return self.size

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

    def draw_on_pos(self, pos: Tuple[float, float]):
        new_rect = pygame.Rect(pos[0], pos[1], self.size[0], self.size[1])

    def hovers(self, mouse_pos):
        return (self.pos[0] <= mouse_pos[0] <= self.pos[0] + self.size[0] and
                self.pos[1] <= mouse_pos[1] <= self.pos[1] + self.size[1])

    def action(self):
        print("EMPTY ACTION CALLED!!1")