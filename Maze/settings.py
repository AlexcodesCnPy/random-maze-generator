from collections import deque
import pygame
from numpy import matrix



#SPECS
WIDTH = HEIGHT = 900
SCREEN = (WIDTH,HEIGHT)#WIDTH AND HEIGHT OF SCREEN
IMAGE = 'blocks.png'
RUNNING = True 
FPS = 60
CAPTION = ''

#CELL
N = 100
W = WIDTH//N + 70
H = W
R = 10
'''class cell:
	def __init__(self,color,dimension):
		self.color = color
		self.dimension = dimension

	def _Rect(self,pos):
		return (pygame.Rect(,(W,H))'''

#COLOURS
WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(204,255,0)
RED=(243,0,0)
YELLOW=(254,254,49)

#DIRECTION
NORTH = [0,-89]
EAST = [89,0]
WEST = [-89,0]
SOUTH = [0,89]
NEWS = [NORTH, EAST, WEST,SOUTH]

#STACK AND LIST
STACK = deque()
VISITED = []
V = 0
GRID = [(10 + j *(R + W) ,10 + i *(R + H))for i in range(10) for j in range(10)]# coordinates of all cells 


#print(GRID)
D = [GRID[i:i+10] for i in range(0,len(GRID),10)]
for j in range(10):
	print(D[j])

