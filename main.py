import pygame, time, random, map.py, items.py, sys 
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

#set up the window
WINDOWWIDTH = 1920
WINDOWHEIGHT = 1080
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('pygamegame')

#set up veriabels for the gameloop
pused = False
exiting = False
runing = True

#run the game loop
while runing == True:
	#check for pygame events
	for event in pygame.event.get():
		#check for the QUIT event
		if event.type == QUIT:
			if event.type == QUIT:
				runing = False
		#check for the KEYDOWN event
		if event.type == KEYDOWN:
		#check for the KEYUP event
		if event.type == KEYUP:
#main loop ended quiting
pygame.quit()
sys.quit()
