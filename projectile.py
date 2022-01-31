import pygame


#Créer une classe qui va représenter le prjectil du projectile
class Projectile(pygame.sprite.Sprite):
	def __init__(self, player):
		super().__init__()
		#Initialiser les informations sur les projectiles
		self.velocity = 5
		self.player = player
		self.image = pygame.image.load('assets/projectile.png')
		self.image = pygame.transform.scale(self.image,(50, 50))
		#Récupere les coordonnées de l'image du joueur
		self.rect = self.image.get_rect()
		self.rect.x = player.rect.x + 120
		self.rect.y = player.rect.y + 80
		self.origin_image = self.image
		self.angle =0

	#1. Génerer la rotation du projectile
	def rotate(self):
		self.angle += 8
		self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
		self.rect = self.image.get_rect(center =self.rect.center)

	#2. Supprimer le projectile
	def remove(self):
		self.player.all_projectiles.remove(self)

	#3. Déplacer le projectile
	def move(self):
		self.rect.x += self.velocity
		self.rotate()

		#Verifier si le projectile entre en collision avec un monstre
		for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
			self.remove()
			monster.damage(self.player.attack)

		#Détécter la sorie du projectile
		if self.rect.x > 1080 :
			self.remove

