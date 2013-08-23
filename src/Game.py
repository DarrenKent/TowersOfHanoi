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

class TowersOfHanoi(GameController):
	def __init__(self):
		GameController.__init__(self,"Towers Of Hanoi")
		
	def GameLogic(self):
		if pygame.K_ESCAPE in self.KeyPressed:
			self.Active = False
		
	def DrawScreen(self):
		return
		