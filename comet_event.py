import pygame
from comet import Comet

#Créer une classe qui va représenter la pluie de comète
class CometFallEvent :
	def __init__(self, game):
		self.percent = 0
		self.percent_speed = 10
		self.game =game
		self.fall_mode = False
		#Définir un groupe de Sprite pour stoker les comètes
		self.all_comets = pygame.sprite.Group()

	#1. Appliquer la formule de pourcentage
	def add_percent(self):
		self.percent += self.percent_speed /100

	#2. Détécter lorsque la barre d'événement est pleine
	def is_full_loaded(self):
		return self.percent >= 100

	#3. Réinitialiser la barre d'événement 
	def reset_percent(self):
		self.percent =0

	#4. Faire apparaître les comètes
	def meteor_fall(self):
		for i in range (1,10) :
			self.all_comets.add(Comet(self))

	#5. Activer la pluie de comètes
	def attempt_fall(self):
		if self.is_full_loaded() and len(self.game.all_monsters) == 0:
			self.meteor_fall()
			self.fall_mode = True

	#6. Ajouter du pourcentage a la barre d'événement
	def update_bar (self, surface):
		self.add_percent()
		#Générer la barre noir
		pygame.draw.rect(surface, (0,0,0), [
			0,                                            #Axe des abscisse
			surface.get_height()-20,                      #Axe des ordonné
			surface.get_width(),                          #Longeur de la fenêtre
			10,                                           #Eppaisseur
		])
		#Générer la barre verte
		pygame.draw.rect(surface, (187,11,11), [
			0,                                            #Axe des abscisse
			surface.get_height()-20,                      #Axe des ordonné
			(surface.get_width() / 100)* self.percent,    #Longeur de la fenêtre
			10,                                           #Eppaisseur
		])