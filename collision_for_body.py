from libraries import *
import pygame,pymunk

shapes = {"ball" : pymunk.Circle} #ENUM?

class collision_for_body(object):
    def __init__(self, x, y):
        self.body = pymunk.Body(1, 100)
        self.body.position = x, y
        self.body.velocity = 0, 0
        self.shape = None

    def setshape(self, shapename):
        self.shape = shapes[shapename](self.body, 8)

    def add_x_velocity(self, x_v):
        self.body.velocity = self.body.velocity[0] + x_v, self.body.velocity[1]

    def add_y_velocity(self, y_v):
        self.body.velocity = self.body.velocity[0] , self.body.velocity[1] + y_v

    def add_velocity(self, x = 0, y = 0):
        self.add_x_velocity(x)
        self.add_y_velocity(y)