#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	State.py
#	This Class is a Base Class for the States
#
#----------------------------------

class State:
	def __init__( self ):
		self.StateQuit = False
		
	def ExecuteStateLogic( self , KeysHeld , KeysPressed , clock ):
		raise NotImplementedError()
		
	def DrawStateFrame( self , screen , clock ):
		raise NotImplementedError()