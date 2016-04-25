import pygame, time, random, sys, thread
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
playerx = 0
playery = 0
wakingforword = False
wakingbackword = False
wakingleft = False
wakingright = False
atacking = False

#defines funcktione for rendering
def render():
	#(not done yet)Redys the displaybufer for update	

	#updates the display
	pygame.display.update()
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
			#do "" if "" key is prest
			if event.key == ord("w"):
				wakingforword = True
			if event.key == ord("s"):
				wakingbackword = True
			if event.key == ord("a"): 
				wakingleft = True
			if event.key == ord("d"):
				wakingright = True
		#check for the KEYUP event
		if event.type == KEYUP:
			#do "" if "" key is stopt being prest
			if event.key == ord("w"):
				wakingforword = False
			if event.key == ord("s"):
				wakingbackword = False
			if event.key == ord("a"):
				wakingleft = False
			if event.key == ord("d"):
				wakingright = False

	#change position variabels
	if wakingforword == True:
		playerx = playerx + 1
	if wakingbackword == True:
		playerx = playerx - 1
	if wakingleft == True:
		playery = playery - 1
	if wakingright == True:
		platery = playery + 1

	#renders the imge
	thread.start_new_thread(render(), )

#main loop ended quiting
pygame.quit()
sys.quit()
