import math
from typing import Tuple

import pygame
from pymunk import Vec2d

from Circle import Circle
from Drawable import Drawable
from ImageLoader import ImageLoader


class Catapult(Drawable):

    def __init__(self, game, isFirstPlayer: bool, base_pos: Tuple[float, float], image_loader: ImageLoader):
        super().__init__(game.display, game.camera)
        self.base_pos = base_pos
        # self.base_pos = 200, 500
        # if not isFirstPlayer:
        #     self.base_pos = 1200, 500
        self.mass = 100
        self.angle = -45
        self.length = 200
        self.end_point = 0.0, 0.0
        self.space = game.space
        self.angular_speed = 0.0
        self.calc_end()
        self.yeet_force = 1550
        self.is_spinning = False
        self.drawables = game.drawables
        self.isFirstPlayer: bool = isFirstPlayer
        self.image_loader = image_loader
        self.isHidden = False
        self.ball = None

    def space_clicked(self):
        if not self.is_spinning:
            self.isHidden = False
            self.is_spinning = True
            if self.isFirstPlayer:
                self.angle = -45
                self.angular_speed = -7
            else:
                self.angle = 45
                self.angular_speed = 7
            return
        self.angular_speed = 0
        self.is_spinning = False
        ball = Circle(self.window, self.camera, self.end_point)
        if not self.isFirstPlayer:
            self.angle += 180
        ball.add_velocity(self.yeet_force * math.sin(math.radians(self.angle - 90)),
                          self.yeet_force * math.cos(math.radians(self.angle - 90)))
        self.camera.follow(ball)
        self.drawables.append(ball)
        self.ball = ball
        # self.isHidden = True
        return ball

    def calc_end(self):
        self.angle += self.angular_speed
        diff = self.length * math.sin(math.radians(self.angle)), self.length * math.cos(math.radians(self.angle))
        self.end_point = self.base_pos[0] + diff[0], self.base_pos[1] + diff[1]

    def draw(self):
        if self.isHidden:
            return
        self.calc_end()
        base_point = self.camera.to_scr_pos(self.base_pos)
        end_point = self.camera.to_scr_pos(self.end_point)
        # pygame.draw.line(self.window, pygame.Color("brown"), base_point, end_point, 5)
        self.image_loader.draw_on_pos(base_point + Vec2d(40, 30), (200, 100), "giraffe.png", self.window)
        self.image_loader.draw_on_pos((Vec2d(*end_point) + Vec2d(*base_point)) / 2, (100, 270),
                                      "full_loong_giraffe_head.png", self.window, math.radians(-self.angle+180))
        if self.is_spinning:
            pygame.draw.circle(self.window, pygame.Color("gray"), end_point, int(25), width=0)


    def get_pos(self) -> Tuple[float, float]:
        return self.base_pos
