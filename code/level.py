import pygame 
import time
from settings import *
from player import Player
from enemy import Enemy
from bullet import Bullet
from sprites import Generic

class Level:
	def __init__(self):

		# get the display surface
		self.display_surface = pygame.display.get_surface()

		# sprite groups
		self.all_sprites = CameraGroup()

		#bullets subgroup
		self.bullets = pygame.sprite.Group()
		#enemies subgroup
		self.enemies = pygame.sprite.Group()

		self.players = pygame.sprite.Group()



		self.setup()

	def setup(self):

		self.player = Player((640,360), self.all_sprites)
		self.players.add(self.player)
		self.enemy1 = Enemy((840,660), self.all_sprites, self.player)
		self.enemies.add(self.enemy1) #do usuniecia?
		self.enemy2 = Enemy((900,660), self.all_sprites, self.player)
		self.enemies.add(self.enemy2) #do usuniecia?
		Generic(
			pos = (0,0),
			surf = pygame.image.load("graphics/world/ground.png").convert_alpha(),
			groups= self.all_sprites,
			z = LAYERS["ground"]
		)


	def draw_bullet(self):


		if time.time() - self.player.last_shot > self.player.shot_delay: #shot delay check
			self.new_bullet = Bullet(self.all_sprites,self.player,self.enemies)
			self.bullets.add(self.new_bullet)
			self.player.last_shot = time.time()

	def draw_enemy_bullet(self):

		for enemy in self.enemies:
			if enemy.shot == True:
				if time.time() - enemy.last_shot > enemy.shot_delay: #shot delay check
					self.new_bullet = Bullet(self.all_sprites,enemy,self.players)
					self.bullets.add(self.new_bullet)
					enemy.last_shot = time.time()
	
	#bullet update
	def update_bullet(self):
		for bullet in self.bullets:
			if bullet.bullet_destroy == True:
				self.all_sprites.remove(bullet)
				self.bullets.remove(bullet)

	#enemies update
	def update_enemies(self):
		for enemy in self.enemies:
			if enemy.enemy_destroy == True:
				self.all_sprites.remove(enemy)
				self.enemies.remove(enemy)
				

	def run(self,dt):
		self.display_surface.fill('black')

		self.all_sprites.custom_draw(self.player)
		self.all_sprites.update(dt)

		self.update_enemies()

		self.update_bullet()
		if self.player.shot == True:
			self.draw_bullet()
		
		for enemy in self.enemies:

			if enemy in self.enemies:
				if enemy.shot == True:
					self.draw_enemy_bullet()


class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.offset = pygame.math.Vector2()

	def custom_draw(self, player):
		self.offset.x = player.rect.centerx - (SCREEN_WIDTH - 380) / 2
		self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

		for layer in LAYERS.values():
			for sprite in self.sprites():
				if sprite.z == layer:
					offset_rect = sprite.rect.copy()
					offset_rect.center -= self.offset
					self.display_surface.blit(sprite.image, offset_rect)

		




