#!/usr/bin/env python

import pygame.event
import pygame.key
import pygame.display
import pygame.image
import pygame.mixer
import pygame
import anglescan
import time
import sys

pygame.display.init()
pygame.display.set_caption("test 7, dual scaling, view shift(left/right) (horizontal function)", "test 7, dual scaling, view shift(left/right) (horizontal function)")
screensurf=pygame.display.set_mode((800, 600))
scaleXA=pygame.image.load("scale.png").convert()
scaleXB=pygame.image.load("scale2.png").convert()
fogx=pygame.image.load("skylinefog.png").convert_alpha()
scaleX=scaleXA
polar=1
bg=pygame.image.load("bg.png").convert()

fogx=pygame.transform.scale(fogx, (50, 400))

scalesurf=pygame.Surface((50, 400)).convert()
screensurf.blit(bg, (0, 0))

pygame.display.update()

viewskew=0
scalesurf.blit(bg, (0, -75))
engtimer=pygame.time.Clock()
while True:
	#scalesurf.blit(scaleX, (0, -75))
	
	#arguments in order: texture, blit surface, effect height (use negative values to flip projection), effect y position,
	# width scale, height scale, rescale skip (numbers greater than 1 are faster but are increasingly distorted.),
	# scale factor of horizon (height and surface width are multiplied by this to create starting width and height),
	# antialiasing (slower) [bool]
	# flip texture on negative height [bool]
	#scalesurf.fill((172, 221, 225))
	
	#note: terms are slightly different for horizontal version. most notably, the width and height scaling values are reversed in argument order, and sevral argument names are different.
	rectx=anglescan.horizontalanglescan(scaleX, scalesurf, (50-viewskew)//3, (120+viewskew)//3, 1.0, 1.0, 1, 1, 1, 0, backprop=25//3, siderepeat=1)
	rectx=anglescan.horizontalanglescan(scaleX, scalesurf, -(50+viewskew)//3, (30+viewskew)//3, 1.0, 1.0, 1, 1, 1, 0, 1, colorfill=0, backprop=25//3, siderepeat=1)
	#screensurf.blit(pygame.transform.scale(scalesurf, (800, 600)), (0, 0))
	scalesurf.blit(fogx, ((0+viewskew)//3, 0))
	
	pygame.transform.scale(scalesurf, (800, 600), screensurf)
	pygame.display.update()
	pygame.event.pump()
	key=pygame.key.get_pressed()
	if key[pygame.K_ESCAPE]:
		sys.exit()
	if key[pygame.K_PAGEUP]:
		scaleX=anglescan.hscroll(12, scaleX)
	elif key[pygame.K_PAGEDOWN]:
		scaleX=anglescan.hscroll(-12, scaleX)
	else:
		scaleX=anglescan.hscroll(6, scaleX)
	if key[pygame.K_UP]:
		scaleX=anglescan.vscroll(10, scaleX)
	elif key[pygame.K_DOWN]:
		scaleX=anglescan.vscroll(-10, scaleX)
	if key[pygame.K_LEFT]:
		viewskew+=4
	elif key[pygame.K_RIGHT]:
		viewskew-=4
	#print time.time()
	engtimer.tick(30)
	print engtimer.get_fps()
	