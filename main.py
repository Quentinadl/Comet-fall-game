import pygame 
import math
from game import Game

pygame.init()

#Generer la fenetre de notre jeux
pygame.display.set_caption("Comet fall game")   #titre et icone de la fenettre
screen = pygame.display.set_mode((1080,720))

#Importer l'image d'arrière plan
background = pygame.image.load('assets/bg.jpg')

#Importation de la bannière
banner = pygame.image.load('assets/banner.png')
banner =pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() /4)

#importer et charger le boutton play
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)

#charger notre jeux
game = Game()

#contient si la fenetre est en cours d'execution
running =True      


#Boucle du jeux
while running:       

	#Appliquer l'arrier plan du jeux , L, H
	screen.blit(background, (0, -200))

	#Verifier si le jeux a commencer
	if game.is_playing:
		#declencher les instruction de la parti 
		game.update(screen)
	else :
		#ajouter mon ecran de bienvenur
		screen.blit(play_button, play_button_rect)
		screen.blit(banner, banner_rect)
		
	#Verifier si 

	#Mettre a jour l'écran
	pygame.display.flip()

	#Veerifier si le joueur feme la fenetre
	for event in pygame.event.get():
		#Vérifier que
		if event.type == (pygame.QUIT or game.pressed.get(pygame.K_Echap)) :
			running =False 
			pygame.quit()
			print("Fermeture du jeux ")

		#deteecter si un jeoueur lache une touche du clavier
		elif event.type == pygame.KEYDOWN :
			game.pressed[event.key] = True

			#detecter si la touche espace est enclencher pourlancer le proj
			if event.key == pygame.K_SPACE :
				game.player.launch_projectile()

		elif event.type == pygame.KEYUP :
			game.pressed[event.key] = False

		elif event.type == pygame.MOUSEBUTTONDOWN:
			#vérifier si la sourie est en collision avec le bouton
			if play_button_rect.collidepoint(event.pos):
				game.start()

