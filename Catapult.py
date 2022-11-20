import math
from typing import Tuple

import pygame
from Circle import Circle
from Drawable import Drawable


class Catapult(Drawable):

    def __init__(self, game, isFirstPlayer: bool):
        super().__init__(game.display, game.camera)
        self.base_pos = 200, 500
        if not isFirstPlayer:
            self.base_pos = 1200, 500
        self.mass = 100
        self.angle = -45
        self.length = 200
        self.end_point = 0.0, 0.0
        self.space = game.space
        self.angular_speed = 0.0
        self.calc_end()
        self.yeet_force = 1000
        self.is_spinning = False
        self.drawables = game.drawables
        self.isFirstPlayer: bool = isFirstPlayer
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
        self.isHidden = True
        return ball

    def is_ball_not_moving(self):
        if self.ball is None:
            return False
        return abs(self.ball.body.velocity[0]) + abs(self.ball.body.velocity[1]) <= 1.0 or self.ball.body.position[
            1] > 1500

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
        pygame.draw.line(self.window, pygame.Color("brown"), base_point, end_point, 5)

    def get_pos(self) -> Tuple[float, float]:
        return self.base_pos
