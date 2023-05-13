import pygame
import math
from settings import *
import random

class Bullet(pygame.sprite.Sprite):

    def __init__(self, group, player, enemies): #enemies do usuniecia ?
        super().__init__(group)
        
        #dousuniecia
        self.enemies = enemies

        #general setup
        self.image = pygame.Surface((15,15))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.center = (player.pos.x,player.pos.y)
        self.bullet_destroy = False
        self.range = player.shot_range
        self.piercing = player.piercing
        self.hit_enemies = pygame.sprite.Group()
        self.angle = player.angle
        self.x = player.pos.x
        self.y = player.pos.y
        self.bullet_speed = player.projectile_speed
        self.z = LAYERS["main"]

        #damge
        self.damage = int(random.randrange(player.weapon_damage[0],player.weapon_damage[1],1) * (player.attack_stat))

        #sound
        bulletSound = pygame.mixer.Sound("audio/bladeSwing.mp3")
        bulletSound.play()

        #velocity in x/y
        self.x_vel = math.cos(self.angle * (2*math.pi/360))
        self.y_vel = math.sin(self.angle * (2*math.pi/360))

        #range
        self.endposx = player.pos.x + self.x_vel * player.shot_range
        self.endposy = player.pos.y + self.y_vel * player.shot_range


    def destroy(self):

        #range destroy

        if (self.x - self.endposx)**2 + (self.y - self.endposy)**2 < self.range:

            self.bullet_destroy = True


        #collision destroy

        

        for enemy in self.enemies:
                
            if self.rect.colliderect(enemy) and self.bullet_destroy == False and enemy not in self.hit_enemies: #second condition prevents hitting multiple targets, third condition prevents double hit
                enemy.health -= self.damage
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




