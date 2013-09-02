#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	Button.py
#	This Class is a Simple Button
#
#----------------------------------

# Imports
import os
import pygame

class Button:
	def __init__( self , xPos , yPos , buttonId , standardFilename , hoverFilename , buttonHandler ):
		self.X = xPos
		self.Y = yPos
		self.ButtonId = buttonId
		self.StandardImage = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , standardFilename ))
		self.HoverImage = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , hoverFilename ))
		self.Width = self.StandardImage.get_width()
		self.Height = self.StandardImage.get_height()
		self.Hover = False
		self.ButtonHandler = buttonHandler
		
	def IsMouseInside( self ):
		return self.Hover
		
	def SetMouseHover( self , mouseX , mouseY ):
		if( mouseX > self.X and mouseX < self.X + self.Width ):
			if( mouseY > self.Y and mouseY < self.Y + self.Height ):
				self.Hover = True
				return
		self.Hover = False
		
	def ExecuteButton( self ):
		self.ButtonHandler( self.ButtonId )
		
	def DrawButton( self , screen ):
		if( self.Hover ):
			screen.blit( self.HoverImage , ( self.X , self.Y ))
		else:
			screen.blit( self.StandardImage , ( self.X , self.Y ))
			