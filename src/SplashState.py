#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	SplashState.py
#	This Class handles the SplashScreens
#
#----------------------------------

import os
import pygame

class SplashState():
	def __init__(self):
		self.SplashScreens = [ ('dkapps.jpg',(255,255,255)) ]
		self.CurrentSplash = 0
		self.CurrentSplashFrame = 0
		self.CurrentSplashAlpha = 0
		self.StateQuit = False
		
	def ExecuteStateLogic(self,KeysHeld,KeysPressed):
		if pygame.K_ESCAPE in KeysPressed:
			self.StateQuit = True
			
		if self.CurrentSplash >= len(self.SplashScreens):
			self.StateQuit = True
			
		self.CurrentSplashFrame += 1
		if self.CurrentSplashFrame > 150 and self.CurrentSplashFrame < 405:
			self.CurrentSplashAlpha += 1
		if self.CurrentSplashFrame > 645 and self.CurrentSplashFrame < 900:
			self.CurrentSplashAlpha -= 1
		if self.CurrentSplashFrame > 900:
			self.StateQuit = True
			
	def DrawStateFrame(self,screen):
		screen.fill(self.SplashScreens[self.CurrentSplash][1])
		SplashImage = pygame.image.load(os.path.join(os.path.join('data','textures'),self.SplashScreens[self.CurrentSplash][0]))
		SplashImage.set_alpha(self.CurrentSplashAlpha)
		screen.blit(SplashImage,((screen.get_width()/2)-(SplashImage.get_width()/2),(screen.get_height()/2)-(SplashImage.get_width()/2)))