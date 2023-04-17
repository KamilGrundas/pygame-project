import pygame
import math
from settings import *

class Bullet(pygame.sprite.Sprite):

    def __init__(self,x,y,angle,range, speed, group):
        super().__init__(group)
        
        #general setup
        self.image = pygame.Surface((15,15))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.startposx = x
        self.startposy = y
        self.range = range
        self.angle = angle
        self.x = x
        self.y = y
        self.bullet_destroy = False
        self.bullet_speed = speed
        self.x_vel = math.cos(angle * (2*math.pi/360))
        self.y_vel = math.sin(angle * (2*math.pi/360))

        self.endposx = self.startposx + self.x_vel*range
        self.endposy = self.startposy + self.y_vel*range


    def range_destroy(self):

        if self.angle >= 0 and self.angle <= 90:
            if self.x > self.endposx or self.y > self.endposy:
                self.bullet_destroy = True
        
        elif self.angle > 90 and self.angle <= 180:
            if self.x < self.endposx or self.y > self.endposy:
                self.bullet_destroy = True

        elif self.angle < 0 and self.angle >= -90:
            if self.x > self.endposx or self.y < self.endposy:
                self.bullet_destroy = True
        else:
            if self.x < self.endposx or self.y < self.endposy:
                self.bullet_destroy = True

    def move(self,dt):
        self.x += self.x_vel * self.bullet_speed * dt
        self.y += self.y_vel * self.bullet_speed * dt
        

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def update(self,dt):
        self.move(dt)
        self.range_destroy()




