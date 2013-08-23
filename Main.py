#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	Main.py
#	Handles Program Initialization
#
#----------------------------------

import sys
sys.path.insert(0,'src/')
import Game

def main():
	game = Game.TowersOfHanoi()
	game.Run()
	
if __name__ == '__main__':
	main()