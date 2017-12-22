#!/usr/bin/env python

import pygame.event
import pygame.key
import pygame.display
import pygame.image
import pygame.mixer
import pygame
import math

def verticalanglescan(texture, surface, height, y, wgrowfactor, hgrowfactor, skipline=1, scalefactor=1, sizescale=1, antialias=0, fliponneg=1, backprop=0, fillercolor=((0, 0, 0)), colorfill=1, siderepeat=0, lpane=None, rpane=None):
	#texture=pygame.transform.scale(texture, (int(surface.get_width()*float(wgrowfactor)), height))
	wval=surface.get_width()
	backprop=backprop*float(scalefactor)
	if height<0:
		height=abs(height)
		if fliponneg==1:
			texture=pygame.transform.flip(texture, 0, 1)
		y+=backprop
		height+=backprop
		neg=1
	else:
		neg=0
		y-=backprop
		height+=backprop
	hval=y
	surfacewidth=surface.get_width()*float(sizescale)
	scalewidth=surfacewidth*float(scalefactor)
	surfaceheight=surface.get_height()
	scaleheight=height*float(scalefactor)
	scalejumpx=(surfacewidth*float(wgrowfactor))/float(height)
	scalejumpy=(height*float(hgrowfactor))/float(height)
	scalewidth -= scalejumpx*backprop
	scaleheight -= scalejumpy*backprop
	while (hval<y+height and hval<surfaceheight and neg==0) or (hval>y-height-skipline and hval>-skipline and neg==1):
		surface.set_clip(pygame.Rect(0, hval, wval, skipline))
		if colorfill==1:
			surface.fill(fillercolor)
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
		if (hval>=0 and neg==0) or (hval<=surfaceheight and neg==1):
			if neg==1:
				blitrect=texscale.get_rect()
				blitrect.x=xoffset
				blitrect.bottom=y
				surface.blit(texscale, blitrect)
				if scalewidth<surfacewidth and (siderepeat==1 or siderepeat==2):
					if lpane!=None:
						if antialias==0:
							texscalelp=pygame.transform.scale(lpane, (abs(int(scalewidth)), abs(int(scaleheight))))
						else:
							texscalelp=pygame.transform.smoothscale(lpane, (abs(int(scalewidth)), abs(int(scaleheight))))
						surface.blit(texscalelp, (xoffset-scalewidth, blitrect.y))
						
					else:
						surface.blit(texscale, (xoffset-scalewidth, blitrect.y))
					if rpane!=None:
						if antialias==0:
							texscalerp=pygame.transform.scale(rpane, (abs(int(scalewidth)), abs(int(scaleheight))))
						else:
							texscalerp=pygame.transform.smoothscale(rpane, (abs(int(scalewidth)), abs(int(scaleheight))))
						surface.blit(texscalerp, (xoffset+scalewidth, blitrect.y))
						
					else:
						surface.blit(texscale, (xoffset+scalewidth, blitrect.y))
					
					
				if scalewidth*3<surfacewidth and siderepeat==2:
					surface.blit(texscale, (xoffset+scalewidth*2, blitrect.y))
					surface.blit(texscale, (xoffset-scalewidth*2, blitrect.y))
			else:
				
				surface.blit(texscale, (xoffset, y))
				if scalewidth<surfacewidth and (siderepeat==1 or siderepeat==2):
					if lpane!=None:
						if antialias==0:
							texscalelp=pygame.transform.scale(lpane, (abs(int(scalewidth)), abs(int(scaleheight))))
						else:
							texscalelp=pygame.transform.smoothscale(lpane, (abs(int(scalewidth)), abs(int(scaleheight))))
						surface.blit(texscalelp, (xoffset-scalewidth, y))
					else:
						surface.blit(texscale, (xoffset-scalewidth, y))
					if rpane!=None:
						if antialias==0:
							texscalerp=pygame.transform.scale(rpane, (abs(int(scalewidth)), abs(int(scaleheight))))
						else:
							texscalerp=pygame.transform.smoothscale(rpane, (abs(int(scalewidth)), abs(int(scaleheight))))
						surface.blit(texscalerp, (xoffset+scalewidth, y))
					else:
						surface.blit(texscale, (xoffset+scalewidth, y))
				if scalewidth*3<surfacewidth and siderepeat==2:
					surface.blit(texscale, (xoffset+scalewidth*2, y))
					surface.blit(texscale, (xoffset-scalewidth*2, y))
		if neg==0:
			hval+=skipline
		else:
			hval-=skipline
	surface.set_clip(None)
	return pygame.Rect(0, y, surface.get_width(), height)


