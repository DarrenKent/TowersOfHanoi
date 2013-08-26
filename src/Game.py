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

from GameController import *
import StateManager

class TowersOfHanoi(GameController):
	def __init__(self):
		GameController.__init__(self,'Towers Of Hanoi')
		self.StateMgr = StateManager.StateManager(self.Screen,self)
		
	def GameLogic(self):		
		if(self.StateMgr.CurrentState == 'QuitState'):
			self.Active = False
		else:
			self.StateMgr.ExecuteCurrentStateLogic(self.KeyHeld,self.KeyPressed,self.Clock)
			
			if(self.StateMgr.CurrentState == 'SplashState' and self.StateMgr.GetCurrentState().StateQuit):
				self.StateMgr.SetState('MainMenuState')
			if(self.StateMgr.CurrentState == 'MainMenuState' and self.StateMgr.GetCurrentState().StateQuit):
				self.StateMgr.SetState('QuitState')
			
			
		
		
	def DrawScreen(self):
		self.StateMgr.DrawCurrentState(self.Screen,self.Clock)
		