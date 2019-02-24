from level1 import Minesweeper
from Tkinter import *
import tkMessageBox
import random


class Minesweeper3(Minesweeper):
	def __init__(self,master):
                  #Takes image files from the folder
		self.tile_plain=PhotoImage(file="tile_plain.gif")
		self.tile_clicked=PhotoImage(file="tile_clicked.gif")
		self.tile_mine=PhotoImage(file="tile_mine.gif")
		self.tile_flag=PhotoImage(file="tile_flag.gif")
		self.tile_wrong=PhotoImage(file="tile_wrong.gif")
		self.tile_no=[]

		for x in range(1,9):
			self.tile_no.append(PhotoImage(file="tile_"+str(x)+".gif"))
		 #creates a frame
		self.frame=Frame(master)
		self.frame.grid()
		
		self.label1=Label(self.frame,text="Minesweeper")
		self.label1.grid(row=0,column=0,columnspan=30)
		
		
		self.flags=0
		self.correct_flags=0
		self.clicked=0

		self.buttons={}
		self.mines=0
		x_cord=1
		y_cord=0

		for x in range(480):
			mine=0
			image_p=self.tile_plain
			if (random.uniform(0,1)<0.2):      #computer chooses no.of mines randomly
				mine=1
				self.mines=self.mines+1
			#0:button
			#1:wether mine present(1:present,0:not present)
			#2:state(0:unclicked,1:clicked;2:flagged)
			#3:button number
			#4:coordinates
			#5:nearby mines
			self.buttons[x]=[Button(self.frame,image=image_p),mine,0,x,[x_cord,y_cord],0]
			self.buttons[x][0].bind("<Button-1>",self.lclick3(x))
			self.buttons[x][0].bind("<Button-3>",self.rclick3(x))

			y_cord=y_cord+1;
			if(y_cord==30):
				y_cord=0
				x_cord=x_cord+1

		for keys in self.buttons:
			self.buttons[keys][0].grid(row=self.buttons[keys][4][0],column=self.buttons[keys][4][1])
                 #checks no.of mines near a tile
		for keys in self.buttons:
			x_crd=self.buttons[keys][4][0]
			y_crd=self.buttons[keys][4][1]
			self.near_mines=0
			if(keys==0):               #Different for boundary tiles as no.of tiles surrounding it are different.
				if (self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys+30)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys+31)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(keys==29):
				if (self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys+30)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys+29)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(keys==464):
				if (self.check_mines(keys-30)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys-29)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(keys==479):
				if (self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys-30)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys-31)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(x_crd==1):
				if(self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+29)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+30)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+31)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(y_crd==0):
				if(self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-30)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-29)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+30)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+31)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(x_crd==16):
				if(self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-30)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-29)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-31)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(y_crd==29):
				if(self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+30)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+29)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-30)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-31)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			else:
				if(self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+29)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+30)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+31)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-31)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-30)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-29)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
                 #creates two labels which shows the the no.of mines in the game and no.of flags you can still plant.
		self.label2=Label(self.frame,text="Mines: "+str(self.mines))
		self.label2.grid(row=17,column=0,columnspan=15)
		self.label3=Label(self.frame,text="Flags: "+str(self.flags))
		self.label3.grid(row=17,column=15,columnspan=15)
	
	def lclick3(self,keys):
		return lambda Button: self.l_click3(self.buttons[keys])
	
	def rclick3(self,keys):
		return lambda Button: self.r_click3(self.buttons[keys])
	 #open the tile if we left click on it.
	def l_click3(self,button):
			if(button[1]==1):
				for keys in self.buttons:
					if (self.buttons[keys][1]!=1 and self.buttons[keys][2]==2):
						self.buttons[keys][0].configure(image=self.tile_wrong)
					if (self.buttons[keys][1]==1 and self.buttons[keys][2]!=2):
						self.buttons[keys][0].configure(image=self.tile_mine)
				self.end()
			else:
				if (button[5]==0):
					button[0].configure(image=self.tile_clicked)
					self.cln_emp_tile3(button[3])
				else:
					button[0].configure(image=self.tile_no[button[5]-1])
				if (button[2]!=1):
					button[2]=1
					self.clicked=self.clicked+1
				if (self.clicked==480-self.mines):
					self.win()
	 #plants flag if once right clicked and removes it if clicked once again.
	def r_click3(self,button):
		if (button[2]==0):
			button[0].configure(image=self.tile_flag)
			button[2]=2
			button[0].unbind("<Button-1>")
			self.flags=self.flags+1
			self.update_flag()
		elif (button[2]==2):
			button[0].configure(image=self.tile_plain)
			button[2]=0
			button[0].bind("<Button-1>",self.lclick3(button[3]))
			self.flags=self.flags-1
			self.update_flag()
	#This function opens all the empty tiles near a tile.
	def cln_emp_tile3(self,button_num):

			button_list=[button_num]
			while (len(button_list)!=0):
				keys=button_list.pop()
				x_crd=self.buttons[keys][4][0]
				y_crd=self.buttons[keys][4][1]			
				if (keys==0):
					self.check(keys+1,button_list)
					self.check(keys+31,button_list)
					self.check(keys+30,button_list)				
				elif(keys==29):
					self.check(keys-1,button_list)
					self.check(keys+29,button_list)
					self.check(keys+30,button_list)
				elif(keys==464):
					self.check(keys-29,button_list)
					self.check(keys-30,button_list)
					self.check(keys+1,button_list)
				elif(keys==479):
					self.check(keys-31,button_list)
					self.check(keys-30,button_list)
					self.check(keys-1,button_list)
				elif(x_crd==1):
					self.check(keys-1,button_list)
					self.check(keys+1,button_list)
					self.check(keys+29,button_list)
					self.check(keys+30,button_list)
					self.check(keys+31,button_list)
				elif(y_crd==0):
					self.check(keys-30,button_list)
					self.check(keys-29,button_list)
					self.check(keys+1,button_list)
					self.check(keys+30,button_list)
					self.check(keys+31,button_list)
				elif(x_crd==16):
					self.check(keys-29,button_list)
					self.check(keys-30,button_list)
					self.check(keys-31,button_list)
					self.check(keys-1,button_list)
					self.check(keys+1,button_list)
				elif(y_crd==29):
					self.check(keys-30,button_list)
					self.check(keys-31,button_list)
					self.check(keys-1,button_list)
					self.check(keys+29,button_list)
					self.check(keys+30,button_list)
				else:
					self.check(keys-29,button_list)
					self.check(keys-30,button_list)
					self.check(keys-31,button_list)
					self.check(keys-1,button_list)
					self.check(keys+1,button_list)
					self.check(keys+29,button_list)
					self.check(keys+30,button_list)
	
