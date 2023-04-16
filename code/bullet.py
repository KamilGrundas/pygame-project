import pygame
import math
from settings import *

class Bullet(pygame.sprite.Sprite):

    def __init__(self,x,y,angle, group):
        super().__init__(group)
        
        #general setup
        self.image = pygame.Surface((15,15))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.x = x
        self.y = y
        self.bullet_speed = 200
        self.x_vel = math.cos(angle * (2*math.pi/360)) * self.bullet_speed
        self.y_vel = math.sin(angle * (2*math.pi/360)) * self.bullet_speed


    def move(self,dt):
        self.x += self.x_vel * dt
        self.y += self.y_vel * dt

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)


    def update(self,dt):
        self.move(dt)




