from collisionforbody import *
import pygame,pymunk


class Ball(CollisionForBody):
    def __init__(self, x, y):
        CollisionForBody.__init__(self, x, y)
        self.add_velocity(0, 0)
        self.body.body_type = pymunk.Body.DYNAMIC
        self.setshape("ball")
        self.shape.density = 1
        self.shape.elasticity = 1
        self.shape.collision_type = 1

    def add_to_space(self, space):
        space.add(self.body, self.shape)

    def draw(self, WINDOW, COLOR):
        x, y = self.body.position
        pygame.draw.circle(WINDOW, COLOR, self.body.position, 8) # problemy do rozw ale odpalic trzeba

#class wall(collision_for_body):
#    def __init__(self, left_corner, top_corner):