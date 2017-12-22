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
pygame.display.set_caption("test 9: 3D-style rotation demo. (vspriteroto & hspriteroto)", "test 9: 3D-style rotation demo. (vspriteroto & hspriteroto)")
screensurf=pygame.display.set_mode((800, 600))
scalesurf=pygame.Surface((50, 50)).convert()
scalesurf2=pygame.Surface((50, 50)).convert()

scaleXA=pygame.image.load("square.png").convert()
scaleXB=pygame.image.load("scale2.png").convert()
scaleX=scaleXA
polar=1
bg=pygame.image.load("bg.png").convert()
screensurf.blit(bg, (0, 0))

pygame.display.update()


degrees=0
engtimer=pygame.time.Clock()
while True:
	#scalesurf.blit(scaleX, (0, -75))
	scalesurf.fill((0, 0, 0))
	scalesurf2.fill((0, 0, 0))
	#rectx=anglescan.verticalanglescan(scaleX, scalesurf, 75, 75, 1.5, 0.6, 2, 1, 1, 0)
	anglescan.hspriteroto(scaleX, degrees, scalesurf, 0.5)
	anglescan.vspriteroto(scaleX, degrees, scalesurf2, 0.5)
	screensurf.blit(pygame.transform.scale(scalesurf, (400, 400)), (0, 0))
	screensurf.blit(pygame.transform.scale(scalesurf2, (400, 400)), (400, 0))
	#rectx.w *= 4
	#rectx.h *= 4
	#rectx.x *= 4
	#rectx.y *= 4
	
	pygame.display.update()
	pygame.event.pump()
	key=pygame.key.get_pressed()
	if key[pygame.K_ESCAPE]:
		sys.exit()
	if key[pygame.K_LEFT]:
		scaleX=anglescan.hscroll(3, scaleX)
	elif key[pygame.K_RIGHT]:
		scaleX=anglescan.hscroll(-3, scaleX)
	else:
		scaleX=anglescan.hscroll(1, scaleX)
	if key[pygame.K_UP]:
		scaleX=anglescan.vscroll(5, scaleX)
	elif key[pygame.K_DOWN]:
		scaleX=anglescan.vscroll(-5, scaleX)
	else:
		scaleX=anglescan.vscroll(1, scaleX)
	if key[pygame.K_PAGEUP]:
		degrees-=5
	elif key[pygame.K_PAGEDOWN]:
		degrees+=5
	else:
		degrees+=1
	if degrees>=360:
		degrees=0
	if degrees<0:
		degrees=355
	#print time.time()
	engtimer.tick(60)
	#print engtimer.get_fps()
	