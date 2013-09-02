#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	CheckBox.py
#	This Class is a CheckBox
#
#----------------------------------

# Imports
import os
import pygame
import Button

class CheckBox( Button.Button ):
	def __init__( self , xPos , yPos , buttonId , label , font ):
		Button.Button.__init__( self , xPos , yPos , buttonId , 'checkbox_unchecked.png' , 'checkbox_checked.png' , None)
		self.Label = label
		self.Font = font
		self.LabelRender = self.Font.render( self.Label , 1 , (255,255,255) )
		self.Checked = False
		
	def DrawButton( self , screen ):
		if( self.Checked ):
			screen.blit( self.HoverImage , ( self.X , self.Y ))
		else:
			screen.blit( self.StandardImage , ( self.X , self.Y ))
		screen.blit( self.LabelRender , ( self.X + self.StandardImage.get_width() + 8 , self.Y-2 ))
			