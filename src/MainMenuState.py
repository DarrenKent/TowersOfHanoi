#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	MainMenuState.py
#	This Class Handles The Main Menu Screen
#
#----------------------------------

import os
import pygame
from State import *

class MainMenuState(State):
	def __init__(self,screen,gamecontroller):
		State.__init__(self)
		self.Screen = screen
		self.MenuStates = [ 'MainMenu' , 'SettingsMenu' , 'HighScores' , 'PlayMenu' ]
		self.CurrentMenu = self.MenuStates[0]
		self.MouseReleased = True
		self.GameController = gamecontroller
		
		#Load Button Images
		QuitButton = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_quit_standard.png'))
		QuitButtonHover = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_quit_hover.png'))
		SettingsButton = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_settings_standard.png'))
		SettingsButtonHover = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_settings_hover.png'))
		HighScoresButton = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_highscores_standard.png'))
		HighScoresButtonHover = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_highscores_hover.png'))
		PlayButton = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_play_standard.png'))
		PlayButtonHover = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_play_hover.png'))
		BackButton = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_back_standard.png'))
		BackButtonHover = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_back_hover.png'))
		SaveButton = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_save_standard.png'))
		SaveButtonHover = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_save_hover.png'))
		
		#Load Background Images
		self.Background = pygame.image.load(os.path.join(os.path.join('data','textures'),'jungle_background.png'))
		self.LeftOverlay = pygame.image.load(os.path.join(os.path.join('data','textures'),'jungle_left.png'))
		self.RightOverlay = pygame.image.load(os.path.join(os.path.join('data','textures'),'jungle_right.png'))
		self.MenuBackgroundOverlay = pygame.image.load(os.path.join(os.path.join('data','textures'),'background_overlay.png'))
		
		self.CheckBoxEmpty = pygame.image.load(os.path.join(os.path.join('data','textures'),'checkbox_unchecked.png'))
		self.CheckBoxChecked = pygame.image.load(os.path.join(os.path.join('data','textures'),'checkbox_checked.png'))
		self.Text = pygame.font.SysFont("times",24,True,False)
		self.FullScreen = self.Text.render("Fullscreen:",1,(255,255,255))
		
		self.MenuButtons = [
							['quit',False,QuitButton,QuitButtonHover,self.QuitHandler],
							['settings',False,SettingsButton,SettingsButtonHover,self.SettingsHandler],
							['highscores',False,HighScoresButton,HighScoresButtonHover,self.HighScoresHandler],
							['play',False,PlayButton,PlayButtonHover,self.PlayHandler],
							['back',False,BackButton,BackButtonHover,self.BackHandler],
							['save',False,SaveButton,SaveButtonHover,self.SaveHandler]]
		
	def ExecuteStateLogic(self,KeysHeld,KeysPressed,clock):
		# Reset Mouse
		if(not pygame.mouse.get_pressed()[0]):
			self.MouseReleased = True
		
		# Execute Proper Menu Logic
		if(self.CurrentMenu == self.MenuStates[0]):
			self.ExecuteMainMenu()
		elif(self.CurrentMenu == self.MenuStates[1]):
			self.ExecuteSettingsMenu()
		elif(self.CurrentMenu == self.MenuStates[2]):
			self.ExecuteHighScores()
		elif(self.CurrentMenu == self.MenuStates[3]):
			self.ExecutePlayMenu()
						
	def DrawStateFrame(self,screen,clock):
		screen.fill((0,253,251))
		
		# Draw Background
		for tile in range(1 + screen.get_width() / self.Background.get_width()):
			screen.blit(self.Background,(tile * self.Background.get_width(), screen.get_height() - self.Background.get_height()))
		screen.blit(self.LeftOverlay,(0, screen.get_height() - self.LeftOverlay.get_height()))
		screen.blit(self.RightOverlay,(screen.get_width() - self.RightOverlay.get_width(), screen.get_height() - self.RightOverlay.get_height()))
		
		if(self.CurrentMenu == self.MenuStates[0]):
			self.DrawMainMenu()
		elif(self.CurrentMenu == self.MenuStates[1]):
			self.DrawSettingsMenu()
		elif(self.CurrentMenu == self.MenuStates[2]):
			self.DrawHighScores()
		elif(self.CurrentMenu == self.MenuStates[3]):
			self.DrawPlayMenu()
		
	def ExecuteMainMenu(self):
		# Buttons
		x,y = pygame.mouse.get_pos()
		leftMargin = self.Screen.get_width() / 2 - self.MenuButtons[1][2].get_width() / 2
		rightMargin = self.Screen.get_width() / 2 + self.MenuButtons[1][2].get_width() / 2
		for buttonNum in range(len(self.MenuButtons)):
			self.MenuButtons[buttonNum][1] = False
			
			if( x > leftMargin and x < rightMargin):
				if( y > self.Screen.get_height() - self.MenuButtons[buttonNum][2].get_height() * ( 2 + buttonNum) - ( buttonNum * 10) and y < self.Screen.get_height() - self.MenuButtons[buttonNum][2].get_height() * ( 1 + buttonNum) - ( buttonNum * 10)):
					self.MenuButtons[buttonNum][1] = True
					if( pygame.mouse.get_pressed()[0] and self.MouseReleased):
						self.MenuButtons[buttonNum][4]()
						self.MouseReleased = False
		
	def ExecuteSettingsMenu(self):
		#Buttons
		x,y = pygame.mouse.get_pos()
		self.MenuButtons[4][1] = False
		self.MenuButtons[5][1] = False
		
		# Back Button
		if( x > self.Screen.get_width() / 2 - self.MenuButtons[4][2].get_width() / 2 and x < self.Screen.get_width() / 2 + self.MenuButtons[4][2].get_width() / 2):
			if( y > self.Screen.get_height() /2  + self.MenuBackgroundOverlay.get_height() / 2 + 10 and y < self.Screen.get_height() /2  + self.MenuBackgroundOverlay.get_height() / 2 + self.MenuButtons[4][2].get_height() + 10):
				self.MenuButtons[4][1] = True
				if( pygame.mouse.get_pressed()[0] and self.MouseReleased):
					self.MenuButtons[4][4]()
					self.MouseReleased = False
		
		# FullScreen Checkbox
		if( x > self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + self.FullScreen.get_width() + 30 and x < self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + self.FullScreen.get_width() + 30 + self.CheckBoxEmpty.get_width()):
			if( y > self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 15 and y < self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 15 + self.CheckBoxEmpty.get_height()):
				if( pygame.mouse.get_pressed()[0] and self.MouseReleased):
					self.MouseReleased = False
					if( self.GameController.UserSettings["[Fullscreen]"] == 1 ):
						self.GameController.UserSettings["[Fullscreen]"] = 0
					else:
						self.GameController.UserSettings["[Fullscreen]"] = 1
						
		# Save Button
		if( x > self.Screen.get_width() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - self.MenuButtons[5][3].get_width() - 10 and x < self.Screen.get_width() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - 10):
			if( y > self.Screen.get_height() /2  + self.MenuBackgroundOverlay.get_height() / 2 - self.MenuButtons[5][3].get_height() - 10 and y < self.Screen.get_height() /2  + self.MenuBackgroundOverlay.get_height() / 2 - 10):
				self.MenuButtons[5][1] = True
				if( pygame.mouse.get_pressed()[0] and self.MouseReleased):
					self.MouseReleased = False
					self.MenuButtons[4][4]()
					self.MenuButtons[5][4]()
					
	def ExecuteHighScores(self):
		pass
		
	def ExecutePlayMenu(self):
		pass
		
	def DrawMainMenu(self):
		# Draw Buttons
		for button in range(4):
			if(self.MenuButtons[button][1]):
				self.Screen.blit(self.MenuButtons[button][3],(self.Screen.get_width() / 2 - self.MenuButtons[button][3].get_width() / 2, self.Screen.get_height() - self.MenuButtons[button][3].get_height() * (2 + button) - (button * 10) ))
			else:
				self.Screen.blit(self.MenuButtons[button][2],(self.Screen.get_width() / 2 - self.MenuButtons[button][2].get_width() / 2, self.Screen.get_height() - self.MenuButtons[button][2].get_height() * (2 + button) - (button * 10) ))
		
	def DrawSettingsMenu(self):
		# Draw Background
		self.Screen.blit(self.MenuBackgroundOverlay,( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2, self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 ))
		
		# Draw Save Button
		if(self.MenuButtons[5][1]):
			self.Screen.blit(self.MenuButtons[5][3],(self.Screen.get_width() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - self.MenuButtons[5][3].get_width() - 10, self.Screen.get_height() /2  + self.MenuBackgroundOverlay.get_height() / 2 - self.MenuButtons[5][3].get_height() - 10 ))
		else:
			self.Screen.blit(self.MenuButtons[5][2],(self.Screen.get_width() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - self.MenuButtons[5][2].get_width() - 10, self.Screen.get_height() /2  + self.MenuBackgroundOverlay.get_height() / 2 - self.MenuButtons[5][2].get_height() - 10 ))
					
		# Draw Back Button
		if(self.MenuButtons[4][1]):
			self.Screen.blit(self.MenuButtons[4][3],(self.Screen.get_width() / 2 - self.MenuButtons[4][3].get_width() / 2, self.Screen.get_height() /2  + self.MenuBackgroundOverlay.get_height() / 2 + 10 ))
		else:
			self.Screen.blit(self.MenuButtons[4][2],(self.Screen.get_width() / 2 - self.MenuButtons[4][2].get_width() / 2, self.Screen.get_height() /2  + self.MenuBackgroundOverlay.get_height() / 2 + 10 ))
			
		# Draw Fullscreen
		fullScreen = self.Text.render("Fullscreen:",1,(255,255,255))
		self.Screen.blit(fullScreen, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 20, self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 10 ))
		if(self.GameController.UserSettings["[Fullscreen]"] == 1):
			self.Screen.blit(self.CheckBoxChecked, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + self.FullScreen.get_width() + 30, self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 15 ))
		else:
			self.Screen.blit(self.CheckBoxEmpty, ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + self.FullScreen.get_width() + 30, self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 + 15 ))
		
	def DrawHighScores(self):
		pass
		
	def DrawPlayMenu(self):
		pass
		
	## Button Handlers
	def SaveHandler(self):
		self.GameController.WriteUserSettings()
		
	def BackHandler(self):
		self.CurrentMenu = self.MenuStates[0]
		
	def QuitHandler(self):
		self.StateQuit = True
	
	def SettingsHandler(self):
		self.CurrentMenu = self.MenuStates[1]
		
	def HighScoresHandler(self):
		self.CurrentMenu = self.MenuStates[2]
		
	def PlayHandler(self):
		self.CurrentMenu = self.MenuStates[3]
		