import pygame
from settings import *
import maze

rect = pygame.Rect(0, 0, 90, 90)
pygame.init()
pygame.display.set_caption('maze')
screen = pygame.display.set_mode(SCREEN)
image = pygame.image.load(IMAGE)

def play():
	global RUNNING,VISITED,WHITE,BLUE
	while RUNNING:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				RUNNING = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_g:
					maze.GENERATE((10,10) , screen)


		for x,y in GRID:
			if (x,y) in VISITED:
				maze.draw((x,y), screen, WHITE)

			#GREEN
			#YELLOW

			else:
				maze.draw((x,y), screen, BLUE)

		pygame.display.update()

	pygame.quit()