import pygame 
import math
from game import Game


#Definir une clock (élément qui nous permet de modifier les frames)
clock = pygame.time.Clock()
FPS = 60



pygame.init()

#1. Generer la fenetre du jeux
#titre et taille de la fenetre
pygame.display.set_caption("Comet fall game")   
screen = pygame.display.set_mode((1080,720))

#Importer l'image d'arrière plan
background = pygame.image.load('assets/bg.jpg')

#Importation de la bannière d'entrée dans le jeux
banner = pygame.image.load('assets/banner.png')
banner =pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() /4)

#Créer le boutton play
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)

#charger le jeux
game = Game()

#Activation par defaut du mode "runing" afin que le jeux s'exécute
running =True      



#2 Boucle du jeux
while running:       

	#Appliquer l'arrier plan du jeux , L, H
	screen.blit(background, (0, -200))

	#Verifier si le jeux a commencer
	if game.is_playing:
		#Appliquer les mise a jour du lancement du jeux 
		game.update(screen)
	else :
		#Appliquer la bannière
		screen.blit(play_button, play_button_rect)
		screen.blit(banner, banner_rect)

	#Mettre a jour l'écran
	pygame.display.flip()

	#Le joueur souhaite quitter le jeux
	for event in pygame.event.get():
		#Vérifier que le joueux quitte la fenetre
		if (event.type == pygame.QUIT) or (event.type == pygame.K_ESCAPE) :
			running =False 
			pygame.quit()
			print("Fermeture du jeux ")

		#Detecter que le joueur enclenche une touche du clavier
		elif event.type == pygame.KEYDOWN :
			game.pressed[event.key] = True

			#Detecter que la touche ESPACE soit enclencher pour lancer le projectile
			if event.key == pygame.K_SPACE :
				if game.is_playing:
					game.player.launch_projectile()
				else :
					game.start()
					#Jouer le son
					game.sound_manager.play('click')

		elif event.type == pygame.KEYUP :
			game.pressed[event.key] = False

		elif event.type == pygame.MOUSEBUTTONDOWN:
			#Detecter que la sourie soit au niveaux de l'image 'bouton play'
			if play_button_rect.collidepoint(event.pos):
				#Lancer le jeux
				game.start()
				#Jouer le son
				game.sound_manager.play('click')

	#Fixer le nombre de FPS sur la clock
	clock.tick(FPS)

