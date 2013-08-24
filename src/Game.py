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
		self.StateMgr = StateManager.StateManager()
		
	def GameLogic(self):
		#if pygame.K_ESCAPE in self.KeyPressed:
		#	self.Active = False
		self.StateMgr.ExecuteCurrentStateLogic(self.KeyHeld,self.KeyPressed,self.Clock)
		
	def DrawScreen(self):
		self.Screen.fill((0,0,0))
		self.StateMgr.DrawCurrentState(self.Screen,self.Clock)
		