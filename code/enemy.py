import pygame
from settings import *
import math
from support import *
import time

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group, player):
        super().__init__(group)


        #general setup
        # self.image = pygame.image.load("graphics/character/down/0.png").convert_alpha()
        self.image = pygame.Surface((30,70))
        self.image.fill("red")
        self.rect = self.image.get_rect(center = pos)
        self.enemy_destroy = False
        self.health = 1000

        self.last_shot = time.time()


        #player import
        self.player = player
        
        # self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS["fruit"]

        #movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.agro = False
        self.speed = 120
        # self.direction.x = 1

        #shooting attributes
        self.shot = False
        self.shot_delay = 0.5
        self.shot_range = 200
        self.projectile_speed = 200
        angle = 0
        bullets = 1
        self.pattern = [angle, bullets]
        self.piercing = False
        self.weapon_damage = [15,75]

            #stats
        self.attack_stat = 1.1
        self.dextarity_stat = 1
        self.vitality_stat = 1
        self.wisdom_stat = 1
        self.defense_stat  = 1
        self.speed_stat = 1


    def health_update(self):
        
        if self.health <= 0:
            self.shot = False
            self.enemy_destroy = True

    def ai(self, dt):

        self.x_change = (self.player.pos.x - self.pos.x)
        self.y_change = (self.player.pos.y - self.pos.y)
        self.angle = math.degrees(math.atan2(self.y_change, self.x_change))

        #velocity in x/y
        self.x_vel = math.cos(self.angle * (2*math.pi/360))
        self.y_vel = math.sin(self.angle * (2*math.pi/360))

        if (self.player.pos.x - self.pos.x)**2 + (self.player.pos.y - self.pos.y)**2 < 50000:
            self.agro = True
        else:
            self.agro = False

        if self.agro == True:
            self.pos.x += self.x_vel * self.speed * dt
            self.pos.y += self.y_vel * self.speed * dt


        # if self.agro == False:
        #     if self.pos.x >= 1000:
        #         self.direction.x = -1
        #     if self.pos.x <= 700:
        #         self.direction.x = 1

    def shooting(self):
        if self.agro == True:
            self.shot = True

        if self.agro == False:
            self.shot = False
    


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
        self.ai(dt)
        self.move(dt)
        self.health_update()
        self.shooting()
