#!/usr/bin/env python

import pygame.event
import pygame.key
import pygame.display
import pygame.image
import pygame.mixer
import pygame
import math

def verticalanglescan(texture, surface, height, y, wgrowfactor, hgrowfactor, skipline=1, scalefactor=1, sizescale=1, antialias=0, fliponneg=1):
	#texture=pygame.transform.scale(texture, (int(surface.get_width()*float(wgrowfactor)), height))
	wval=surface.get_width()
	hval=y
	if height<0:
		height=abs(height)
		if fliponneg==1:
			texture=pygame.transform.flip(texture, 0, 1)
		neg=1
	else:
		neg=0
	surfacewidth=surface.get_width()*float(sizescale)
	scalewidth=surfacewidth*float(scalefactor)
	surfaceheight=surface.get_height()
	scaleheight=height*float(scalefactor)
	scalejumpx=(surfacewidth*float(wgrowfactor))/float(height)
	scalejumpy=(height*float(hgrowfactor))/float(height)
	while (hval<y+height and hval<surfaceheight and neg==0) or (hval>y-height-skipline and hval>-skipline and neg==1):
		surface.set_clip(pygame.Rect(0, hval, wval, skipline))
		#print surface.get_clip()
		scalewidth += scalejumpx*skipline
		scaleheight += scalejumpy*skipline
		xoffset=int(0-((scalewidth-surfacewidth)/2))
		if antialias==0:
			texscale=pygame.transform.scale(texture, (abs(int(scalewidth)), abs(int(scaleheight))))
		else:
			texscale=pygame.transform.smoothscale(texture, (abs(int(scalewidth)), abs(int(scaleheight))))
		#print scalewidth
		#print xoffset
		if neg==1:
			blitrect=texscale.get_rect()
			blitrect.x=xoffset
			blitrect.bottom=y
			surface.blit(texscale, blitrect)
		else:
			
			surface.blit(texscale, (xoffset, y))
		if scalewidth<surfacewidth:
			surface.blit(texscale, (xoffset+scalewidth, y))
			surface.blit(texscale, (xoffset-scalewidth, y))
		if neg==0:
			hval+=skipline
		else:
			hval-=skipline
	surface.set_clip(None)
	return pygame.Rect(0, y, surface.get_width(), height)


def rotatefeild(texture, destsurf, degrees):
	scalerotsurfrect=destsurf.get_rect()
	scaleXg=pygame.transform.rotate(texture, degrees)
	scalerect=scaleXg.get_rect()
	scalerect.centerx=scalerotsurfrect.centerx
	scalerect.centery=scalerotsurfrect.centery
	destsurf.blit(scaleXg, scalerect)


def hscroll(scrollval, image):
	offs=image.get_width()
	newimage=image.copy()
	newimage.fill((0, 0, 0, 0))
	newimage.blit(image, (scrollval, 0))
	if (str(scrollval))[0]=="-":
		newimage.blit(image, ((scrollval + offs), 0))
	else:
		newimage.blit(image, ((scrollval - offs), 0))
	return newimage


def vscroll(scrollval, image):
	offs=image.get_height()
	newimage=image.copy()
	newimage.fill((0, 0, 0, 0))
	newimage.blit(image, (0, scrollval))
	if (str(scrollval))[0]=="-":
		newimage.blit(image, (0, (scrollval + offs)))
	else:
		newimage.blit(image, (0, (scrollval - offs)))
	return newimage


def rotatedirection(degrees, offset, directionoffset=90):
    x = math.cos(math.radians(degrees+directionoffset)) * offset
    y = math.sin(math.radians(degrees+directionoffset)) * offset
    return [x, y]
   

def rotoscroll(surface, degrees, offset):
	rottoup=rotatedirection(degrees, offset)
	if rottoup[0]!=0:
		surface=hscroll(int(rottoup[0]), surface)
	if rottoup[1]!=0:
		surface=vscroll(int(rottoup[1]), surface)
	return surface
		
	