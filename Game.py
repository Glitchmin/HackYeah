import ctypes
import math
import types
from copy import copy

import pygame
import pymunk
import pymunk as pm
from pymunk import CollisionHandler

import GameStates
from Builder import Builder
from BuildingElement import BuildingElement
from Button import Button
from Camera import Camera
from Circle import Circle
from ImageLoader import ImageLoader
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
        self.ch.post_solve = self.pre_solve_collision
        self.width, self.height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.display = pygame.display.set_mode((self.width, self.height))
        self.image_loader = ImageLoader()
        self.ch.data["surface"] = self.display
        self.camera = Camera((self.width, self.height), (0, 0))
        self.drawables = []
        self.run = True
        self.proj_dict = {}
        player1 = Player(True, self, (-1600, 600))
        player2 = Player(False, self, (1600, 600))
        pygame.font.init()

        self.players = [player1, player2]
        self.current_state = GameStates.BUILDING
        self.current_player = 1
        self.current_proj: Circle = None
        self.set_state_to_building()
        self.winner = None
        self.create_ground()
        self.font = pygame.font.SysFont(None, 24)

        self.buttons = []
        self.create_buttons()

        elements_choice = [
            BuildingElement(
                Rectangle(self.display, self.camera, pos=(50, 500), size=(Game.GRID_SIZE * 4, Game.GRID_SIZE * 10),
                          image_loader=self.image_loader, image_name="szary.png"),
                cost=100, hp=10),
        ]
        self.builder = Builder(1000, Game.GRID_SIZE, elements_choice, self.camera)

    def player_won(self, nr):
        self.winner = nr

    def create_ground(self):
        y = self.display.get_height() + 1.1 * 1000
        size_y = 2000
        pos = (-self.display.get_width() * 4, (y - (y - size_y / 2) % Game.GRID_SIZE))
        # pos = (-self.display.get_width() * 4, self.display.get_height() + 200)
        self.ground = Rectangle(self.display, self.camera, pos,
                                size=(100 * self.display.get_width(), size_y), image_loader=self.image_loader,
                                image_name="weed.png", static=True, render_image=False)

        # self.ground_surface = pygame.image.load("testgrass.png")
        # self.ground_surface.convert()
        # self.rect_ground_surface = self.ground_surface.get_rect()
        # self.rect_ground_surface.center = (-100, 100)

        self.ground.color = pygame.Color(0, 255, 100)
        self.drawables.append(self.ground)
        self.space.add(self.ground.shape, self.ground.shape.body)

        # self.ground = Rectangle(self.display, self.camera, (-self.display.get_width()*4, self.display.get_height()+100),
        #                         size=(100 * self.display.get_width(), 200), static=True)
        # self.ground.color = pygame.Color("green")
        # self.drawables.append(self.ground)
        # self.space.add(self.ground.shape, self.ground.shape.body)

    def create_buttons(self):
        button1 = Button(self.display, self.camera, (20, 800),self.font,color=pygame.Color("grey"))
        # button1.action = types.MethodType(self.finish_building, button1)
        self.drawables.append(button1)
        self.buttons.append((button1, self.finish_building))

    def pre_solve_collision(self, arbiter, space, data):
        a, b = arbiter.shapes
        b.collision_type = 0
        b.group = 1
        body1 = a.body
        body2 = b.body

        if self.proj_dict.get(id(body2)) is not None or self.proj_dict.get(id(body1)) is not None:
            def return_proj() -> Circle:
                if self.proj_dict.get(id(body2)) is not None:
                    return self.proj_dict.get(id(body2))
                return self.proj_dict.get(id(body1))

            def return_target() -> BuildingElement:
                if self.builder.body_to_item_dict.get(id(body2)) is not None:
                    return self.builder.body_to_item_dict.get(id(body2))
                if self.builder.body_to_item_dict.get(id(body1)) is not None:
                    return self.builder.body_to_item_dict.get(id(body1))
                for i in [0, 1]:
                    if body1 == self.players[i].king.physical.body or \
                            body2 == self.players[i].king.physical.body:
                        return self.players[i].king
                return None

            proj = return_proj()
            targ = return_target()
            if targ is not None and proj is not None:
                targ.hp -= (proj.mass * (
                        proj.body.velocity[0] * proj.body.velocity[0] + proj.body.velocity[1] * proj.body.velocity[1]))
                if targ.hp <= 0:
                    if targ == self.players[0].king:
                        self.player_won(1)
                    if targ == self.players[1].king:
                        self.player_won(0)
                    if targ.physical in self.drawables:
                        self.drawables.remove(targ.physical)
                        self.space.remove(targ.physical.body, targ.physical.shape)

        return True

    def set_state_to_building(self):
        self.space.gravity = 0, 0
        self.current_player += 1
        self.current_player %= 2
        self.current_state = GameStates.BUILDING
        self.camera.target = None
        self.camera.set_center(self.players[self.current_player].pos_center)

    def set_state_to_firing(self):
        if len(self.buttons)==1:
            self.drawables.remove(self.buttons[0][0])
            self.buttons.clear()
        self.current_state = GameStates.FIRING
        self.current_player += 1
        self.current_player %= 2
        self.players[self.current_player].playerTurn()
        if self.players[1-self.current_player].catapult is not None:
            self.players[1-self.current_player].catapult.isHidden = True
        self.camera.target = self.players[self.current_player].catapult
        self.space.gravity = 0, 900

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
        if self.winner is not None:
            self.display.fill(pygame.Color(0,255,255))
            font = pygame.font.SysFont(None, 72)
            img = font.render('player '+str(self.winner+1)+' wins', True, pygame.Color("black") )
            self.display.blit(img, (self.width/2-img.get_size()[0]/2, self.height/2))
        for ball in to_remove:
            self.space.remove(ball.shape, ball.body)
            self.drawables.remove(ball)

    def display_frame(self, clock):
        pygame.display.update()
        self.display.fill(pygame.Color(0, 208, 230))
        clock.tick(Game.FPS)

    def finish_building(self):
        if self.current_state == GameStates.BUILDING:
            self.set_state_to_building()
            if self.current_player == 0:
                self.current_player = 1
                self.set_state_to_firing()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                button_clicked = False

                for button, action in self.buttons:
                    if button.hovers(pos):
                        button_clicked = True
                        # button.action()
                        action()

                if self.current_state == GameStates.BUILDING and not button_clicked:
                    print(pos)
                    element = self.builder.build(pos)
                    if element is not None:
                        self.space.add(element.physical.shape, element.physical.body)
                        self.drawables.append(element.physical)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.builder.angle += math.pi / 2
                if event.key == pygame.K_e:
                    self.builder.angle -= math.pi / 2
                if event.key == pygame.K_p:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    circle = Circle(self.display, self.camera, pos)
                    self.space.add(circle.shape, circle.body)
                    self.drawables.append(circle)

                if event.key == pygame.K_SPACE and self.current_state == GameStates.FIRING:
                    if self.current_proj is None:
                        projectile = self.players[self.current_player].catapult.space_clicked()
                        if projectile is not None:
                            self.proj_dict[id(projectile.body)] = projectile
                            self.camera.target = projectile
                            self.space.add(projectile.body, projectile.shape)
                            self.current_proj = projectile
                    else:
                        self.current_proj = None
                        self.set_state_to_firing()

                if event.key == pygame.K_RETURN:
                    self.finish_building()

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
