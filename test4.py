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



polar=1



pygame.display.init()
screensurf=pygame.display.set_mode((800, 600))
scaleXA=pygame.image.load("scale3.png").convert()
scaleXB=pygame.image.load("scale2.png").convert()
bg=pygame.image.load("bg.png").convert()
scaleX=scaleXA

scalesurf=pygame.Surface((200, 75)).convert()
scalerotsurf=pygame.Surface((200, 150)).convert()
lpane=pygame.Surface((200, 150)).convert()
rpane=pygame.Surface((200, 150)).convert()

screensurf.blit(bg, (0, 0))

pygame.display.update()



engtimer=pygame.time.Clock()
rotdeg=0
scalesurf.blit(bg, (0, -75))
wscale=0.8
hscale=0.8
wscale=2.1
hscale=2.1
wscale=1.28
hscale=1.28
originscale=1.0
while True:
	#the texture, (scaleXA) should be larger enough than the destination surface (scalerotsurf), so that no edges are visible. 
	#this will vary with verticalanglescan arguments.
	#lpane and rpane, if defined, will have the left and right sides of the main surface blitted to them, so that when passed
	#to verticalanglescan as lpane and rpane (and siderepeat=1 or 2), they will be scaled and blitted as needed.
	anglescan.rotatefeild(scaleXA, scalerotsurf, rotdeg, lpane, rpane)
	scaleX=scalerotsurf
	
	
	key=pygame.key.get_pressed()
	if key[pygame.K_ESCAPE]:
		sys.exit()
	if key[pygame.K_SPACE]:
		#scaleXA=anglescan.vscroll(5, scaleXA)
		scaleXA=anglescan.rotoscroll(scaleXA, rotdeg, 10)
	#scaleXA=anglescan.rotoscroll(scaleXA, rotdeg, 5)
	#scalesurf.blit(bg, (0, -75))
	#arguments in order: texture, blit surface, effect height, effect y position,
	# width scale, height scale, rescale skip (numbers greater than 1 are faster but are increasingly distorted.),
	# scale factor of horizon (height and surface width are multiplied by this to create starting width and height)
	rectx=anglescan.verticalanglescan(scaleX, scalesurf, 60//2, 90//2, wscale, hscale, 1, originscale, 1, 0, backprop=20, lpane=lpane, rpane=rpane, siderepeat=1)
	screensurf.blit(pygame.transform.scale(scalesurf, (800, 600)), (0, 0))
	rectx.w *= 4
	rectx.h *= 8
	rectx.x *= 4
	rectx.y *= 8
	pygame.display.update(rectx)
	pygame.event.pump()
	
	if key[pygame.K_LEFT]:
		#scaleXA=hscroll(7, scaleXA)
		rotdeg-=4
	elif key[pygame.K_RIGHT]:
		#scaleXA=hscroll(-7, scaleXA)
		rotdeg+=4
	#else:
	#	rotdeg-=2
	if key[pygame.K_UP]:
		wscale+=0.01
		hscale+=0.01
		print wscale
	elif key[pygame.K_DOWN]:
		wscale-=0.01
		hscale-=0.01
		print wscale
	if key[pygame.K_PAGEUP]:
		originscale += 0.01
		print originscale
	elif key[pygame.K_PAGEDOWN]:
		originscale -= 0.01
		print originscale
	#print time.time()
	engtimer.tick(30)
	print engtimer.get_fps()
	