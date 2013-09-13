#----------------------------------
#
#	Towers of Hanoi
#	By: Darren Kent
#
#	PlayState.py
#	This Class Handles The GamePlay
#
#----------------------------------

import os
import pygame
import time
from State import *
import Button
import Disk


class PlayState( State ):
	def __init__( self , screen , gameController , numDisks ):
		State.__init__( self )
		self.Screen = screen
		self.NumDisks = numDisks
		self.GameController = gameController
		self.Texture = 'jungle'
		self.Pause = False
		self.Countdown = True
		self.StartTime = time.time()
		self.StartPause = 0
		self.TimePaused = 0
		self.Towers = [0,0,0]
		self.TowersList = [[],[],[]]
		self.Disks = []
		self.WinTime = 0
		self.Win = False
		for disk in range( numDisks ):
			tNewDisk = Disk.Disk( disk , numDisks - disk , 0 , "disk_"+str(disk+1)+"_red.png" , screen , self.DiskHandler )
			self.Disks.append( tNewDisk )
			self.Towers[0] += 1
			self.TowersList[0].append(disk)
		self.SelectedDisk = None
		
		# Initialize Background Images
		self.Background = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , self.Texture+'_background.png' ))
		self.LeftOverlay = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , self.Texture+'_left.png' ))
		self.LeftForground = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , self.Texture+'_left_forground.png' ))
		self.RightOverlay = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , self.Texture+'_right.png' ))
		self.RightForground = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , self.Texture+'_right_forground.png' ))
		self.Stage = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , self.Texture+'_stage.png' ))
		self.MenuBackgroundOverlay = pygame.image.load( os.path.join( os.path.join( 'data' , 'textures' ) , 'background_overlay.png' ))
		self.Text = pygame.font.SysFont( "times", 24 , True , False )
		
		self.InitializeButtons()
		
	def InitializeButtons( self ):
		self.Buttons = []
		self.Buttons.append( Button.Button( self.Screen.get_width() - 160 , 10 , 'Menu' , 'button_menu_standard.png' , 'button_menu_hover.png' , self.ButtonHandler ))
		self.Buttons.append( Button.Button( self.Screen.get_width() / 2 - 75 , self.Screen.get_height() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - 60 , 'Resume' , 'button_back_standard.png' , 'button_back_hover.png' , self.ButtonHandler ))
		self.Buttons.append( Button.Button( self.Screen.get_width() / 2 - 75 , self.Screen.get_height() / 2 + self.MenuBackgroundOverlay.get_width() / 2 - 180 , 'Quit' , 'button_quit_standard.png' , 'button_quit_hover.png' , self.ButtonHandler ))
		
	def ExecuteStateLogic( self , KeysHeld , KeysPressed , clock ):
		if( not pygame.mouse.get_pressed()[0] and self.SelectedDisk ):
			self.SelectedDisk.SetLocation( self.Towers , self.TowersList )
		if( not pygame.mouse.get_pressed()[0] ):
			self.MouseReleased = True
			self.SelectedDisk = None
			
		if( self.Countdown ):
			self.ExecuteCountdown()
		elif( self.Win ):
			self.ExecuteWin()
		elif( self.Pause ):
			self.ExecutePauseMenuLogic()
		else:
			self.ExecuteGameLogic()
			
	def ExecuteGameLogic( self ):
		self.Towers = [0,0,0]
		self.TowersList = [[],[],[]]
		tX , tY = pygame.mouse.get_pos()
		self.Buttons[0].SetMouseHover( tX , tY )
		for disk in self.Disks:
			disk.SetMouseHover( tX , tY )
			self.Towers[disk.Column] += 1
			self.TowersList[disk.Column].append(disk.ButtonId)
			
		if( self.Buttons[0].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased ):
			self.Buttons[0].ExecuteButton()
		
		for disk in self.Disks:
			disk.ExecuteButton()
			
		self.CheckForWin()
		
			
	def ExecutePauseMenuLogic( self ):
		tX , tY = pygame.mouse.get_pos()
		self.Buttons[1].SetMouseHover( tX , tY )
		self.Buttons[2].SetMouseHover( tX , tY )
		if( self.Buttons[1].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased ):
			self.Buttons[1].ExecuteButton()
		if( self.Buttons[2].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased ):
			self.Buttons[2].ExecuteButton()
		
	def ExecuteCountdown( self ):
		self.Countdown = False
		
	def ExecuteWin( self ):
		tX , tY = pygame.mouse.get_pos()
		self.Buttons[2].SetMouseHover( tX , tY )
		if( self.Buttons[2].IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased ):
			self.Buttons[2].ExecuteButton()
			
	def CheckForWin( self ):
		if( self.Towers[2] == self.NumDisks ):
			self.WinTime = time.time() - self.StartTime - self.TimePaused
			self.Win = True
			self.GameController.RetrieveHighScores( False )
			tAddScore = False
			tLastScore = 0
			tLastPlayer = 0
			for score in range( 10 ):
				tScore = self.GameController.HighScores["["+str(self.NumDisks)+"-"+str(score+1)+"]"]
				tScoreValue = eval(tScore[0])
				if( not tAddScore and ((tScoreValue != 0 and self.WinTime < tScoreValue) or tScoreValue == 0) ):
					print "working"
					tAddScore = True
					tLastScore = str(self.WinTime)
					tLastPlayer = "ABC"
				if( tAddScore ):
					tThisScore = tLastScore
					tThisPlayer = tLastPlayer
					tLastScore = tScore[0]
					tLastPlayer = tScore[1]
					tNewScore = (tThisScore,tThisPlayer)
					self.GameController.HighScores["["+str(self.NumDisks)+"-"+str(score+1)+"]"] = tNewScore
			if( tAddScore):
				self.GameController.WriteHighScores()

	def DrawStateFrame( self , screen , clock ):
		screen.fill( (0,253,251) )
		
		# Draw Background
		for tile in range( 1 + screen.get_width() / self.Background.get_width() ):
			screen.blit( self.Background , ( tile * self.Background.get_width() , screen.get_height() - self.Background.get_height() ))
		screen.blit( self.LeftOverlay , ( 0 , screen.get_height() - self.LeftOverlay.get_height() ))
		screen.blit( self.RightOverlay , ( screen.get_width() - self.RightOverlay.get_width() , screen.get_height() - self.RightOverlay.get_height() ))
		screen.blit( self.Stage , ( screen.get_width() / 2 - self.Stage.get_width() / 2 , screen.get_height() - self.Stage.get_height() ))
		screen.blit( self.LeftForground , ( 0 , screen.get_height() - self.LeftForground.get_height() ))
		screen.blit( self.RightForground , ( screen.get_width() - self.RightForground.get_width() , screen.get_height() - self.RightForground.get_height() ))
		
		self.Buttons[0].DrawButton( self.Screen )
		
		for disk in self.Disks:
			disk.DrawButton()
			
		if( self.Win ):
			self.DrawWin()
		elif( self.Pause ):
			self.DrawPauseMenu()
			timer = self.Text.render( "PAUSED" , 1 , (255,255,255) )
			self.Screen.blit( timer , ( 10 , 10) )
		else:
			timer = self.Text.render( "Time: %.2f" % (time.time() - self.StartTime - self.TimePaused) , 1 , (255,255,255) )
			self.Screen.blit( timer , ( 10 , 10) ) 
			
		
			
	def DrawPauseMenu( self ):
		rect = pygame.Surface( ( self.Screen.get_width() , self.Screen.get_height() ) , pygame.SRCALPHA , 32 )
		rect.fill( (0,0,0,200) )
		self.Screen.blit( rect , (0,0) )
		self.Screen.blit( self.MenuBackgroundOverlay , ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 ))
		self.Buttons[1].DrawButton( self.Screen )
		self.Buttons[2].DrawButton( self.Screen )
		
	def DrawWin( self ):
		rect = pygame.Surface( ( self.Screen.get_width() , self.Screen.get_height() ) , pygame.SRCALPHA , 32 )
		rect.fill( (0,0,0,200) )
		self.Screen.blit( rect , (0,0) )
		self.Screen.blit( self.MenuBackgroundOverlay , ( self.Screen.get_width() / 2 - self.MenuBackgroundOverlay.get_width() / 2 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_height() / 2 ))
		
		winText = self.Text.render( "Congratulations, You Win!" , 1 , (255,255,255) )
		winTimeText = self.Text.render( "Time: %.2f" % self.WinTime , 1 , (255,255,255) )
		self.Screen.blit( winText , ( self.Screen.get_width() / 2 - winText.get_width() / 2 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 20 ))
		self.Screen.blit( winTimeText , ( self.Screen.get_width() / 2 - winTimeText.get_width() / 2 , self.Screen.get_height() / 2 - self.MenuBackgroundOverlay.get_width() / 2 + 60 ))
		self.Buttons[2].DrawButton( self.Screen )
		
	def ButtonHandler( self , button ):
		self.MouseReleased = False
		if( button.ButtonId == 'Menu' ):
			self.Pause = True
			self.StartPause = time.time()
		elif( button.ButtonId == 'Resume' ):
			self.Pause = False
			self.TimePaused += time.time() - self.StartPause
		elif( button.ButtonId == 'Quit' ):
			self.StateQuit = True
			
	def DiskHandler( self , disk ):
		tX , tY = pygame.mouse.get_pos()
		if( disk.IsMouseInside() and pygame.mouse.get_pressed()[0] and self.MouseReleased and (disk.ButtonId) == min(self.TowersList[disk.Column]) ):
			self.SelectedDisk = disk
			self.MouseReleased = False
			disk.MouseXDist = tX - disk.X
			disk.MouseYDist = tY - disk.Y
		elif( disk == self.SelectedDisk and not self.MouseReleased ):
			disk.NewX = tX - disk.MouseXDist
			disk.NewY = tY - disk.MouseYDist