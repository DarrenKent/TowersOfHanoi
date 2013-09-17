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
import Arrow
import PlayState

class MainMenuState( State ):
	def __init__( self , screen , gamecontroller ):
		State.__init__( self )
		
		# Class Variables
		self.Screen = screen
		self.MenuStates = [ 'MainMenu' , 'SettingsMenu' , 'HighScores' , 'PlayMenu' ]
		self.CurrentMenu = self.MenuStates[0]
		self.MouseReleased = True
		self.GameController = gamecontroller
		self.StartSlider = False
		self.ScoresPage = 1
		self.NumDisks = 3
		self.ColorNum = 0
		self.Colors = [ (255,0,0) , (0,255,0) , (0,0,255) ]
		
		# Background Images
		self.Background = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'jungle_background.png' ))
		self.Logo = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'logo.png' ))
		self.LeftOverlay = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'jungle_left.png' ))
		self.RightOverlay = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'jungle_right.png' ))
		self.MenuBackgroundOverlay = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'background_overlay.png' ))
		self.LeftForground = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'jungle_left_forground.png' ))
		self.RightForground = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'jungle_right_forground.png' ))
		self.Disk = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'disk_1.png' ))
		
		self.InitializeButtons()
		
	def PlayBGMusic( self ):
		pygame.mixer.music.load( os.path.join( os.path.join( 'data' , 'music' ) , "MasalaMadness(Pad).mp3" ))
		pygame.mixer.music.set_volume(self.GameController.UserSettings["[MusicVolume]"]/100.0)
		pygame.mixer.music.play(-1)

	def InitializeButtons( self ):
		self.Text = pygame.font.SysFont( "times", 24 , True , False )
		self.SFXVolumeText = self.Text.render( "SFX Volume" , 1 , (255,255,255) )
		self.MusicVolumeText = self.Text.render( "Music Volume" , 1 , (255,255,255) )
		self.PlayTitleText = self.Text.render( "Play" , 1 ,  (255,255,255) )
		self.NumDisksText = self.Text.render( "Number of Disks" , 1 , (255,255,255) )
		
		self.SliderBar = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'slider_bar.png' ))
		self.CheckBoxEmpty = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'checkbox_unchecked.png' ))
		self.CheckBoxChecked = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures') , 'checkbox_checked.png' ))
		
		self.MenuButtons = []
		ButtonImages = [ 'Quit' , 'Settings' , 'High Scores' , 'Play' ]
		for button in range( len( ButtonImages )):
			tNewButton = Button.Button( self.Screen.get_width() / 2 - 75 , self.Screen.get_height() - 50 * (2 + button) - (button * 10) , ButtonImages[button] , 'button_standard.png' , 'button_hover.png' , self.ButtonHandler )
			self.MenuButtons.append(tNewButton)
		self.MenuButtons.append(Button.Button( self.Screen.get_width() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - 160 , self.Screen.get_height() / 2 + self.MenuBackgroundOverlay.get_height() / 2 - 60, 'Back' , 'button_standard.png' , 'button_hover.png' , self.ButtonHandler ))
		self.MenuButtons.append(Button.Button( self.Screen.get_width() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - 320 , self.Screen.get_height() / 2 + self.MenuBackgroundOverlay.get_height() / 2 - 60, 'Save' , 'button_standard.png' , 'button_hover.png' , self.ButtonHandler ))
		self.MenuButtons.append(Button.Button( self.Screen.get_width() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - 160 , self.Screen.get_height() / 2 + self.MenuBackgroundOverlay.get_height() / 2 - 120, 'Default' , 'button_standard.png' , 'button_hover.png' , self.ButtonHandler ))
		self.MenuButtons.append(Button.Button( self.Screen.get_width() / 2 + self.GameController.UserSettings["[MusicVolume]"] - 4, self.Screen.get_height() / 2 + self.MusicVolumeText.get_height() / 2 - 7 , 'Music' , 'button_slider_standard.png' , 'button_slider_hover.png' , self.SliderHandler ))
		self.MenuButtons.append(Button.Button( self.Screen.get_width() / 2 + self.GameController.UserSettings["[SFXVolume]"] - 4, self.Screen.get_height() / 2 + self.SFXVolumeText.get_height() / 2 + 23 , 'SFX' , 'button_slider_standard.png' , 'button_slider_hover.png' , self.SliderHandler ))
		self.MenuButtons.append(Button.Button( self.Screen.get_width() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - 160 , self.Screen.get_height() / 2 + self.MenuBackgroundOverlay.get_height() / 2 - 120 , 'Start' , 'button_standard.png' , 'button_hover.png' , self.ButtonHandler ))
		self.MenuButtons.append(Button.Button( self.Screen.get_width() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - 320 , self.Screen.get_height() / 2 + self.MenuBackgroundOverlay.get_height() / 2 - 120, 'Reset Scores' , 'button_standard.png' , 'button_hover.png' , self.ButtonHandler ))
		
		self.Arrows = []
		self.Arrows.append(Arrow.Arrow( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 30 , self.Screen.get_height() / 2 + self.MenuBackgroundOverlay.get_height() / 2 - 50 , 'ScoresLeft' , 'arrow_left_standard.png' , 'arrow_left_hover.png' , 'arrow_left_gray.png' , self.ArrowHandler ))
		self.Arrows.append(Arrow.Arrow( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 70 , self.Screen.get_height() / 2 + self.MenuBackgroundOverlay.get_height() / 2 - 50 , 'ScoresRight' , 'arrow_right_standard.png' , 'arrow_right_hover.png' , 'arrow_right_gray.png' , self.ArrowHandler ))
		self.Arrows.append(Arrow.Arrow( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 30 , self.Screen.get_height() / 2 - 100 , 'DisksLeft' , 'arrow_left_standard.png' , 'arrow_left_hover.png' , 'arrow_left_gray.png' , self.ArrowHandler ))
		self.Arrows.append(Arrow.Arrow( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 120 , self.Screen.get_height() / 2 - 100 , 'DisksRight' , 'arrow_right_standard.png' , 'arrow_right_hover.png' , 'arrow_right_gray.png' , self.ArrowHandler ))
		self.Arrows.append(Arrow.Arrow( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 30 , self.Screen.get_height() / 2 - 50, 'DiskColorLeft' , 'arrow_left_standard.png' , 'arrow_left_hover.png' , 'arrow_left_gray.png' , self.ArrowHandler ))
		self.Arrows.append(Arrow.Arrow( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 180 , self.Screen.get_height() / 2 - 50, 'DiskColorRight' , 'arrow_right_standard.png' , 'arrow_right_hover.png' , 'arrow_right_gray.png' , self.ArrowHandler ))
		
		
		self.CheckBoxes = []
		Checks = [ 'Fullscreen:' , '800x600' , '1024x768' , '1280x768' , '1360x768' , '1366x768' , '1600x900' ]
		
		columns = [ self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 30 , self.Screen.get_width() / 2 ]
		
		
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
		if( not pygame.mixer.music.get_busy() ):
			self.PlayBGMusic()
			
		# Reset Mouse
		if( not pygame.mouse.get_pressed()[0] ):
			self.MouseReleased = True
			self.StartSlider = False
		
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
		screen.blit( self.LeftForground , ( 0 , screen.get_height() - self.LeftForground.get_height() ))
		screen.blit( self.RightForground , ( screen.get_width() - self.RightForground.get_width() , screen.get_height() - self.RightForground.get_height() ))
		
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
		self.MenuButtons[6].SetMouseHover( tX, tY )
		self.MenuButtons[7].SetMouseHover( tX, tY )
		self.MenuButtons[8].SetMouseHover( tX, tY )
		self.MenuButtons[10].SetMouseHover( tX, tY )
		for check in self.CheckBoxes:
			check.SetMouseHover( tX, tY )
		
		# Button Press Checks
		for button in range( 4 ):
			if( self.MenuButtons[button+4].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased ):
				self.MenuButtons[button+4].ExecuteButton()
			
		self.MenuButtons[7].ExecuteButton()
		self.MenuButtons[8].ExecuteButton()
		
		if( self.MenuButtons[10].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased ):
				self.MenuButtons[10].ExecuteButton()
		
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
		# Get Mouse Coords
		tX,tY = pygame.mouse.get_pos()
		
		# Check To See If Mouse is Over any Buttons
		self.MenuButtons[4].SetMouseHover( tX, tY )
		self.Arrows[0].SetMouseHover( tX, tY )
		self.Arrows[1].SetMouseHover( tX, tY )
		
		if( self.MenuButtons[4].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased ):
			self.MenuButtons[4].ExecuteButton()
			
		if( self.Arrows[0].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased and self.ScoresPage != 1):
			self.Arrows[0].ExecuteButton()
			
		if( self.Arrows[1].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased and self.ScoresPage != 6):
			self.Arrows[1].ExecuteButton()
			
		if( self.ScoresPage == 1 ):
			self.Arrows[0].Gray = True
		else:
			self.Arrows[0].Gray = False
			
		if( self.ScoresPage == 6 ):
			self.Arrows[1].Gray = True
		else:
			self.Arrows[1].Gray = False
		
	def ExecutePlayMenu( self ):
		# Get Mouse Coords
		tX,tY = pygame.mouse.get_pos()
		
		# Check To See If Mouse is Over any Buttons
		self.MenuButtons[4].SetMouseHover( tX , tY )	# Back Button
		self.MenuButtons[9].SetMouseHover( tX , tY )
		self.Arrows[2].SetMouseHover( tX , tY )
		self.Arrows[3].SetMouseHover( tX , tY )
		self.Arrows[4].SetMouseHover( tX , tY )
		self.Arrows[5].SetMouseHover( tX , tY )
        
		if( self.MenuButtons[4].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased ):
			self.MenuButtons[4].ExecuteButton()
			
		if( self.MenuButtons[9].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased ):
			self.MenuButtons[9].ExecuteButton()
			
		if( self.Arrows[2].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased and self.NumDisks != 3):
			self.Arrows[2].ExecuteButton()
			
		if( self.Arrows[3].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased and self.NumDisks != 8):
			self.Arrows[3].ExecuteButton()
		
		if( self.Arrows[4].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased):
			self.Arrows[4].ExecuteButton()
			
		if( self.Arrows[5].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased):
			self.Arrows[5].ExecuteButton()
			
		if( self.NumDisks == 3 ):
			self.Arrows[2].Gray = True
		else:
			self.Arrows[2].Gray = False
			
		if( self.NumDisks == 8 ):
			self.Arrows[3].Gray = True
		else:
			self.Arrows[3].Gray = False
			
		
	def DrawMainMenu( self ):
		self.Screen.blit( self.Logo , ( self.Screen.get_width() / 2 - self.Logo.get_width() / 2 , self.Screen.get_height() / 2 - self.Logo.get_height()))
		# Draw Buttons
		for button in range( 4 ):
			self.MenuButtons[button].DrawButtonWithText( self.Screen )
		
	def DrawSettingsMenu( self ):
		# Draw Background
		self.Screen.blit( self.MenuBackgroundOverlay , ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2, self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 ))
		
		# Draw Sliders
		self.Screen.blit( self.MusicVolumeText , ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 30 , self.Screen.get_height() / 2 ))
		self.Screen.blit( self.SFXVolumeText , ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 30 , self.Screen.get_height() / 2 + 30 ))
		
		self.Screen.blit( self.SliderBar , ( self.Screen.get_width() / 2 , self.Screen.get_height() / 2 + self.MusicVolumeText.get_height() / 2 ))
		self.Screen.blit( self.SliderBar , ( self.Screen.get_width() / 2 , self.Screen.get_height() / 2 + self.SFXVolumeText.get_height() / 2 + 30))
		
		# Draw Buttons
		self.MenuButtons[4].DrawButtonWithText( self.Screen )	# Back Button
		self.MenuButtons[5].DrawButtonWithText( self.Screen )	# Save Button
		self.MenuButtons[6].DrawButtonWithText( self.Screen )	# Default Button
		self.MenuButtons[7].DrawButton( self.Screen )	# Music Slider
		self.MenuButtons[8].DrawButton( self.Screen )	# SFX Slider
		self.MenuButtons[10].DrawButtonWithText( self.Screen )
		
		# Draw CheckBoxes
		for checkbox in self.CheckBoxes:
			checkbox.DrawButton( self.Screen )
		
	def DrawHighScores( self ):
		# Draw Background
		self.Screen.blit( self.MenuBackgroundOverlay , ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2, self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 ))
		
		# Draw Buttons
		self.MenuButtons[4].DrawButtonWithText( self.Screen )	# Back Button
		
        # Draw Scores
		tScoreTitle = self.Text.render( "Fastest Times: " + str(self.ScoresPage+2) + " Disks" , 1 , (255,255,255) )
		self.Screen.blit ( tScoreTitle , ( self.Screen.get_width()  / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 30 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 20 ))
		for score in range( 10 ):
			tPlaceText = self.Text.render( str( score + 1 ) + ":" , 1 , (255,255,255) )
			self.Screen.blit( tPlaceText , ( self.Screen.get_width()  / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 30 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 25 * ( score + 3 ) ))
			tPlayerText = self.Text.render( self.GameController.HighScores['['+str(self.ScoresPage+2)+'-'+str(score+1)+']'][1] , 1 , (255,255,255) )
			self.Screen.blit( tPlayerText , ( self.Screen.get_width()  / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 80 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 25 * ( score + 3 ) ))
			tScoreText = self.Text.render( self.GameController.HighScores['['+str(self.ScoresPage+2)+'-'+str(score+1)+']'][0] , 1 , (255,255,255) )
			self.Screen.blit( tScoreText , ( self.Screen.get_width()  / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 180 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 25 * ( score + 3 ) ))
		
        # Draw Page Arrows
		self.Arrows[0].DrawButton( self.Screen )
		self.Arrows[1].DrawButton( self.Screen )
		
	def DrawPlayMenu( self ):
		# Draw Background
		self.Screen.blit( self.MenuBackgroundOverlay , ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2, self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 ))
		
		# Draw Buttons
		self.MenuButtons[4].DrawButtonWithText( self.Screen )	# Back Button
		self.MenuButtons[9].DrawButtonWithText( self.Screen )	# Play Button
		
		# Draw Text
		self.Screen.blit ( self.PlayTitleText , ( self.Screen.get_width()  / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 30 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 20 ))
		self.Screen.blit ( self.NumDisksText , ( self.Screen.get_width()  / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 30 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 70 ))
		tDiskCount = self.Text.render( str(self.NumDisks) , 1 , (255,255,255) )
		self.Screen.blit( tDiskCount , ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 95 - tDiskCount.get_width() / 2 , self.Screen.get_height() / 2 - 95 ))
		
		# Draw Disk
		self.Screen.blit( self.Disk , ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 77 , self.Screen.get_height() / 2 - 45 ))
		rect = pygame.Surface( ( self.Disk.get_width() , self.Disk.get_height() ) , pygame.SRCALPHA , 32 )
		rect.fill( self.Colors[self.ColorNum] )
		self.Screen.blit( rect , ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 77 , self.Screen.get_height() / 2 - 45 ),None,pygame.BLEND_RGB_MULT)
		
		# Draw Disk Arrows
		self.Arrows[2].DrawButton( self.Screen )
		self.Arrows[3].DrawButton( self.Screen )
		self.Arrows[4].DrawButton( self.Screen )
		self.Arrows[5].DrawButton( self.Screen )
		
	## Button Handlers
	def ButtonHandler( self , button ):
		self.MouseReleased = False
		if( button.ButtonId == 'Default'):
			self.GameController.ReadUserSettings(True)
			self.GameController.WriteUserSettings()
			self.GameController.InitializeWindow("TowersOfHanoi")
			self.InitializeButtons()
		elif( button.ButtonId == 'Save' ):
			self.GameController.WriteUserSettings()
			self.GameController.InitializeWindow("TowersOfHanoi")
			self.InitializeButtons()
		elif( button.ButtonId == 'Back' ):
			self.CurrentMenu = self.MenuStates[0]
		elif( button.ButtonId == 'Quit' ):
			self.StateQuit = True
		elif( button.ButtonId == 'Settings' ):
			self.CurrentMenu = self.MenuStates[1]
		elif( button.ButtonId == 'High Scores' ):
			self.CurrentMenu = self.MenuStates[2]
			self.GameController.RetrieveHighScores( False )
		elif( button.ButtonId == 'Play' ):
			self.CurrentMenu = self.MenuStates[3]
		elif( button.ButtonId == 'Start' ):
			self.GameController.StateMgr.AddState( 'PlayState' , PlayState.PlayState( self.Screen , self.GameController , self.NumDisks , self.Colors[self.ColorNum] ))
			self.GameController.StateMgr.SetState( 'PlayState' )
			pygame.mixer.music.stop()
		elif( button.ButtonId == 'Reset Scores' ):
			self.GameController.RetrieveHighScores( True )
			self.GameController.WriteHighScores()
			
	def SliderHandler( self , button ):
		tX , tY = pygame.mouse.get_pos()
		if( button.IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased ):
			self.StartSlider = button.ButtonId
			self.MouseReleased = False
		elif( self.StartSlider == button.ButtonId and pygame.mouse.get_pressed()[0] and not self.MouseReleased ):
			if( tX - self.Screen.get_width() / 2 <= 0 ):
				button.X = self.Screen.get_width() / 2 - 4
				self.GameController.UserSettings["["+button.ButtonId+"Volume]"] = 0
			elif( tX - self.Screen.get_width() / 2 >= 100 ):
				button.X = self.Screen.get_width() / 2 + 96
				self.GameController.UserSettings["["+button.ButtonId+"Volume]"] = 100
			else:
				button.X = tX - 4
				self.GameController.UserSettings["["+button.ButtonId+"Volume]"] = tX - self.Screen.get_width() / 2
		if(button.ButtonId == "Music"):
			pygame.mixer.music.set_volume( self.GameController.UserSettings["[MusicVolume]"] / 100.0 )
			
	def ArrowHandler( self , button ):
		self.MouseReleased = False
		if( button.ButtonId == 'ScoresLeft' ):
			self.ScoresPage -= 1
			if( self.ScoresPage < 1 ):
				self.ScoresPage = 1
		elif( button.ButtonId == 'ScoresRight' ):
			self.ScoresPage += 1
			if( self.ScoresPage > 6 ):
				self.ScoresPage = 6
		elif( button.ButtonId == 'DisksLeft' ):
			self.NumDisks -= 1
			if( self.NumDisks < 3 ):
				self.NumDisks = 3
		elif( button.ButtonId == 'DisksRight' ):
			self.NumDisks += 1
			if( self.NumDisks > 8 ):
				self.NumDisks = 8
		elif( button.ButtonId == 'DiskColorLeft' ):
			self.ColorNum -= 1
			if( self.ColorNum < 0 ):
				self.ColorNum = len(self.Colors)-1
		elif( button.ButtonId == 'DiskColorRight' ):
			self.ColorNum += 1
			if( self.ColorNum >= len(self.Colors) ):
				self.ColorNum = 0
			