#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	Main.py
#	Handles Program Initialization
#
#----------------------------------

# Imports
import sys
sys.path.insert(0,'src/')
import Game

''' Function: Main
	Creates an instance of the game and
	runs it.'''
def main():
	game = Game.TowersOfHanoi()
	game.Run()

# Call Main
if( __name__ == '__main__'):
	main()