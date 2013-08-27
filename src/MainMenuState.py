#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	MainMenuState.py
#	This Class Handles The Main Menu Screen
#
#----------------------------------

# Imports
import os
import pygame
from State import *

class MainMenuState(State):
	def __init__(self,screen,gamecontroller):
		State.__init__(self)
		
		# Class Variables
		self.Screen = screen
		self.MenuStates = [ 'MainMenu' , 'SettingsMenu' , 'HighScores' , 'PlayMenu' ]
		self.CurrentMenu = self.MenuStates[0]
		self.MouseReleased = True
		self.GameController = gamecontroller
		
		self.MenuButtons = []
		ButtonImages = [ 'quit' , 'settings' , 'highscores' , 'play' , 'back' , 'save' ]
		for button in ButtonImages:
			standard = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'button_'+button+'_standard.png' ))
			hover = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'button_'+button+'_hover.png' ))
			buttonInfo = [ button , False , standard , hover , self.ButtonHandler ]
			self.MenuButtons.append(buttonInfo)
			
		#Load Background Images
		self.Background = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'jungle_background.png' ))
		self.LeftOverlay = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'jungle_left.png' ))
		self.RightOverlay = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'jungle_right.png' ))
		self.MenuBackgroundOverlay = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'background_overlay.png' ))
		
		self.CheckBoxEmpty = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'checkbox_unchecked.png' ))
		self.CheckBoxChecked = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures') , 'checkbox_checked.png' ))
		
		self.Text = pygame.font.SysFont( "times", 24 , True , False )
		self.FullScreen = self.Text.render( "Fullscreen:" , 1 , (255,255,255) )
		self.Resolutions = self.Text.render( "Screen Resolution:" , 1 , (255,255,255) )
		self.Res800x600 = self.Text.render( "800 x 600" , 1 , (255,255,255) )
		self.Res1024x768 = self.Text.render( "1024 x 768" , 1 , (255,255,255) )
		self.Res1280x768 = self.Text.render( "1280 x 768" , 1 , (255,255,255) )
		self.Res1360x768 = self.Text.render( "1360 x 768" , 1 , (255,255,255) )
		self.Res1366x768 = self.Text.render( "1366 x 768" , 1 , (255,255,255) )
		self.Res1600x900 = self.Text.render( "1600 x 900" , 1 , (255,255,255) )
		
	def ExecuteStateLogic( self , KeysHeld , KeysPressed , clock ):
		# Reset Mouse
		if( not pygame.mouse.get_pressed()[0] ):
			self.MouseReleased = True
		
		# Execute Proper Menu Logic
		if( self.CurrentMenu == self.MenuStates[0] ):
			self.ExecuteMainMenu()
		elif( self.CurrentMenu == self.MenuStates[1] ):
			self.ExecuteSettingsMenu()
		elif( self.CurrentMenu == self.MenuStates[2] ):
			self.ExecuteHighScores()
		elif( self.CurrentMenu == self.MenuStates[3] ):
			self.ExecutePlayMenu()
						
	def DrawStateFrame( self , screen , clock ):
		screen.fill( (0,253,251) )
		
		# Draw Background
		for tile in range( 1 + screen.get_width() / self.Background.get_width() ):
			screen.blit( self.Background , ( tile * self.Background.get_width() , screen.get_height() - self.Background.get_height() ))
		screen.blit( self.LeftOverlay , ( 0 , screen.get_height() - self.LeftOverlay.get_height() ))
		screen.blit( self.RightOverlay , ( screen.get_width() - self.RightOverlay.get_width() , screen.get_height() - self.RightOverlay.get_height() ))
		
		if( self.CurrentMenu == self.MenuStates[0] ):
			self.DrawMainMenu()
		elif( self.CurrentMenu == self.MenuStates[1] ):
			self.DrawSettingsMenu()
		elif( self.CurrentMenu == self.MenuStates[2] ):
			self.DrawHighScores()
		elif( self.CurrentMenu == self.MenuStates[3] ):
			self.DrawPlayMenu()
		
	def ExecuteMainMenu( self ):
		# Buttons
		x,y = pygame.mouse.get_pos()
		leftMargin = self.Screen.get_width() / 2 - self.MenuButtons[1][2].get_width() / 2
		rightMargin = self.Screen.get_width() / 2 + self.MenuButtons[1][2].get_width() / 2
		for buttonNum in range( len( self.MenuButtons )):
			self.MenuButtons[buttonNum][1] = False
			
			if( x > leftMargin and x < rightMargin ):
				if( y > self.Screen.get_height() - self.MenuButtons[buttonNum][2].get_height() * (2 + buttonNum) - (buttonNum * 10) and y < self.Screen.get_height() - self.MenuButtons[buttonNum][2].get_height() * (1 + buttonNum) - (buttonNum * 10) ):
					self.MenuButtons[buttonNum][1] = True
					if( pygame.mouse.get_pressed()[0] and self.MouseReleased ):
						self.MenuButtons[buttonNum][4](self.MenuButtons[buttonNum][0])
						self.MouseReleased = False
		
	def ExecuteSettingsMenu( self ):
		#Buttons
		x,y = pygame.mouse.get_pos()
		self.MenuButtons[4][1] = False
		self.MenuButtons[5][1] = False
		
		# Back Button
		if( x > self.Screen.get_width() / 2 - self.MenuButtons[4][2].get_width() / 2 and x < self.Screen.get_width() / 2 + self.MenuButtons[4][2].get_width() / 2 ):
			if( y > self.Screen.get_height() / 2  + self.MenuBackgroundOverlay.get_height() / 2 + 10 and y < self.Screen.get_height() /2  + self.MenuBackgroundOverlay.get_height() / 2 + self.MenuButtons[4][2].get_height() + 10 ):
				self.MenuButtons[4][1] = True
				if( pygame.mouse.get_pressed()[0] and self.MouseReleased):
					self.MenuButtons[4][4](self.MenuButtons[4][0])
					self.MouseReleased = False
		
		# FullScreen Checkbox
		if( x > self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + self.FullScreen.get_width() + 30 and x < self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + self.FullScreen.get_width() + 30 + self.CheckBoxEmpty.get_width() ):
			if( y > self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 15 and y < self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 15 + self.CheckBoxEmpty.get_height() ):
				if( pygame.mouse.get_pressed()[0] and self.MouseReleased ):
					self.MouseReleased = False
					if( self.GameController.UserSettings["[Fullscreen]"] == 1 ):
						self.GameController.UserSettings["[Fullscreen]"] = 0
					else:
						self.GameController.UserSettings["[Fullscreen]"] = 1
					
		# Screen Resolution CheckBoxes
		if( x > self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 140 and x < self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 140 + self.CheckBoxEmpty.get_width() ):
			if( y > self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 83 and y < self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 83 + self.CheckBoxEmpty.get_height() ):
				if( pygame.mouse.get_pressed()[0] and self.MouseReleased ):
					self.MouseReleased = False
					self.GameController.UserSettings["[ScreenWidth]"] = 800
					self.GameController.UserSettings["[ScreenHeight]"] = 600
					
		if( x > self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 140 and x < self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 140 + self.CheckBoxEmpty.get_width() ):
			if( y > self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 113 and y < self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 113 + self.CheckBoxEmpty.get_height() ):
				if( pygame.mouse.get_pressed()[0] and self.MouseReleased ):
					self.MouseReleased = False
					self.GameController.UserSettings["[ScreenWidth]"] = 1024
					self.GameController.UserSettings["[ScreenHeight]"] = 768
		
		if( x > self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 140 and x < self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 140 + self.CheckBoxEmpty.get_width() ):
			if( y > self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 143 and y < self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 143 + self.CheckBoxEmpty.get_height() ):
				if( pygame.mouse.get_pressed()[0] and self.MouseReleased):
					self.MouseReleased = False
					self.GameController.UserSettings["[ScreenWidth]"] = 1280
					self.GameController.UserSettings["[ScreenHeight]"] = 768
					
		if( x > self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 320 and x < self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 320 + self.CheckBoxEmpty.get_width() ):
			if( y > self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 83 and y < self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 83 + self.CheckBoxEmpty.get_height() ):
				if( pygame.mouse.get_pressed()[0] and self.MouseReleased ):
					self.MouseReleased = False
					self.GameController.UserSettings["[ScreenWidth]"] = 1360
					self.GameController.UserSettings["[ScreenHeight]"] = 768
					
		if( x > self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 320 and x < self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 320 + self.CheckBoxEmpty.get_width() ):
			if( y > self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 113 and y < self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 113 + self.CheckBoxEmpty.get_height() ):
				if( pygame.mouse.get_pressed()[0] and self.MouseReleased ):
					self.MouseReleased = False
					self.GameController.UserSettings["[ScreenWidth]"] = 1366
					self.GameController.UserSettings["[ScreenHeight]"] = 768
		
		if( x > self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 320 and x < self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 320 + self.CheckBoxEmpty.get_width() ):
			if( y > self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 143 and y < self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 143 + self.CheckBoxEmpty.get_height() ):
				if( pygame.mouse.get_pressed()[0] and self.MouseReleased ):
					self.MouseReleased = False
					self.GameController.UserSettings["[ScreenWidth]"] = 1600
					self.GameController.UserSettings["[ScreenHeight]"] = 900

					
		# Save Button
		if( x > self.Screen.get_width() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - self.MenuButtons[5][3].get_width() - 10 and x < self.Screen.get_width() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - 10 ):
			if( y > self.Screen.get_height() /2  + self.MenuBackgroundOverlay.get_height() / 2 - self.MenuButtons[5][3].get_height() - 10 and y < self.Screen.get_height() /2  + self.MenuBackgroundOverlay.get_height() / 2 - 10 ):
				self.MenuButtons[5][1] = True
				if( pygame.mouse.get_pressed()[0] and self.MouseReleased ):
					self.MouseReleased = False
					self.MenuButtons[4][4](self.MenuButtons[4][0])
					self.MenuButtons[5][4](self.MenuButtons[5][0])
					self.GameController.InitializeWindow("TowersOfHanoi")
					
	def ExecuteHighScores( self ):
		pass
		
	def ExecutePlayMenu( self ):
		pass
		
	def DrawMainMenu( self ):
		# Draw Buttons
		for button in range( 4 ):
			if( self.MenuButtons[button][1] ):
				self.Screen.blit( self.MenuButtons[button][3] , ( self.Screen.get_width() / 2 - self.MenuButtons[button][3].get_width() / 2 , self.Screen.get_height() - self.MenuButtons[button][3].get_height() * (2 + button) - (button * 10) ))
			else:
				self.Screen.blit( self.MenuButtons[button][2] , ( self.Screen.get_width() / 2 - self.MenuButtons[button][2].get_width() / 2 , self.Screen.get_height() - self.MenuButtons[button][2].get_height() * (2 + button) - (button * 10) ))
		
	def DrawSettingsMenu( self ):
		# Draw Background
		self.Screen.blit( self.MenuBackgroundOverlay , ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2, self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 ))
		
		# Draw Save Button
		if( self.MenuButtons[5][1] ):
			self.Screen.blit( self.MenuButtons[5][3] , ( self.Screen.get_width() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - self.MenuButtons[5][3].get_width() - 10 , self.Screen.get_height() /2  + self.MenuBackgroundOverlay.get_height() / 2 - self.MenuButtons[5][3].get_height() - 10 ))
		else:
			self.Screen.blit( self.MenuButtons[5][2] , ( self.Screen.get_width() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - self.MenuButtons[5][2].get_width() - 10 , self.Screen.get_height() /2  + self.MenuBackgroundOverlay.get_height() / 2 - self.MenuButtons[5][2].get_height() - 10 ))
					
		# Draw Back Button
		if( self.MenuButtons[4][1] ):
			self.Screen.blit( self.MenuButtons[4][3] , ( self.Screen.get_width() / 2 - self.MenuButtons[4][3].get_width() / 2 , self.Screen.get_height() / 2  + self.MenuBackgroundOverlay.get_height() / 2 + 10 ))
		else:
			self.Screen.blit( self.MenuButtons[4][2] , ( self.Screen.get_width() / 2 - self.MenuButtons[4][2].get_width() / 2 , self.Screen.get_height() / 2  + self.MenuBackgroundOverlay.get_height() / 2 + 10 ))
			
		# Draw Fullscreen
		self.Screen.blit(self.FullScreen, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 20, self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 10 ))
		if( self.GameController.UserSettings["[Fullscreen]"] == 1 ):
			self.Screen.blit( self.CheckBoxChecked, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + self.FullScreen.get_width() + 30 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 15 ))
		else:
			self.Screen.blit( self.CheckBoxEmpty, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + self.FullScreen.get_width() + 30 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 15 ))
		
		# Draw Resolutions
		self.Screen.blit( self.Resolutions, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 20 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 50 ))
		self.Screen.blit( self.Res800x600, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 20 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 80 ))
		self.Screen.blit( self.Res1024x768, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 20 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 110 ))
		self.Screen.blit( self.Res1280x768, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 20 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 140 ))
		self.Screen.blit( self.Res1360x768, ( self.Screen.get_width() / 2 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 80 ))
		self.Screen.blit( self.Res1366x768, ( self.Screen.get_width() / 2 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 110 ))
		self.Screen.blit( self.Res1600x900, ( self.Screen.get_width() / 2 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 140 ))
		
		if( self.GameController.UserSettings['[ScreenWidth]'] == 800 ):
			self.Screen.blit( self.CheckBoxChecked, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 140 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 83 ))
		else:
			self.Screen.blit( self.CheckBoxEmpty, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 140 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 83 ))
		
		if(self.GameController.UserSettings['[ScreenWidth]'] == 1024 ):
			self.Screen.blit( self.CheckBoxChecked, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 140 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 113 ))
		else:
			self.Screen.blit( self.CheckBoxEmpty, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 140 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 113 ))
		
		if( self.GameController.UserSettings['[ScreenWidth]'] == 1280 ):
			self.Screen.blit(self.CheckBoxChecked, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 140 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 143 ))
		else:
			self.Screen.blit(self.CheckBoxEmpty, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 140 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 143 ))

		if( self.GameController.UserSettings['[ScreenWidth]'] == 1360 ):
			self.Screen.blit( self.CheckBoxChecked, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 320 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 83 ))
		else:
			self.Screen.blit( self.CheckBoxEmpty, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 320 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 83 ))

		if( self.GameController.UserSettings['[ScreenWidth]'] == 1366 ):
			self.Screen.blit( self.CheckBoxChecked, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 320 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 113 ))
		else:
			self.Screen.blit( self.CheckBoxEmpty, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 320 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 113 ))

		if(self.GameController.UserSettings['[ScreenWidth]'] == 1600):
			self.Screen.blit( self.CheckBoxChecked, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 320 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 143 ))
		else:
			self.Screen.blit( self.CheckBoxEmpty, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 320 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 143 ))
		
	def DrawHighScores( self ):
		pass
		
	def DrawPlayMenu( self ):
		pass
		
	## Button Handlers
	def ButtonHandler( self , button ):
		if( button == 'save' ):
			self.GameController.WriteUserSettings()
		elif( button == 'back' ):
			self.CurrentMenu = self.MenuStates[0]
		elif( button == 'quit' ):
			self.StateQuit = True
		elif( button == 'settings' ):
			self.CurrentMenu = self.MenuStates[1]
		elif( button == 'highscores' ):
			self.CurrentMenu = self.MenuStates[2]
		elif( button == 'play' ):
			self.CurrentMenu = self.MenuStates[3]
			