import ctypes
from copy import copy

import pygame
import pymunk as pm
from pymunk import Body

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

    def __init__(self):
        user32 = ctypes.windll.user32
        self.space = pm.Space()
        self.space.gravity = (0.0, 900.0)
        self.ch = self.space.add_collision_handler(0, 0)
        self.width, self.height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.display = pygame.display.set_mode((self.width, self.height))
        self.ch.data["surface"] = self.display
        self.camera = Camera((self.width, self.height), (0, 0))
        self.drawables = []
        self.run = True
        self.players = [Player(True, self), Player(False, self)]
        self.current_state = GameStates.BUILDING
        self.current_player = 0

        elements_choice = [
            BuildingElement(Rectangle(self.display, self.camera, pos=(50, 500), size=(10, 50)), cost=100),
        ]
        self.builder = Builder(1000, 15, elements_choice)

    def set_state_to_building(self):
        self.current_player += 1
        self.current_player %= 2
        self.current_state = GameStates.BUILDING
        self.camera.follow(self.players[self.current_player].catapult)

    def set_state_to_firing(self):
        self.current_state = GameStates.FIRING
        self.players[self.current_player].playerTurn()


    def apply_rules(self):
        if self.current_state == GameStates.BUILDING:
            self.space.gravity = 0, 0
        if self.current_state == GameStates.FIRING:
            self.space.gravity = 0, 900
            if self.players[self.current_player].catapult.is_ball_not_moving():
                print("ball stopped")
                self.set_state_to_building()


    def calculate_physics(self):
        dt = 1.0 / 60.0
        for x in range(1):
            self.space.step(dt)

    def update_screen(self, clock):
        self.update_drawable()
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

    def handle_input(self, catapult: Catapult):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.current_state == GameStates.FIRING:
                projectile = self.players[self.current_player].catapult.space_clicked()
                if projectile is not None:
                    self.space.add(projectile.body, projectile.shape)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if self.current_state == GameStates.BUILDING:
                    self.set_state_to_firing()
