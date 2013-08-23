#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	GameController.py
#	This Class is a Base Class of the Game
#
#----------------------------------

import pygame
import pygame.locals

class GameController:
	def __init__(self,name):
		# Class Variables
		self.KeyHeld = set()
		self.KeyPressed = set()
		self.Active = True
		
		# Read in User Settings
		self.UserSettings = {}
		self.ReadUserSettings(True)
		
		# Initialize Window
		self.Screen = pygame.display.set_mode( (self.UserSettings["[ScreenWidth]"],self.UserSettings["[ScreenHeight]"]),
												pygame.locals.DOUBLEBUF | pygame.locals.SRCALPHA)
		pygame.display.set_caption(name)
		
	def ReadUserSettings(self, reset):
		# Clear current User Settings
		self.UserSettings = {}	

		# Open Correct Settings
		if not reset:
			file = open("user/user.cfg","r")
		else:
			file = open("src/default.cfg","r")
			
		# Read through each line and store the settings
		line = file.readline()
		while(line):
			if line == "":
				break
			setting = line.split()
			value = int(setting[1])
			self.UserSettings[setting[0]] = value
			line = file.readline()
			
		# Close the File
		file.close()
			
	def WriteUserSettings(self):
		# Open File to write
		file = open("user/user.cfg","r")
		
		# Read through each setting and save to file
		for setting in self.UserSettings:
			file.write(setting[0] + " " + setting[1])
			
		# Close File
		file.close()
	
	def GetKeyboardInput(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				self.Active = False
			if event.type == pygame.KEYDOWN:
				self.KeyHeld.add(event.key)
				self.KeyPressed.add(event.key)
			if event.type == pygame.KEYUP:
				self.KeyHeld.discard(event.key)
	
	def DrawScreen(self):
		raise NotImplementedError()
		
	def GameLogic(self):
		raise NotImplementedError()
	
	def Run(self):
		while(self.Active):
			# Reset Key Presses
			KeyPressed = set()
			
			# Get Keyboard Input
			self.GetKeyboardInput()
			
			# Calculate one Frame of Logic
			self.GameLogic()
			
			if(self.Active):
				# Draw One Frame
				self.DrawScreen()
				pygame.display.flip()