import pygame
import random

#definir une class qui va gérer les monstres
class Monster(pygame.sprite.Sprite):
	def __init__(self, game):
		super().__init__()
		self.game = game
		self.health = 100
		self.max_health = 100
		self.attack = 0.3
		self.image =pygame.image.load('assets/mummy.png')
		self.rect = self.image.get_rect()
		self.rect.x = 1000 +random.randint(0,300)
		self.rect.y = 540
		self.velocity = random.randint(1, 3)

	def damage(self, amount):
		#Infliger des degat
		self.health -=amount

		#verrifier si c inferieur ou egale 0
		if self.health <=0 :
			#réapparaite
			self.rect.x = 1000 + random.randint(0, 300)
			self.velocity=random.randint(1, 3)
			self.health=self.max_health

			#Si la barre d'evenement est charger a 100
			if self.game.comet_event.is_full_loaded():
				#le retirer du jeux
				self.game.all_monsters.remove(self)

				#Apelll de la methode pour declencher la plui
				self.game.comet_event.attempt_fall()



	def update_health_bar(self, surface):
		#dessiner notre barre de vie
		pygame.draw.rect(surface, (60,63,60), [self.rect.x+10, self.rect.y-20, self.max_health, 5])
		pygame.draw.rect(surface, (111,210,46), [self.rect.x+10, self.rect.y-20, self.health, 5])


	def forward(self):
		#le deplacement ne se fait que si il n'y a pas de collision avec un joueur
		if not self.game.check_collision(self, self.game.all_players):
			self.rect.x -= self.velocity	
			#si le monstre est en collision avec ke joueur
		else :
			#infliger des degat
			self.game.player.damage(0.3)
