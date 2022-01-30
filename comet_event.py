import pygame
from comet import Comet

#créer une classe pour gérer cet evenement
class CometFallEvent :

	#Lors du chargement -> créer un compteur
	def __init__(self, game):
		self.percent = 0
		self.percent_speed = 10
		self.game =game
		self.fall_mode = False


		#definir un groupe de Sprite pour stoker les cometes
		self.all_comets = pygame.sprite.Group()


	def add_percent(self):
		self.percent += self.percent_speed /100

	def is_full_loaded(self):
		return self.percent >= 100

	def reset_percent(self):
		self.percent =0

	def meteor_fall(self):
		for i in range (1,10) :
			#apparaitre une boulle de feux
			self.all_comets.add(Comet(self))

	def attempt_fall(self):
		#Si la jaud d'avancement est totalement chargé
		if self.is_full_loaded() and len(self.game.all_monsters) == 0:
			self.meteor_fall()
			self.fall_mode = True


	def update_bar (self, surface):

		#ajouter du pourcentage a la bar
		self.add_percent()


		#barre noir
		pygame.draw.rect(surface, (0,0,0), [
			0,#axe des x
			surface.get_height()-20, #l'axe des y
			surface.get_width(), #longeur de la fenetre
			10, #eppaisseur
		])
		#barre rouge
		pygame.draw.rect(surface, (187,11,11), [
			0,#axe des x
			surface.get_height()-20, #l'axe des y
			(surface.get_width() / 100)* self.percent, #longeur de la fenetre
			10, #eppaisseur
		])