def horizontalanglescan(texture, surface, width, x, hgrowfactor, wgrowfactor, skipline=1, scalefactor=1, sizescale=1, antialias=0, fliponneg=1, backprop=0, fillercolor=((0, 0, 0)), colorfill=1, siderepeat=0, upane=None, dpane=None):
	#texture=pygame.transform.scale(texture, (int(surface.get_width()*float(wgrowfactor)), width))
	hval=surface.get_height()
	backprop=backprop*float(scalefactor)
	if width<0:
		width=abs(width)
		if fliponneg==1:
			texture=pygame.transform.flip(texture, 1, 0)
		x+=backprop
		width+=backprop
		neg=1
	else:
		neg=0
		x-=backprop
		width+=backprop
	wval=x
	surfaceheight=surface.get_height()*float(sizescale)
	scaleheight=surfaceheight*float(scalefactor)
	surfacewidth=surface.get_width()
	scalewidth=width*float(scalefactor)
	scalejumpy=(surfaceheight*float(wgrowfactor))/float(width)
	scalejumpx=(width*float(hgrowfactor))/float(width)
	scalewidth -= scalejumpx*backprop
	scaleheight -= scalejumpy*backprop
	while (wval<x+width and wval<surfacewidth and neg==0) or (wval>x-width-skipline and wval>-skipline and neg==1):
		surface.set_clip(pygame.Rect(wval, 0, skipline, hval))
		if colorfill==1:
			surface.fill(fillercolor)
		#print surface.get_clip()
		scalewidth += scalejumpx*skipline
		scaleheight += scalejumpy*skipline
		yoffset=int(0-((scaleheight-surfaceheight)/2))
		if (wval>=0 and neg==0) or (wval<=surfacewidth and neg==1):
			if antialias==0:
				texscale=pygame.transform.scale(texture, (abs(int(scalewidth)), abs(int(scaleheight))))
			else:
				texscale=pygame.transform.smoothscale(texture, (abs(int(scalewidth)), abs(int(scaleheight))))
			
			#print scalewidth
			#print xoffset
			if neg==1:
				blitrect=texscale.get_rect()
				blitrect.y=yoffset
				blitrect.right=x
				surface.blit(texscale, blitrect)
				if scaleheight<surfaceheight and (siderepeat==1 or siderepeat==2):
					if upane!=None:
						if antialias==0:
							texscalelp=pygame.transform.scale(upane, (abs(int(scalewidth)), abs(int(scaleheight))))
						else:
							texscalelp=pygame.transform.smoothscale(upane, (abs(int(scalewidth)), abs(int(scaleheight))))
						surface.blit(texscalelp, (blitrect.x, yoffset-scaleheight))
						
					else:
						surface.blit(texscale, (blitrect.x, yoffset-scaleheight))
					if dpane!=None:
						if antialias==0:
							texscalerp=pygame.transform.scale(dpane, (abs(int(scalewidth)), abs(int(scaleheight))))
						else:
							texscalerp=pygame.transform.smoothscale(dpane, (abs(int(scalewidth)), abs(int(scaleheight))))
						surface.blit(texscalerp, (blitrect.x, yoffset+scaleheight))
						
					else:
						surface.blit(texscale, (blitrect.x, yoffset+scaleheight))
					
					
				if scaleheight*3<surfaceheight and siderepeat==2:
					surface.blit(texscale, (blitrect.x, yoffset+scaleheight*2))
					surface.blit(texscale, (blitrect.x, yoffset-scaleheight*2))
			else:
				
				surface.blit(texscale, (x, yoffset))
				if scaleheight<surfaceheight and (siderepeat==1 or siderepeat==2):
					if upane!=None:
						if antialias==0:
							texscalelp=pygame.transform.scale(upane, (abs(int(scalewidth)), abs(int(scaleheight))))
						else:
							texscalelp=pygame.transform.smoothscale(upane, (abs(int(scalewidth)), abs(int(scaleheight))))
						surface.blit(texscalelp, (x, yoffset-scaleheight))
					else:
						surface.blit(texscale, (x, yoffset-scaleheight))
					if dpane!=None:
						if antialias==0:
							texscalerp=pygame.transform.scale(dpane, (abs(int(scalewidth)), abs(int(scaleheight))))
						else:
							texscalerp=pygame.transform.smoothscale(dpane, (abs(int(scalewidth)), abs(int(scaleheight))))
						surface.blit(texscalerp, (x, yoffset+scaleheight))
					else:
						surface.blit(texscale, (x, yoffset+scaleheight))
				if scaleheight*3<surfaceheight and siderepeat==2:
					surface.blit(texscale, (x, yoffset+scaleheight*2))
					surface.blit(texscale, (x, yoffset-scaleheight*2))
		if neg==0:
			wval+=skipline
		else:
			wval-=skipline
	surface.set_clip(None)
	return pygame.Rect(0, x, width, surface.get_height())

