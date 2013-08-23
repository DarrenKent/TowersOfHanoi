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
		
	def ExecuteCurrentStateLogic(self,KeysHeld,KeysPressed):
		if( not self.StateList[self.CurrentState].StateQuit):
			self.StateList[self.CurrentState].ExecuteStateLogic(KeysHeld,KeysPressed)
		#else:
			#if self.CurrentState = 'SplashState':
				#self.CurrentState = 'MainMenuState'
		
		
	def DrawCurrentState(self,screen):
		if( not self.StateList[self.CurrentState].StateQuit):
			self.StateList[self.CurrentState].DrawStateFrame(screen)
		
	def AddState(self,StateName,State):
		self.StateList[StateName] = State