import ctypes
from copy import copy

import pygame
import pymunk
import pymunk as pm
from pymunk import CollisionHandler

import GameStates
from Builder import Builder
from BuildingElement import BuildingElement
from Camera import Camera
from Catapult import Catapult
from Circle import Circle
from Player import Player
from Rectangle import Rectangle


class Game:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    FPS = 60
    GRID_SIZE = 15

    def __init__(self):
        user32 = ctypes.windll.user32
        self.space = pm.Space()
        self.space.gravity = (0.0, 900.0)
        self.ch: CollisionHandler = self.space.add_collision_handler(0, 0)
        self.ch.pre_solve = self.pre_solve_collision
        self.width, self.height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.display = pygame.display.set_mode((self.width, self.height))
        self.ch.data["surface"] = self.display
        self.camera = Camera((self.width, self.height), (0, 0))
        self.drawables = []
        self.run = True
        self.players = [Player(True, self), Player(False, self)]
        self.current_state = GameStates.BUILDING
        self.current_player = 1
        self.current_proj: Circle = None
        self.set_state_to_building()


        self.create_ground()

        elements_choice = [
            BuildingElement(
                Rectangle(self.display, self.camera, pos=(50, 500), size=(Game.GRID_SIZE * 4, Game.GRID_SIZE * 6)),
                cost=100),
        ]
        self.builder = Builder(1000, Game.GRID_SIZE, elements_choice, self.camera)

    def create_ground(self):
        y = self.display.get_height() + 1.1 * 1000
        size_y = 2000
        pos = (-self.display.get_width() * 4, (y - (y - size_y / 2) % Game.GRID_SIZE))
        self.ground = Rectangle(self.display, self.camera, pos,
                                size=(100 * self.display.get_width(), size_y), static=True)
        self.ground.color = pygame.Color("green")
        self.drawables.append(self.ground)
        self.space.add(self.ground.shape, self.ground.shape.body)

        # self.ground = Rectangle(self.display, self.camera, (-self.display.get_width()*4, self.display.get_height()+100),
        #                         size=(100 * self.display.get_width(), 200), static=True)
        # self.ground.color = pygame.Color("green")
        # self.drawables.append(self.ground)
        # self.space.add(self.ground.shape, self.ground.shape.body)

    def pre_solve_collision(self, arbiter, space, data):
        a, b = arbiter.shapes
        b.collision_type = 0
        b.group = 1
        body1 = a.body
        body2 = b.body
        # print(body1.velocity, end=" ")
        # print(body2.velocity)
        # print(self.builder.body_to_item_dict.get(id(body1)))
        # print(self.builder.body_to_item_dict.get(id(body2)))
        return True

    def set_state_to_building(self):
        self.space.gravity = 0, 0
        self.current_player += 1
        self.current_player %= 2
        self.current_state = GameStates.BUILDING
        self.camera.target = None
        self.camera.set_center((200, 600))
        if self.current_player == 1:
            self.camera.set_center((800, 600))

    def set_state_to_firing(self):
        self.current_state = GameStates.FIRING
        self.current_player += 1
        self.current_player %= 2
        self.players[self.current_player].playerTurn()
        self.camera.target = self.players[self.current_player].catapult
        self.space.gravity = 0, 900

    def apply_rules(self):
        if self.current_state == GameStates.FIRING:
            if self.current_proj is not None and self.current_proj.is_not_moving():
                self.current_proj = None
                self.set_state_to_firing()

    def calculate_physics(self):
        dt = 1.0 / 60.0
        for x in range(1):
            self.space.step(dt)

    def update_screen(self, clock):
        self.update_drawable()
        if self.current_state == GameStates.BUILDING:
            self.builder.show_selected(pygame.mouse.get_pos())

        self.display_frame(clock)

    def update_drawable(self):
        to_remove = []
        for drawable in self.drawables:
            # if drawable.get_pos()[1] > 400:
            #     to_remove.append(drawable)
            p = tuple(map(int, drawable.get_pos()))
            drawable.draw()
        for ball in to_remove:
            self.space.remove(ball.shape, ball.body)
            self.drawables.remove(ball)

    def display_frame(self, clock):
        pygame.display.update()
        self.display.fill(pygame.Color("white"))
        clock.tick(Game.FPS)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and self.current_state == GameStates.BUILDING:
                pos = pygame.mouse.get_pos()
                print(pos)
                element = self.builder.build(pos)
                if element is not None:
                    self.space.add(element.shape, element.body)
                    self.drawables.append(element)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pos = pygame.mouse.get_pos()
                print(pos)
                circle = Circle(self.display, self.camera, pos)
                self.space.add(circle.shape, circle.body)
                self.drawables.append(circle)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and \
                    self.current_state == GameStates.FIRING:
                if self.current_proj is None:
                    projectile = self.players[self.current_player].catapult.space_clicked()
                    if projectile is not None:
                        self.camera.target = projectile
                        self.space.add(projectile.body, projectile.shape)
                        self.current_proj = projectile
                else:
                    self.current_proj = None
                    self.set_state_to_firing()

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if self.current_state == GameStates.BUILDING:
                    self.set_state_to_building()
                if self.current_player == 0:
                    self.current_player = 1
                    self.set_state_to_firing()
