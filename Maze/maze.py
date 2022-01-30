#IMPORTS
import pygame
from settings import *
import random as r

#CLASSES AND FUNCTIONS

#THIS FUNCTION DRAWS BLOCK/CELL ON SCREEN
def draw(pos,screen,color):
	rect = pygame.Rect(pos,(W,H))
	pygame.draw.rect(screen,color,rect)

#THIS IS A FUNCTION THAT FINDS THE AVALIABLE NEIGHBORS NEAR CURRENT CELL
def NEIGHBORS(pos):
	n = []
	for news in NEWS:
		k = list(pos)
		for d in range(2):
			k[d] += news[d]

		if tuple(k) in GRID and tuple(k) not in VISITED:
			n.append(tuple(k))

	return n

def remove(pos1 , pos2, screen):
	#finding midpoint
	p = list(pos1)
	k = list(pos2)
	midpoint = tuple([ (p[n] + k[n])//2 for n in range(2)])

	#placing block inbetween 
	draw(midpoint,screen,WHITE)

	

def GENERATE(cur, screen):
	STACK.append(cur)
	VISITED.append(cur)
	while STACK != deque():
		pos = STACK.pop()
		n = NEIGHBORS(pos)
		if n != []:
			new = r.choice(n)
			STACK.append(pos)
			STACK.append(new)
			remove(pos,new,screen)
			VISITED.append(new)





#GENERATE((10,10))

#remove(list((10,10)),list((99,10)))




