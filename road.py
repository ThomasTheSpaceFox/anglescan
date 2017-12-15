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


scaleXA=pygame.image.load("road.png")
scaleXB=pygame.image.load("scale2.png")
scaleX=scaleXA
polar=1
bg=pygame.image.load("bg.png")


pygame.display.init()
screensurf=pygame.display.set_mode((800, 600))
scalesurf=pygame.Surface((200, 150))
screensurf.blit(bg, (0, 0))

pygame.display.update()

ypos=75
yposdef=ypos
yposjump=95
jump=0
engtimer=pygame.time.Clock()
while True:
	scalesurf.fill((185, 218, 226))
	rectx=anglescan.verticalanglescan(scaleX, scalesurf, int(ypos), int(ypos), 1.5, 0.6, 2, 1, 1, 0)
	screensurf.blit(pygame.transform.scale(scalesurf, (800, 600)), (0, 0))
	rectx.w *= 4
	rectx.h *= 4
	rectx.x *= 4
	rectx.y *= 4
	pygame.display.update()
	pygame.event.pump()
	key=pygame.key.get_pressed()
	if key[pygame.K_ESCAPE]:
		sys.exit()
	if key[pygame.K_SPACE]:
		jump=1
	if jump==1:
		print "up"+ str(ypos)
		ypos+=4
		if ypos>=yposjump+4:
			ypos=yposjump
			jump=2
	elif jump==2:
		ypos-=4
		if ypos<=yposdef:
			jump=0
		
	if key[pygame.K_LEFT]:
		scaleX=anglescan.hscroll(3, scaleX)
	elif key[pygame.K_RIGHT]:
		scaleX=anglescan.hscroll(-3, scaleX)
	else:
		scaleX=anglescan.hscroll(-1, scaleX)
	if key[pygame.K_UP]:
		scaleX=anglescan.vscroll(5, scaleX)
	elif key[pygame.K_DOWN]:
		scaleX=anglescan.vscroll(-5, scaleX)
	#print time.time()
	engtimer.tick(30)
	print engtimer.get_fps()
	