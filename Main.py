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

def main():
	# Create Game Object and Start Game
	game = Game.TowersOfHanoi()
	game.Run()

# Call Main
if( __name__ == '__main__'):
	main()