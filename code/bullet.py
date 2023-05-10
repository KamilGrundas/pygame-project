import pygame
import math
from settings import *

class Bullet(pygame.sprite.Sprite):

    def __init__(self,x,y,angle,range, speed, group, enemies, piercing): #enemies do usuniecia ?
        super().__init__(group)
        
        #dousuniecia
        self.enemies = enemies

        #general setup
        self.image = pygame.Surface((15,15))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.bullet_destroy = False
        self.range = range
        self.piercing = piercing
        self.hit_enemies = pygame.sprite.Group()
        self.angle = angle
        self.x = x
        self.y = y
        self.bullet_speed = speed
        self.z = LAYERS["main"]

        #velocity in x/y
        self.x_vel = math.cos(angle * (2*math.pi/360))
        self.y_vel = math.sin(angle * (2*math.pi/360))

        #range
        self.endposx = x + self.x_vel * range
        self.endposy = y + self.y_vel * range


    def destroy(self):

        #range destroy

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

        #collision destroy

        

        for enemy in self.enemies:
                
            if self.rect.colliderect(enemy) and self.bullet_destroy == False and enemy not in self.hit_enemies: #second condition prevents hitting multiple targets, third condition prevents double hit
                enemy.health -= 10
                self.hit_enemies.add(enemy)
                print(enemy.health)
                if self.piercing == False:
                    self.bullet_destroy = True
            

    def move(self,dt):
    
        self.x += self.x_vel * self.bullet_speed * dt
        self.y += self.y_vel * self.bullet_speed * dt
        
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self,dt):
        self.move(dt)
        self.destroy()




