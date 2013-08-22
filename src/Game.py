#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	Game.py
#	This Class Handles Primary Game Loop and Functions
#
#----------------------------------

class GameController:
	def __init__(self):
		# Read in User Settings
		self.UserSettings = []
		self.ReadUserSettings(False)
		
	def ReadUserSettings(self, reset):
		if not reset:
			file = open("user/user.cfg","r")
		else
			file = open("default.cfg","r")
		line = file.readline()
		while(line):
			if line == "":
				break
			setting = line.split()
			self.UserSettings.append([setting[0],setting[1]])
			line = file.readline()
		file.close()
			
	def WriteUserSettings(self):
		file = open("user/user.cfg","r")
		for setting in self.UserSettings:
			file.write(setting[0] + " " + setting[1])
		file.close()
		
	def Run(self):
		return
		
		