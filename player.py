import pygame
from projectile import Projectile
import animation

#Créer une classe qui va représenter notre joueur
class Player(animation.AnimateSprite):              
	def __init__(self, game):
		super().__init__('player')
		#Initialiser les informations sur le joueur
		self.game = game
		self.health = 100
		self.max_health = 100
		self.attack = 10
		self.velocity = 5
		#Définir un groupe de Sprite pour stoker les comètes
		self.all_projectiles= pygame.sprite.Group()
		#Récupere les coordonnées de l'image du joueur
		self.rect = self.image.get_rect()
		self.rect.x =400
		self.rect.y = 500

	#1. Mettre a jour la barre de vie du joueur
	def damage(self, amount):
		if self.health - amount > amount :
			self.health-= amount
		else : 
			self.game.game_over()

	#2. Animer le joueur
	def update_animation(self):
		self.animate()

	#3. Générer la barre de vie du joueur
	def update_health_bar(self, surface):
		#dessiner notre barre de vie
		pygame.draw.rect(surface, (60,63,60), [self.rect.x+50, self.rect.y + 20, self.max_health, 7])
		pygame.draw.rect(surface, (111,210,46), [self.rect.x+50, self.rect.y +20, self.health, 7])

	#4. Animer le joueur lors de la lancer s'un projectile
	def launch_projectile(self):
		self.all_projectiles.add(Projectile(self))
		self.start_animation()
		#Jouer le son
		self.game.sound_manager.play('tir')

	#5. Déplacer le joueur s'il n'est pas en collision avec un monster
	def move_right(self):
		if not self.game.check_collision(self, self.game.all_monsters):
			self.rect.x += self.velocity
			
	#6. Déplacer le joueur
	def move_left(self):
		self.rect.x -= self.velocity
