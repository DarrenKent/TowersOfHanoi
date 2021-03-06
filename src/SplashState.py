#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	SplashState.py
#	This Class handles the SplashScreens
#
#----------------------------------

# Imports
import os
import pygame
from State import *

class SplashState( State ):
	def __init__( self ):
		State.__init__( self )
		self.SplashScreens = [ ( 'dkapps.jpg' , (255,255,255) ) ]
		self.CurrentSplash = 0
		self.CurrentSplashFrame = 0
		self.CurrentSplashAlpha = 0
		
		self.SplashImage = pygame.image.load( os.path.join ( os.path.join( 'data' , 'textures' ) , self.SplashScreens[self.CurrentSplash][0] ))
		
	def ExecuteStateLogic( self , KeysHeld , KeysPressed , clock ):
		if( pygame.K_ESCAPE in KeysPressed ):
			self.StateQuit = True
			
		if( self.CurrentSplash >= len( self.SplashScreens )):
			self.StateQuit = True
		
		self.CurrentSplashFrame += 1 * clock.get_time() / 1000.0
		if( self.CurrentSplashFrame > 1.5 and self.CurrentSplashFrame < 4 ):
			self.CurrentSplashAlpha += 100 * clock.get_time() / 1000.0
		if( self.CurrentSplashFrame > 8 and self.CurrentSplashFrame < 10 ):
			self.CurrentSplashAlpha -= 255 * clock.get_time() / 1000.0
		if( self.CurrentSplashFrame > 11.5 ):
			self.StateQuit = True
			
	def DrawStateFrame( self , screen , clock ):
		screen.fill( self.SplashScreens[self.CurrentSplash][1] )
		self.SplashImage.set_alpha( self.CurrentSplashAlpha )
		screen.blit( self.SplashImage , ( (screen.get_width() / 2) - (self.SplashImage.get_width() / 2) , (screen.get_height() / 2) - (self.SplashImage.get_width() / 2) ))