#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	PlayState.py
#	This Class Handles The GamePlay
#
#----------------------------------

import os
import pygame
from State import *
import Button

class PlayState( State ):
	def __init__( self , screen , gameController , numDisks ):
		State.__init__( self )
		self.Screen = screen
		self.NumDisks = numDisks
		self.GameController = gameController
		self.Texture = 'jungle'
		self.Pause = False
		
		# Initialize Background Images
		self.Background = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , self.Texture+'_background.png' ))
		self.LeftOverlay = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , self.Texture+'_left.png' ))
		self.LeftForground = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , self.Texture+'_left_forground.png' ))
		self.RightOverlay = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , self.Texture+'_right.png' ))
		self.RightForground = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , self.Texture+'_right_forground.png' ))
		self.Stage = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , self.Texture+'_stage.png' ))
		self.MenuBackgroundOverlay = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'background_overlay.png' ))
		
		self.InitializeButtons()
		
	def InitializeButtons( self ):
		self.Buttons = []
		self.Buttons.append( Button.Button( self.Screen.get_width() - 160 , 10 , 'Menu' , 'button_menu_standard.png' , 'button_menu_hover.png' , self.ButtonHandler ))
		
	def ExecuteStateLogic( self , KeysHeld , KeysPressed , clock ):
		if( not pygame.mouse.get_pressed()[0] ):
			self.MouseReleased = True
			self.StartSlider = False
			
		if( self.Pause ):
			self.ExecutePauseMenuLogic()
		else:
			self.ExecuteGameLogic()
			
	def ExecuteGameLogic( self ):
		tX , tY = pygame.mouse.get_pos()
		self.Buttons[0].SetMouseHover( tX , tY )
		if( self.Buttons[0].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased ):
			self.Buttons[0].ExecuteButton()
		
			
	def ExecutePauseMenuLogic( self ):
		tX , tY = pygame.mouse.get_pos()
	
		
		
	def DrawStateFrame( self , screen , clock ):
		screen.fill( (0,253,251) )
		
		# Draw Background
		for tile in range( 1 + screen.get_width() / self.Background.get_width() ):
			screen.blit( self.Background , ( tile * self.Background.get_width() , screen.get_height() - self.Background.get_height() ))
		screen.blit( self.LeftOverlay , ( 0 , screen.get_height() - self.LeftOverlay.get_height() ))
		screen.blit( self.RightOverlay , ( screen.get_width() - self.RightOverlay.get_width() , screen.get_height() - self.RightOverlay.get_height() ))
		screen.blit( self.Stage , ( screen.get_width() / 2 - self.Stage.get_width() / 2 , screen.get_height() - self.Stage.get_height() ))
		screen.blit( self.LeftForground , ( 0 , screen.get_height() - self.LeftForground.get_height() ))
		screen.blit( self.RightForground , ( screen.get_width() - self.RightForground.get_width() , screen.get_height() - self.RightForground.get_height() ))
		
		self.Buttons[0].DrawButton( self.Screen )
		
		if( self.Pause ):
			self.DrawPauseMenu()
			
	def DrawPauseMenu( self ):
		for tile in range( 1 + self.Screen.get_width() / self.Background.get_width() ):
			self.Screen.blit( self.Background , ( tile * self.Background.get_width() , self.Screen.get_height() - self.Background.get_height() ))
		rect = pygame.Rect(0,0,self.Screen.get_width(),self.Screen.get_height())
		self.Screen.fill( (255,0,0,.25), rect, pygame.BLEND_RGBA_MIN)
		self.Screen.blit( self.MenuBackgroundOverlay , ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 ))
		
	def ButtonHandler( self , button ):
		self.MouseReleased = False
		if( button.ButtonId == 'Menu' ):
			self.Pause = True