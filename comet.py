import pygame
import random

#Créer une classe qui va représenter les comètes 
class Comet(pygame.sprite.Sprite):
	def __init__(self, comet_event):
		super().__init__()
		#Importer l'image des comètes
		self.image = pygame.image.load('assets/comet.png')
		#Récupere les coordonnées de l'image de la somète
		self.rect = self.image.get_rect()
		#Initialiser les informations sur les comètes
		self.velocity = random.randint(1, 3)
		self.rect.x=random.randint(20,800)
		self.rect.y = - random.randint(0, 800)
		self.comet_event = comet_event

	#1.Supprimer une comètes 
	def remove(self):
		self.comet_event.all_comets.remove(self)
		#Jouer le son
		self.comet_event.game.sound_manager.play('meteorite')

		#Verifier si le nombre de comètes  = 0
		if len(self.comet_event.all_comets) == 0 :
			self.comet_event.reset_percent()
			self.comet_event.game.start()

	#2. Lancer une comète
	def fall(self):
		self.rect.y += self.velocity

		#Detecter et le supprimer si une comète touche le sol
		if self.rect.y >= 500:
			self.remove()
			#Vérifier qu'il n'y ai plus de comètes
			if len(self.comet_event.all_comets) ==0:
				#remettre la jauge au depart
				self.comet_event.reset_percent()
				self.comet_event.fall_mode = False

		#Verifier si une comète touche le joueur
		if self.comet_event.game.check_collision(self,self.comet_event.game.all_players):
			self.remove()
			self.comet_event.game.player.damage(20)
			

