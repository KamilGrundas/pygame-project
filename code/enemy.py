import pygame
from settings import *
import math
from support import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)


        #general setup
        # self.image = pygame.image.load("graphics/character/down/0.png").convert_alpha()
        self.image = pygame.Surface((30,70))
        self.image.fill("red")
        self.rect = self.image.get_rect(center = pos)
        self.enemy_destroy = False
        self.health = 100
        
        # self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS["fruit"]

        #movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        #shooting attributes
        self.shot = False
        self.shot_delay = 0.1
        self.shot_range = 200
        self.projectile_speed = 600


    def health_update(self):
        
        if self.health <= 0:
            self.enemy_destroy = True


    def move(self,dt):

        if self.direction.magnitude() > 0 :
            self.direction = self.direction.normalize()

        #horizontal movement

        self.pos.x += self.direction.x * self.speed * dt

        self.rect.centerx = self.pos.x

        #vertical movement

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y





    def update(self,dt):
        self.move(dt)
        self.health_update()
