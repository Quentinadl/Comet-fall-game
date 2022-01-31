import pygame
import random

#Créer une classe qui va représenter les mecanique d'animation 
class AnimateSprite(pygame.sprite.Sprite):
	def __init__(self, sprite_name, size = (200,200)):
		super().__init__()
		self.size = size
		self.image = pygame.image.load(f'assets/{sprite_name}.png')
		self.image = pygame.transform.scale (self.image, size)
		self.current_image =0
		self.images =animations.get(sprite_name)
		self.animation = False

	#1. Démarer l'animation
	def start_animation(self):
		self.animation =True

	#2. Animer le Sprite
	def animate(self, loop=False):
		#Vérifier si l'animation est activé pour l'entité
		if self.animation:
			self.current_image+= random.randint(0,1)
			#Relancer l'animation si elle est terminé
			if self.current_image >= len(self.images):
				self.current_image =0
				if loop is False :
					self.animation =False

			self.image = self.images[self.current_image]
			self.image = pygame.transform.scale (self.image, self.size)

#Charger les 24 images des dossiers correspondant 
def load_animation_images(sprite_name):
	images=[]
	#Recuperer le chemin du dossier pour le Sprite
	path = f"assets/{sprite_name}/{sprite_name}"
	#Boucler sur chaque image du dossier
	for num in range (1,24):
		image_path = path + str(num) + '.png'
		images.append(pygame.image.load(image_path))
	return images


#Definir un dictionnaire qui va contenir les images charger de chaque Sprite
animations ={
	'mummy' : load_animation_images('mummy'),
	'player': load_animation_images('player'),
	'alien': load_animation_images('alien')
}
