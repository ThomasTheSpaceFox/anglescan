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


scaleXA=pygame.image.load("square.png")
scaleXROT=pygame.image.load("square.png")
scaleXB=pygame.image.load("scale2.png")
scaleX=scaleXA
polar=1
bg=pygame.image.load("bg.png")

pygame.display.init()
pygame.display.set_caption("test 8: 1 vertical scaled floor, 2 vertical scaled walls.","test 8: 1 vertical scaled floor, 2 vertical scaled walls.")

screensurf=pygame.display.set_mode((800, 600))
scalesurf=pygame.Surface((150, 150), flags=pygame.SRCALPHA)
screensurf.blit(bg, (0, 0))

pygame.display.update()



engtimer=pygame.time.Clock()
while True:
	#scalesurf.blit(scaleX, (0, -75))
	rectx=anglescan.verticalanglescan(scaleXROT, scalesurf, 70, 125, 1.0, 1.0, 2, 1, 1, 0, backprop=25, siderepeat=1)
	rectx=anglescan.horizontalanglescan(scaleX, scalesurf, 35, 165, 1.3, 1.3, 1, 1, 1, 0, backprop=38, siderepeat=0, colorfill=0)
	rectx=anglescan.horizontalanglescan(scaleX, scalesurf, -35, -20, 1.3, 1.3, 1, 1, 1, 0, backprop=38, siderepeat=0, colorfill=0)
	#rectx=anglescan.horizontalanglescan(scaleX, scalesurf, 30, 125, 1.0, 1.0, 1, 1, 1, 0, backprop=45, siderepeat=0, colorfill=0)
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
	if key[pygame.K_UP]:
		scaleX=anglescan.hscroll(-7, scaleX)
		scaleXROT=anglescan.vscroll(-5, scaleXROT)
	elif key[pygame.K_DOWN]:
		scaleX=anglescan.hscroll(7, scaleX)
		scaleXROT=anglescan.vscroll(5, scaleXROT)
	else:
		scaleX=anglescan.hscroll(-3, scaleX)
		scaleXROT=anglescan.vscroll(-2, scaleXROT)
	#print time.time()
	engtimer.tick(30)
	print engtimer.get_fps()
	