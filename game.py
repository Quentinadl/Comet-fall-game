import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent

#Créer une classe qui vas représenter notre jeu
class Game :
	def __init__(self):
		#definir si notre jeux a commencer ou non 
		self.is_playing = False
		#generer notre joueur
		self.all_players = pygame.sprite.Group()
		self.player = Player(self)
		self.all_players.add(self.player)
		#genere l'evenement 
		self.comet_event = CometFallEvent(self)
		#groupe de monstre
		self.all_monsters = pygame.sprite.Group()
		self.pressed = {}  #touche actuellemnt activeé par le joueur


	def start(self):
		self.is_playing = True
		self.spawn_monster()
		self.spawn_monster()

	def game_over(self):
		#remettre le jeu a neuf, retirer les monstre, remettre le joueur a 100 de vie et tt 
		self.all_monsters = pygame.sprite.Group()
		self.player.health = self.player.max_health
		self.comet_event.all_comets = pygame.sprite.Group()
		self.comet_event.reset_percent()
		self.is_playing =False


	def update(self, screen):
		#Appliquer l'image du joueur
		screen.blit(self.player.image, self.player.rect)

		#actualiser la bar de vie du joureur
		self.player.update_health_bar(screen)

		#Actualiser la barre d'evenement du jeux
		self.comet_event.update_bar(screen)

		#recuperer les projectiles du joueur
		for projectile in self.player.all_projectiles :
			projectile.move()

		#recupere les monstres 
		for monster in self.all_monsters	:
			monster.forward()
			monster.update_health_bar(screen)

		#recuperrer les comets du jeux
		for comet in self.comet_event.all_comets:
			comet.fall()

		#appliquer l'enssemble des image de mon groupe de proj
		self.player.all_projectiles.draw(screen)

		#ajouter l'enssemble des image de monsters
		self.all_monsters.draw(screen)

		#appliquer l'enssemble des image de commetes
		self.comet_event.all_comets.draw(screen)

		#verifié si le joueur souhaite aller g ou d
		if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width< 1080:
			self.player.move_right()
		elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
			self.player.move_left()

	def check_collision(self, sprite, group):
		return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

	def spawn_monster(self):
		monster = Monster(self)
		self.all_monsters.add(monster)
