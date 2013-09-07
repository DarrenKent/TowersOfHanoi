#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	Arrow.py
#	This Class is a Arrow Button
#
#----------------------------------

# Imports
import os
import pygame
import Button

class Arrow(Button.Button):
	def __init__( self , xPos , yPos , buttonId , standardFilename , hoverFilename , grayFilename , buttonHandler ):
		Button.Button.__init__( self , xPos , yPos , buttonId , standardFilename , hoverFilename , buttonHandler )
		self.Gray = False
		self.GrayImage = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , grayFilename ))
		
	def DrawButton( self , screen ):
		if( self.Gray ):
			screen.blit( self.GrayImage , ( self.X , self.Y ))
		elif( self.Hover ):
			screen.blit( self.HoverImage , ( self.X , self.Y ))
		else:
			screen.blit( self.StandardImage , ( self.X , self.Y ))
			