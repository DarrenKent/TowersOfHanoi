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
	def __init__(self,screen):
		State.__init__(self)
		self.Screen = screen
		
		#Load Button Images
		QuitButton = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_quit_standard.png'))
		QuitButtonHover = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_quit_hover.png'))
		SettingsButton = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_settings_standard.png'))
		SettingsButtonHover = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_settings_hover.png'))
		HighScoresButton = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_highscores_standard.png'))
		HighScoresButtonHover = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_highscores_hover.png'))
		PlayButton = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_play_standard.png'))
		PlayButtonHover = pygame.image.load(os.path.join(os.path.join('data','textures'),'button_play_hover.png'))
		
		#Load Background Images
		self.Background = pygame.image.load(os.path.join(os.path.join('data','textures'),'jungle_background.png'))
		self.LeftOverlay = pygame.image.load(os.path.join(os.path.join('data','textures'),'jungle_left.png'))
		self.RightOverlay = pygame.image.load(os.path.join(os.path.join('data','textures'),'jungle_right.png'))
		
		self.MenuButtons = [
							['quit',False,QuitButton,QuitButtonHover,self.QuitHandler],
							['settings',False,SettingsButton,SettingsButtonHover,self.SettingsHandler],
							['highscores',False,HighScoresButton,HighScoresButtonHover,self.HighScoresHandler],
							['play',False,PlayButton,PlayButtonHover,self.PlayHandler]]
		
	def ExecuteStateLogic(self,KeysHeld,KeysPressed,clock):
		# Buttons
		x,y = pygame.mouse.get_pos()
		leftMargin = self.Screen.get_width() / 2 - self.MenuButtons[1][2].get_width() / 2
		rightMargin = self.Screen.get_width() / 2 + self.MenuButtons[1][2].get_width() / 2
		for buttonNum in range(len(self.MenuButtons)):
			self.MenuButtons[buttonNum][1] = False
			
			if( x > leftMargin and x < rightMargin):
				if( y > self.Screen.get_height() - self.MenuButtons[buttonNum][2].get_height() * ( 2 + buttonNum) - ( buttonNum * 10) and y < self.Screen.get_height() - self.MenuButtons[buttonNum][2].get_height() * ( 1 + buttonNum) - ( buttonNum * 10)):
					self.MenuButtons[buttonNum][1] = True
					if( pygame.mouse.get_pressed()[0] ):
						self.MenuButtons[buttonNum][4]()
						
	def DrawStateFrame(self,screen,clock):
		screen.fill((0,253,251))
		
		# Draw Background
		for tile in range(1 + screen.get_width() / self.Background.get_width()):
			screen.blit(self.Background,(tile * self.Background.get_width(), screen.get_height() - self.Background.get_height()))
		screen.blit(self.LeftOverlay,(0, screen.get_height() - self.LeftOverlay.get_height()))
		screen.blit(self.RightOverlay,(screen.get_width() - self.RightOverlay.get_width(), screen.get_height() - self.RightOverlay.get_height()))
		
		# Draw Buttons
		for button in range(len(self.MenuButtons)):
			type = ''
			if(self.MenuButtons[button][1]):
				screen.blit(self.MenuButtons[button][3],(screen.get_width() / 2 - self.MenuButtons[button][2].get_width() / 2, screen.get_height() - self.MenuButtons[button][2].get_height() * (2 + button) - (button * 10) ))
			else:
				screen.blit(self.MenuButtons[button][2],(screen.get_width() / 2 - self.MenuButtons[button][2].get_width() / 2, screen.get_height() - self.MenuButtons[button][2].get_height() * (2 + button) - (button * 10) ))
				
	def QuitHandler(self):
		self.StateQuit = True
	
	def SettingsHandler(self):
		pass
		
	def HighScoresHandler(self):
		pass
		
	def PlayHandler(self):
		pass
		