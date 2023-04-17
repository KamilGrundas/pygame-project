import pygame
from settings import *
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        #general setup
        self.image = pygame.transform.rotozoom(pygame.image.load("graphics/character/down/0.png").convert_alpha(),0,PLAYER_SIZE)
        self.base_player_image = self.image
        self.rect = self.image.get_rect(center = pos)

        #movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        self.shot = False


    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
            
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_f]:
            self.shot = True
        else:
            self.shot = False



        

    def move(self,dt):

        #normalizing a vector
        # if self.direction != [0,0]:

        if self.direction.magnitude() > 0 :
            self.direction = self.direction.normalize()

        #horizontal movement

        self.pos.x += self.direction.x * self.speed * dt

        self.rect.centerx = self.pos.x

        #vertical movement

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y


    def get_angle(self):

        self.mouse_pos = pygame.mouse.get_pos()
        self.x_change = (self.mouse_pos[0] - self.pos.x)
        self.y_change = (self.mouse_pos[1] - self.pos.y)
        self.angle = math.degrees(math.atan2(self.y_change, self.x_change))


    def update(self,dt):
        self.input()
        self.move(dt)
        self.get_angle()
