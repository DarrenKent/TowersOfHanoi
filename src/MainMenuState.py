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
import Button
import CheckBox

class MainMenuState( State ):
	def __init__( self , screen , gamecontroller ):
		State.__init__( self )
		
		# Class Variables
		self.Screen = screen
		self.MenuStates = [ 'MainMenu' , 'SettingsMenu' , 'HighScores' , 'PlayMenu' ]
		self.CurrentMenu = self.MenuStates[0]
		self.MouseReleased = True
		self.GameController = gamecontroller
		
		# Background Images
		self.Background = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'jungle_background.png' ))
		self.LeftOverlay = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'jungle_left.png' ))
		self.RightOverlay = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'jungle_right.png' ))
		self.MenuBackgroundOverlay = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'background_overlay.png' ))
		
		self.InitializeButtons()

	def InitializeButtons( self ):
		self.CheckBoxEmpty = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'checkbox_unchecked.png' ))
		self.CheckBoxChecked = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures') , 'checkbox_checked.png' ))
		
		self.MenuButtons = []
		ButtonImages = [ 'quit' , 'settings' , 'highscores' , 'play' ]
		for button in range( len( ButtonImages )):
			tNewButton = Button.Button( self.Screen.get_width() / 2 - 75 , self.Screen.get_height() - 50 * (2 + button) - (button * 10) , ButtonImages[button] , 'button_' + ButtonImages[button] + '_standard.png' , 'button_' + ButtonImages[button] + '_hover.png' , self.ButtonHandler )
			self.MenuButtons.append(tNewButton)
		self.MenuButtons.append(Button.Button( self.Screen.get_width() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - 160 , self.Screen.get_height() / 2 + self.MenuBackgroundOverlay.get_height() / 2 - 60, 'back' , 'button_back_standard.png' , 'button_back_hover.png' , self.ButtonHandler ))
		self.MenuButtons.append(Button.Button( self.Screen.get_width() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - 320 , self.Screen.get_height() / 2 + self.MenuBackgroundOverlay.get_height() / 2 - 60, 'save' , 'button_save_standard.png' , 'button_save_hover.png' , self.ButtonHandler ))
		
		self.CheckBoxes = []
		Checks = [ 'Fullscreen:' , '800x600' , '1024x768' , '1280x768' , '1360x768' , '1366x768' , '1600x900' ]
		
		columns = [ self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 30 , self.Screen.get_width() / 2 ]
		
		self.Text = pygame.font.SysFont( "times", 24 , True , False )
		Fullscreen = CheckBox.CheckBox( columns[0] , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 30 , Checks[0] , Checks[0] , self.Text )
		if( self.GameController.UserSettings['[Fullscreen]'] == 1 ):
			Fullscreen.Checked = True
		self.CheckBoxes.append( Fullscreen )
		resolution = str( self.GameController.UserSettings['[ScreenWidth]'] ) + 'x' + str( self.GameController.UserSettings['[ScreenHeight]'] )
		count = 1
		for col in range( 2 ):
			for row in range( 3 ):
				tCheckBox = CheckBox.CheckBox( columns[col] , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 83 + 30 * row , Checks[count] , Checks[count] , self.Text )
				if( resolution == tCheckBox.ButtonId ):
					tCheckBox.Checked = True
				self.CheckBoxes.append(tCheckBox)
				count += 1
		
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
		tX,tY = pygame.mouse.get_pos()
		for button in self.MenuButtons:
			button.SetMouseHover( tX, tY )
			if( button.IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased ):
				self.MouseReleased = False
				button.ExecuteButton()
		
	def ExecuteSettingsMenu( self ):
		# Get Mouse Coords
		tX,tY = pygame.mouse.get_pos()
		
		# Check To See If Mouse is Over any Buttons
		self.MenuButtons[4].SetMouseHover( tX, tY )
		self.MenuButtons[5].SetMouseHover( tX, tY )
		for check in self.CheckBoxes:
			check.SetMouseHover( tX, tY )
		
		# Button Press Checks
		if( self.MenuButtons[4].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased):
			self.MenuButtons[4].ExecuteButton()
			self.MouseReleased = False
			
		if( self.MenuButtons[5].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased):
			self.MenuButtons[5].ExecuteButton()
			self.GameController.InitializeWindow("TowersOfHanoi")
			self.InitializeButtons()
			self.MouseReleased = False
		
		# CheckBox Press Checks
		if( self.CheckBoxes[0].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased ):
			self.MouseReleased = False
			if( self.CheckBoxes[0].Checked ):
				self.GameController.UserSettings['[Fullscreen]'] = 0
				self.CheckBoxes[0].Checked = False
			elif( not self.CheckBoxes[0].Checked ):
				self.GameController.UserSettings['[Fullscreen]'] = 1
				self.CheckBoxes[0].Checked = True
				
		resolution = str( self.GameController.UserSettings['[ScreenWidth]'] ) + 'x' + str( self.GameController.UserSettings['[ScreenHeight]'] )
		for check in range( 6 ):
			if( resolution == self.CheckBoxes[check+1].ButtonId ):
				self.CheckBoxes[check+1].Checked = True
			else:
				self.CheckBoxes[check+1].Checked = False
			if( self.CheckBoxes[check+1].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased ):
				self.MouseReleased = False
				size = self.CheckBoxes[check+1].ButtonId.split('x')
				self.GameController.UserSettings['[ScreenWidth]'] = int(size[0])
				self.GameController.UserSettings['[ScreenHeight]'] = int(size[1])
			
	def ExecuteHighScores( self ):
		pass
		
	def ExecutePlayMenu( self ):
		pass
		
	def DrawMainMenu( self ):
		# Draw Buttons
		for button in range( 4 ):
			self.MenuButtons[button].DrawButton( self.Screen )
		
	def DrawSettingsMenu( self ):
		# Draw Background
		self.Screen.blit( self.MenuBackgroundOverlay , ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2, self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 ))
		
		self.MenuButtons[4].DrawButton( self.Screen )	# Back Button
		self.MenuButtons[5].DrawButton( self.Screen )	# Save Button
		
		for checkbox in self.CheckBoxes:
			checkbox.DrawButton( self.Screen )
		
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
			