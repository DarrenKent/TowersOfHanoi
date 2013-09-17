#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	Disk.py
#	This Class Handles Disk Objects
#
#----------------------------------

import os
import pygame
import Button

class Disk ( Button.Button ):
	def __init__( self , diskId , row , column , image , screen , buttonHandler , color ):
		self.DiskImage = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , image ))
		self.Color = color
		Button.Button.__init__( self , 
						screen.get_width() / 2 - 236 + 236 * column - self.DiskImage.get_width() / 2 , 
						screen.get_height() - 95 - 35 * (row) , 
						diskId , image , image , buttonHandler )
		
		self.NewX = self.X
		self.NewY = self.Y
		self.Column = column
		self.Row = row
		self.Screen = screen
		self.MouseXDist = 0
		self.MouseYDist = 0
		
		
	def DrawButton( self ):
		self.Screen.blit( self.DiskImage , ( self.NewX , self.NewY ))
		rect = pygame.Surface( ( self.Width , self.Height ) , pygame.SRCALPHA , 32 )
		rect.fill( self.Color )
		self.Screen.blit( rect , ( self.NewX , self.NewY ),None,pygame.BLEND_RGB_MULT)
		
	
	def SetMouseHover( self , mouseX , mouseY ):
		if( mouseX > self.NewX and mouseX < self.NewX + self.Width ):
			if( mouseY > self.NewY and mouseY < self.NewY + self.Height ):
				self.Hover = True
				return
		self.Hover = False
		
	def SetLocation( self , colPlacement , rowPlacement ):
		tX , tY = pygame.mouse.get_pos()
		newColumn = -1
		if( tX > self.Screen.get_width() / 2 - 236 - 117 and tX < self.Screen.get_width() / 2 - 236 + 117 ):
			newColumn = 0
			newX = self.Screen.get_width() / 2 - 236 - self.DiskImage.get_width() / 2
		elif( tX > self.Screen.get_width() / 2 - 117 and tX < self.Screen.get_width() / 2 + 117 ):
			newColumn = 1
			newX = self.Screen.get_width() / 2 - self.DiskImage.get_width() / 2
		elif( tX > self.Screen.get_width() / 2 + 236 - 117 and tX < self.Screen.get_width() / 2 + 236 + 117 ):
			newColumn = 2
			newX = self.Screen.get_width() / 2 + 236 - self.DiskImage.get_width() / 2
			
		if( newColumn != -1 and (len(rowPlacement[newColumn]) == 0 or self.ButtonId < min(rowPlacement[newColumn]))):
			self.Column = newColumn
			self.Row = colPlacement[self.Column]+1
			self.X = newX
			self.Y = self.Screen.get_height() - 95 - 35 * (self.Row)
			
		self.NewX = self.X
		self.NewY = self.Y