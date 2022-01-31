import pygame
import random
import animation

#Créer une classe qui va représenter les monstres
class Monster(animation.AnimateSprite):
	def __init__(self, game, name, size, offset=0):
		super().__init__(name, size)
		#Initialiser les informations sur les monstres
		self.game = game
		self.health = 100
		self.max_health = 100
		self.attack = 0.3
		#Récupere les coordonnées de l'image du monstre
		self.rect = self.image.get_rect()
		self.rect.x = 1000 +random.randint(0,300)
		self.rect.y = 540 - offset
		self.loot_amount =10
		self.start_animation()

	#1. Faire avancer un monstre
	def set_speed(self, speed):
		self.default_speed = speed
		self.velocity = random.randint(1, 3)

	#2. Ajouter des points au score lorsqu'un monstre meur
	def set_loot_amount(self, amount):
		self.loot_amount = amount

	#3. Infliger des dégâts au joueur lorsqu'il touche un monstre
	def damage(self, amount):
		self.health -=amount

		#Détécter si il reste de la vie au joueur
		if self.health <=0 :
			self.rect.x = 1000 + random.randint(0, 300)
			self.velocity=random.randint(1, self.default_speed)
			self.health=self.max_health
			self.game.add_score(self.loot_amount)

			#Détécter si la barre d'évenement est charger a 100 %
			if self.game.comet_event.is_full_loaded():
				#le retirer du jeux
				self.game.all_monsters.remove(self)
				self.game.comet_event.attempt_fall()

	#4. Animer un monstre
	def update_animation(self):
		self.animate(loop=True)


	#5. Générer la barre de vie
	def update_health_bar(self, surface):
		pygame.draw.rect(surface, (60,63,60), [self.rect.x+10, self.rect.y-20, self.max_health, 5])
		pygame.draw.rect(surface, (111,210,46), [self.rect.x+10, self.rect.y-20, self.health, 5])

	#6. Arrêter le joueur s'il entre en collision avec un monstre
	def forward(self):
		if not self.game.check_collision(self, self.game.all_players):
			self.rect.x -= self.velocity	
		else :
			self.game.player.damage(0.3)

#Créer une classe qui va représenter les monstres : Mummy
class Mummy(Monster):
	def __init__(self, game):
		super().__init__(game, "mummy", (130,130))
		self.set_speed(3)
		self.set_loot_amount(20)


#Créer une classe qui va représenter les monstres: Alien
class Alien(Monster):
	def __init__(self, game):
		super().__init__(game, "alien", (300,300), 130)
		self.healt = 250
		self.max_health = 250
		self.attack = 0.8
		self.set_speed(1)
		self.set_loot_amount(50)
