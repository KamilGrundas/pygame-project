import pygame 
from settings import *
from player import Player
from bullet import Bullet

class Level:
	def __init__(self):

		# get the display surface
		self.display_surface = pygame.display.get_surface()

		# sprite groups
		self.all_sprites = pygame.sprite.Group()

		self.setup()

	def setup(self):
		self.player = Player((640,360), self.all_sprites)

	def draw_bullet(self,x,y,angle):
		self.new_bullet = Bullet(x,y,angle,self.all_sprites)

	def run(self,dt):
		self.display_surface.fill('black')
		self.all_sprites.draw(self.display_surface)
		self.all_sprites.update(dt)

		keys = pygame.key.get_pressed()

		if keys[pygame.K_f]:
			self.draw_bullet(self.player.rect.centerx,self.player.rect.centery,self.player.angle)

		




