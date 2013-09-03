#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	GameController.py
#	This Class is a Base Class of the Game
#
#----------------------------------

# Imports
import pygame
import pygame.locals

class GameController:
	def __init__( self , name ):
		# Class Variables
		self.KeyHeld = set()
		self.KeyPressed = set()
		self.Active = True
		self.Clock = pygame.time.Clock()
		
		# Read in User Settings
		self.UserSettings = {}
		self.ReadUserSettings( False )
		
		# Initialize Window
		self.Screen = None
		self.InitializeWindow( name )
		
		pygame.init()
		pygame.mixer.init()
	
	def InitializeWindow( self , name ):
		if( self.UserSettings['[Fullscreen]'] == 1 ):
			self.Screen = pygame.display.set_mode( ( self.UserSettings['[ScreenWidth]'] , self.UserSettings['[ScreenHeight]'] ),
												pygame.locals.DOUBLEBUF | pygame.locals.SRCALPHA | pygame.locals.FULLSCREEN )
		else:
			self.Screen = pygame.display.set_mode( ( self.UserSettings['[ScreenWidth]'] , self.UserSettings['[ScreenHeight]'] ),
												pygame.locals.DOUBLEBUF | pygame.locals.SRCALPHA )
			pygame.display.set_caption( name )
		
	
	def ReadUserSettings( self , reset ):
		# Clear current User Settings
		self.UserSettings = {}	

		# Open Correct Settings
		if not reset:
			file = open( 'user/user.cfg' , 'r' )
		else:
			file = open( 'src/default.cfg' , 'r' )
			
		# Read through each line and store the settings
		line = file.readline()
		while( line ):
			if line == '':
				break
			setting = line.split()
			self.UserSettings[setting[0]] = int( setting[1] )
			line = file.readline()
			
		file.close()
			
	def WriteUserSettings( self ):
		# Open File to write
		file = open( 'user/user.cfg' , 'w' )
		
		# Read through each setting and save to file
		for setting in self.UserSettings:
			file.write( setting + " " + str( self.UserSettings[setting] ) + "\n" )
			
		file.close()
	
	def GetKeyboardInput( self ):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				self.Active = False
			if event.type == pygame.KEYDOWN:
				self.KeyHeld.add( event.key )
				self.KeyPressed.add( event.key )
			if event.type == pygame.KEYUP:
				self.KeyHeld.discard( event.key )
	
	def DrawScreen( self ):
		raise NotImplementedError()
		
	def GameLogic( self ):
		raise NotImplementedError()
	
	def Run( self ):
		while( self.Active ):
			# Advance Time
			self.Clock.tick()
			
			# Reset Key Presses
			self.KeyPressed = set()
			
			# Get Keyboard Input
			self.GetKeyboardInput()
			
			# Calculate one Frame of Logic
			self.GameLogic()
			
			if( self.Active ):
				# Draw One Frame
				self.DrawScreen()
				pygame.display.flip()