import math

import pygame
from pymunk import Space

import collisionforbody
from shapes_collection import Ball


class Catapult:

    def __init__(self, space: Space, display: pygame.display, balls: [collisionforbody]):
        self.base_pos = 200, 750-200
        self.mass = 100
        self.angle = -45
        self.length = 200
        self.end_point = 0, 0
        self.space = space
        self.angular_speed = 0.0
        self.calc_end()
        self.display = display
        self.yeet_force = 500
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
        ball = Ball(self.end_point[0], self.end_point[1])
        ball.add_to_space(self.space)
        ball.add_velocity(self.yeet_force * math.sin(math.radians(self.angle - 90)), self.yeet_force * math.cos(math.radians(self.angle - 90)))
        self.balls.append(ball)

    def calc_end(self):
        self.angle += self.angular_speed
        diff = self.length * math.sin(math.radians(self.angle)), self.length * math.cos(math.radians(self.angle))
        self.end_point = self.base_pos[0] + diff[0], self.base_pos[1] + diff[1]

    def draw(self):
        pygame.draw.line(self.display, pygame.Color("brown"), self.base_pos, self.end_point, 5)
