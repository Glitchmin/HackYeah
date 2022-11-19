import math
from typing import Tuple

import pygame
from pymunk import Space

import collisionforbody
from Camera import Camera
from Circle import Circle
from Drawable import Drawable
from shapes_collection import Ball


class Catapult(Drawable):

    def __init__(self, space: Space, balls: [collisionforbody], window, camera: Camera):
        super().__init__(window, camera)
        self.base_pos = 200, 500 - 200
        self.mass = 100
        self.angle = -45
        self.length = 200
        self.end_point = 0.0, 0.0
        self.space = space
        self.angular_speed = 0.0
        self.calc_end()
        self.yeet_force = 1000
        self.is_spinning = False
        self.balls = balls

    def space_clicked(self):
        if not self.is_spinning:
            self.angle = -45
            self.angular_speed = -7
            self.is_spinning = True
            return
        self.angular_speed = 0
        self.is_spinning = False
        ball = Circle(self.window, self.camera, self.end_point)
        ball.add_velocity(self.yeet_force * math.sin(math.radians(self.angle - 90)),
                          self.yeet_force * math.cos(math.radians(self.angle - 90)))
        self.balls.append(ball)
        return ball

    def calc_end(self):
        self.angle += self.angular_speed
        diff = self.length * math.sin(math.radians(self.angle)), self.length * math.cos(math.radians(self.angle))
        self.end_point = self.base_pos[0] + diff[0], self.base_pos[1] + diff[1]

    def draw(self):
        self.calc_end()
        pygame.draw.line(self.window, pygame.Color("brown"), self.base_pos, self.end_point, 5)

    def get_pos(self) -> Tuple[float, float]:
        return self.end_point
