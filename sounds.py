import pygame

#Créer une classe qui va représenter les sons
class SoundManager :
	def __init__(self):
		self.sounds = {
			'click' : pygame.mixer.Sound("assets/sounds/click.ogg"),
			'game_over': pygame.mixer.Sound('assets/sounds/game_over.ogg'),
			'meteorite': pygame.mixer.Sound('assets/sounds/meteorite.ogg'),
			'tir': pygame.mixer.Sound('assets/sounds/tir.ogg')
		}
		
	#1. Jouer le son
	def play(self, name):
		self.sounds[name].play()