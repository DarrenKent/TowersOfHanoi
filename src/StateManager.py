#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	StateManager.py
#	This Class handles the games current State
#
#----------------------------------

# Imports
import pygame
import SplashState
import MainMenuState

class StateManager:
	def __init__( self , screen , gamecontroller ):
		self.StateList = {}
		self.GameController = gamecontroller
		
		self.AddState( 'MainMenuState' , MainMenuState.MainMenuState( screen , gamecontroller ))
		self.AddState( 'SplashState' , SplashState.SplashState() )
		self.AddState( 'QuitState' , None )
		self.CurrentState = 'SplashState'
		
	def SetState( self , state ):
		self.CurrentState = state
		
	def ExecuteCurrentStateLogic( self , keysHeld , keysPressed , clock ):
		if( not self.StateList[self.CurrentState].StateQuit ):
			self.StateList[self.CurrentState].ExecuteStateLogic( keysHeld , keysPressed , clock )
		
		
	def DrawCurrentState( self , screen , clock ):
		if( self.CurrentState != 'QuitState' and not self.StateList[self.CurrentState].StateQuit ):
			self.StateList[self.CurrentState].DrawStateFrame( screen , clock )
		
	def AddState( self , StateName , State ):
		self.StateList[StateName] = State
		
	def GetCurrentState( self ):
		return self.StateList[self.CurrentState]