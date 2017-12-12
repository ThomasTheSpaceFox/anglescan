#!/usr/bin/env python

import pygame.event
import pygame.key
import pygame.display
import pygame.image
import pygame.mixer
import pygame
import anglescan
import time




polar=1
bg=pygame.image.load("bg.png")


pygame.display.init()
screensurf=pygame.display.set_mode((800, 600))
scalesurf=pygame.Surface((200, 150)).convert()
screensurf.blit(bg, (0, 0))

scaleXA=pygame.image.load("scale.png").convert()
scaleXB=pygame.image.load("scale2.png").convert()
scaleX=scaleXA
shadow=pygame.image.load("shadowdepth1.png").convert_alpha()
pygame.display.update()



engtimer=pygame.time.Clock()
while True:
	scalesurf.blit(scaleX, (0, -75))
	rectx=anglescan.verticalanglescan(scaleX, scalesurf, 75, 75, 1.5, 0.6, 2, 1, 1, 0)
	screensurf.blit(pygame.transform.scale(scalesurf, (800, 600)), (0, 0))
	screensurf.blit(shadow, (0, 0))
	pygame.display.update()
	pygame.event.pump()
	key=pygame.key.get_pressed()
	if key[pygame.K_LEFT]:
		scaleX=anglescan.hscroll(7, scaleX)
	elif key[pygame.K_RIGHT]:
		scaleX=anglescan.hscroll(-7, scaleX)
	else:
		scaleX=anglescan.hscroll(-1, scaleX)
	if key[pygame.K_UP]:
		scaleX=anglescan.vscroll(7, scaleX)
	elif key[pygame.K_DOWN]:
		scaleX=anglescan.vscroll(-7, scaleX)
	#else:
	#	scaleX=vscroll(-1, scaleX)
	
	#print time.time()
	engtimer.tick(30)
	print engtimer.get_fps()
	