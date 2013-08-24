#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	StateManager.py
#	This Class handles the games current State
#
#----------------------------------

import pygame
import SplashState

class StateManager:
	def __init__(self):
		self.StateList = {}
		
		self.AddState('SplashState',SplashState.SplashState())
		self.CurrentState = 'SplashState'
		
	def SetState(self,state):
		self.CurrentState = state
		
	def ExecuteCurrentStateLogic(self,keysHeld,keysPressed,clock):
		if( not self.StateList[self.CurrentState].StateQuit):
			self.StateList[self.CurrentState].ExecuteStateLogic(keysHeld,keysPressed,clock)
		#else:
			#if self.CurrentState = 'SplashState':
				#self.CurrentState = 'MainMenuState'
		
		
	def DrawCurrentState(self,screen,clock):
		if( not self.StateList[self.CurrentState].StateQuit):
			self.StateList[self.CurrentState].DrawStateFrame(screen,clock)
		
	def AddState(self,StateName,State):
		self.StateList[StateName] = State