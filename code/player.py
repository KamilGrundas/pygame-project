import pygame
from settings import *
import math
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assets()
        self.status = "down"
        self.frame_index = 0

        #general setup
        self.image = self.animations[self.status][self.frame_index]
        self.base_player_image = self.image
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS["main"]

        #movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        #shooting attributes
        self.shot = False
        self.shot_delay = 0.1
        self.shot_range = 200
        self.projectile_speed = 600

    def import_assets(self):
        self.animations = {"up":[],"down":[],"left":[],"right":[],
                           "right_idle":[],"left_idle":[],"up_idle":[],"down_idle":[],}

        for animation in self.animations.keys():
            full_path = "graphics/character/" + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self,dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):

        mouse = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.status = "down"
        else:
            self.direction.y = 0
            
        if keys[pygame.K_d]:
            self.direction.x = 1
            self.status = "right"
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.status= "left"
        else:
            self.direction.x = 0

        if mouse[0]:
            self.shot = True
        else:
            self.shot = False

    def get_status(self):

        #idle
        if self.direction.magnitude() == 0:
            self.status =  self.status.split("_")[0] + "_idle"


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
        self.x_change = ((self.mouse_pos[0] + self.pos.x - (SCREEN_WIDTH/2)) - self.pos.x)
        self.y_change = (self.mouse_pos[1] + self.pos.y - (SCREEN_HEIGHT/2) - self.pos.y)
        self.angle = math.degrees(math.atan2(self.y_change, self.x_change))


    def update(self,dt):
        self.input()
        self.get_status()
        self.move(dt)
        self.get_angle()
        self.animate(dt)
