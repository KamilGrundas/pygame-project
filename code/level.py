import pygame 
import time
from settings import *
from player import Player
from bullet import Bullet
from sprites import Generic

class Level:
	def __init__(self):

		# get the display surface
		self.display_surface = pygame.display.get_surface()

		# sprite groups
		self.all_sprites = CameraGroup()

		#bullets group
		self.bullets = pygame.sprite.Group()
		self.last_shot = time.time()

		self.setup()

	def setup(self):
		Generic(
			pos = (0,0),
			surf = pygame.image.load("graphics/world/ground.png").convert_alpha(),
			groups= self.all_sprites
		)
		self.player = Player((640,360), self.all_sprites)

	def draw_bullet(self):


		if time.time() - self.last_shot > self.player.shot_delay: #shot delay check
			self.new_bullet = Bullet(self.player.rect.centerx,self.player.rect.centery,self.player.angle,self.player.shot_range,self.player.projectile_speed,self.bullets)
			self.bullets.add(self.new_bullet)
			self.last_shot = time.time()
	
	def update_bullet(self):
		for bullet in self.bullets:
			if bullet.bullet_destroy == True:
				self.bullets.remove(bullet)

	def run(self,dt):
		self.display_surface.fill('black')
		# self.all_sprites.draw(self.display_surface)
		self.all_sprites.custom_draw()
		self.all_sprites.update(dt)
		self.bullets.draw(self.display_surface)
		self.bullets.update(dt)
		self.update_bullet()
		if self.player.shot == True:
			self.draw_bullet()


class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()

	def custom_draw(self):
		for sprite in self.sprites():
			self.display_surface.blit(sprite.image, sprite.rect)

		