def rotatefeild(texture, destsurf, degrees, lpane=None, rpane=None):
	scalerotsurfrect=destsurf.get_rect()
	scaleXg=pygame.transform.rotate(texture, degrees)
	destwidth=destsurf.get_width()
	scalerect=scaleXg.get_rect()
	scalerectr=scaleXg.get_rect()
	scalerectl=scaleXg.get_rect()
	
	scalerect.centerx=scalerotsurfrect.centerx
	scalerect.centery=scalerotsurfrect.centery
	
	scalerectr=scalerect.move(-destwidth, 0)
	scalerectl=scalerect.move(destwidth, 0)
	#print scalerectl.x
	#print scalerect.x
	#print scalerectr.x
	#print scalerotsurfrect.centerx-destwidth
	destsurf.blit(scaleXg, scalerect)
	if lpane!=None:
		lpane.blit(scaleXg, scalerectl)
	if rpane!=None:
		rpane.blit(scaleXg, scalerectr)


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
		

def hspriteroto(texture, degrees, surface, growfactor=0.3, lineskip=1):
	width=surface.get_width()
	height=surface.get_height()
	growfactor=float(growfactor)
	if degrees>180:
		degrees-=180
		texture=pygame.transform.flip(texture, 1, 0)
	if degrees>90:
		degrees-=90
		inverteffect=1
		widthval=int((width/float(90))*abs(degrees-90))
		texture=pygame.transform.flip(texture, 1, 0)
		scaleval=(growfactor/90)*degrees
	else:
		inverteffect=0
		widthval=int((width/float(90))*degrees)
		scaleval=(growfactor/90)*abs(degrees-90)
	if widthval==0:
		widthval=1
	if inverteffect==1:
		horizontalanglescan(texture, surface, 1, width//2+widthval//2, scaleval, scaleval, colorfill=0, backprop=widthval, skipline=lineskip)
	else:
		horizontalanglescan(texture, surface, -1, width//2-widthval//2, scaleval, scaleval, colorfill=0, backprop=widthval, skipline=lineskip)
	return surface

def vspriteroto(texture, degrees, surface, growfactor=0.3, lineskip=1):
	height=surface.get_height()
	width=surface.get_width()
	growfactor=float(growfactor)
	if degrees>180:
		degrees-=180
		texture=pygame.transform.flip(texture, 0, 1)
	if degrees>90:
		degrees-=90
		inverteffect=1
		heightval=int((height/float(90))*abs(degrees-90))
		texture=pygame.transform.flip(texture, 0, 1)
		scaleval=(growfactor/90)*degrees
	else:
		inverteffect=0
		heightval=int((height/float(90))*degrees)
		scaleval=(growfactor/90)*abs(degrees-90)
	if heightval==0:
		heightval=1
	if inverteffect==1:
		verticalanglescan(texture, surface, 1, height//2+heightval//2, scaleval, scaleval, colorfill=0, backprop=heightval, skipline=lineskip)
	else:
		verticalanglescan(texture, surface, -1, height//2-heightval//2, scaleval, scaleval, colorfill=0, backprop=heightval, skipline=lineskip)
	return surface




