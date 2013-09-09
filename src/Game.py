#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	Game.py
#	This Class Handles A more Advanced Version
#	of the Game Controller
#
#----------------------------------

# Imports
from GameController import *
import StateManager

class TowersOfHanoi( GameController ):
	def __init__( self ):
		GameController.__init__( self , 'Towers Of Hanoi')
		self.StateMgr = StateManager.StateManager( self.Screen , self)
		self.HighScores = {}
		
	def GameLogic( self ):
		if( self.StateMgr.CurrentState == 'QuitState' ):
			self.Active = False
		else:
			self.StateMgr.ExecuteCurrentStateLogic( self.KeyHeld , self.KeyPressed , self.Clock )
			
			if( self.StateMgr.CurrentState == 'SplashState' and self.StateMgr.GetCurrentState().StateQuit ):
				self.StateMgr.SetState( 'MainMenuState' )
			if( self.StateMgr.CurrentState == 'MainMenuState' and self.StateMgr.GetCurrentState().StateQuit ):
				self.StateMgr.SetState( 'QuitState' )
			if( self.StateMgr.CurrentState == 'PlayState' and self.StateMgr.GetCurrentState().StateQuit ):
				self.StateMgr.SetState( 'MainMenuState' )
			
	def DrawScreen( self ):
		self.StateMgr.DrawCurrentState( self.Screen , self.Clock )
		
	def RetrieveHighScores( self , reset ):
		# Clear current High Scores
		self.HighScores = {}

		# Open Correct Settings
		if not reset:
			file = open( 'user/pscores.cfg' , 'r' )
		else:
			file = open( 'src/dscores.cfg' , 'r' )
			
		# Read through each line and store the settings
		line = file.readline()
		while( line ):
			if line == '':
				break

			scores = line.split()
			score = scores[1]
			name = ""
			if( len( scores ) > 2 ):
				name = scores[2]
			self.HighScores[scores[0]] = ( score , name )
			line = file.readline()
			
		file.close()