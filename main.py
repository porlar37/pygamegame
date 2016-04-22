import pygame, time, random, map.py, items.py, sys, thread
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

#set up esantal veriabels for the player
player-x = 0
player-y = 0
waking-forword = False
waking-backword = False
waking-left = False
waking-right = False
atacking = False

#defines funcktione for rendering
def render():
	
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
	thread.start_new_thread(render())
#main loop ended quiting
pygame.quit()
sys.quit()
