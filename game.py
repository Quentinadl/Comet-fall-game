import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent
from monster import Mummy
from monster import Alien
from sounds import SoundManager


#Créer une classe qui va représenter notre jeu
class Game :
	def __init__(self):
		#Définir la situation du jeux (par defaut : pas encore commencé) 
		self.is_playing = False
		#Générer le joueur
		self.all_players = pygame.sprite.Group()
		self.player = Player(self)
		self.all_players.add(self.player)
		#Générer la pluie de commete
		self.comet_event = CometFallEvent(self)
		#Générer les monstres
		self.all_monsters = pygame.sprite.Group()
		self.font = pygame.font.SysFont("monospace", 16)
		#Générer le son
		self.sound_manager = SoundManager()
		#Générer le score (par defaut a 0)
		self.score = 0
		#Connaitre le touche activé par le joueur
		self.pressed = {}

	#1. Lancer la première phase
	def start(self):
		self.is_playing = True
		self.spawn_monster(Mummy)
		self.spawn_monster(Mummy)
		self.spawn_monster(Alien)

	#2. Ajouter les points
	def add_score(self, points=20):
		self.score += points

	#3. Actualiser l'écran
	def update(self, screen):

		#Afficher le score sur l'écran
		score_text = self.font.render(f"Score : {self.score}", 1, (0,0,0))
		screen.blit(score_text, (20,20))

		#Appliquer l'image du joueur
		screen.blit(self.player.image, self.player.rect)

		#Actualiser la barre de vie du joueur
		self.player.update_health_bar(screen)

		#Actualiser la barre d'évenement du jeux
		self.comet_event.update_bar(screen)

		#Actualiser l'animation du joueur
		self.player.update_animation()


		#Arrêter les projectiles du joueur
		for projectile in self.player.all_projectiles :
			projectile.move()

		#Arrêter les monstres 
		for monster in self.all_monsters	:
			monster.forward()
			monster.update_health_bar(screen)
			monster.update_animation()

		#Arrêter les la pluie de commetes
		for comet in self.comet_event.all_comets:
			comet.fall()

		#Appliquer l'enssemble des images du groupe de projectile
		self.player.all_projectiles.draw(screen)

		#Appliquer l'enssemble des images du groupe de monstres
		self.all_monsters.draw(screen)

		#Appliquer l'enssemble des images du groupe de commetes
		self.comet_event.all_comets.draw(screen)

		#Détécter le déplacement du joueur
		if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width< 1080:
			self.player.move_right()
		elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
			self.player.move_left()

	#4. Detecter si le joueur est en collision avec un monstre
	def check_collision(self, sprite, group):
		return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

	#5. Faire apparaitre un monstre
	def spawn_monster(self, monster_class_name):
		self.all_monsters.add(monster_class_name.__call__(self))

	#6. Detecter la perte
	def game_over(self):
		#Remettre le jeu a neuf, retirer les monstre, remettre le joueur a 100 de vie, etc ...
		self.all_monsters = pygame.sprite.Group()
		self.player.health = self.player.max_health
		self.comet_event.all_comets = pygame.sprite.Group()
		self.comet_event.reset_percent()
		self.is_playing =False
		self.score = 0
		#Jouer le son 
		self.sound_manager.play('game_over')



