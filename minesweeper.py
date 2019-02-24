from level1 import Minesweeper
from level2 import Minesweeper2
from Tkinter import *
import tkMessageBox
import random
import time

def instruction():
    tkMessageBox.showinfo("Instructions","The rules in Minesweeper are simple: Uncover a mine, and the game ends.Uncover an empty square, and you keep playing. Uncover a number, and it tells you how many mines lay hidden in the eight surrounding squares-information you use to deduce which nearby squares are safe to click.")
def starttime():
	tkMessageBox.showinfo("timer start as soon as you click ok")

class minesweeper(Minesweeper2,Minesweeper):  #This class shows the player the levels he can choose to play.
    def __init__(self,master):
        self.frame=Frame(root)
        self.frame.grid()
        self.buttons={}
        self.tile_plain=PhotoImage(file="tile_plain.gif")
        self.tile_clicked=PhotoImage(file="tile_clicked.gif")
        self.tile_mine=PhotoImage(file="tile_mine.gif")
        self.tile_flag=PhotoImage(file="tile_flag.gif")
        self.tile_wrong=PhotoImage(file="tile_wrong.gif")
        self.tile_no=[]

        for x in range(1,9):
            self.tile_no.append(PhotoImage(file="tile_"+str(x)+".gif"))

            
        self.label_minesweeper=Label(self.frame,text="Minesweeper")    #Displays Title of the game.
        self.label_minesweeper.grid(row=0,column=0,columnspan=9)
	
	
        self.level1_button=Button(self.frame,text="Easy")      #Displays level1 button.
        self.level1_button.grid(row=1,column=0,columnspan=3)
        self.level1_button.bind("<Button-1>",lambda Button:self.level1())

        self.level2_button=Button(self.frame,text="Hard")       #Displays level2 button.
        self.level2_button.grid(row=1,column=3,columnspan=3)
        self.level2_button.bind("<Button-1>",lambda Button:self.level2())


        self.Inst_button=Button(self.frame,text="Instruction",command = instruction)   #Displays Instructions button.
        self.Inst_button.grid(row=2,column=0,columnspan=9)
           
        self.Quit_button=Button(self.frame,text="Quit",command=self.Quit)       #Displays Quit button.
        self.Quit_button.grid(row=3,column=0,columnspan=9)
           

    def level1(self): #Forgets everything and opens 8 by 8 game 
        self.frame.grid_forget()
        self.label_minesweeper.grid_forget()
        self.level1_button.grid_forget()
        self.level2_button.grid_forget()
	
	self.startgame=Button(self.frame,command = instruction)   #Displays Instructions button.
        self.startgame.grid(row=2,column=0,columnspan=9)
                

	self.Quit_button.grid_forget()
        self.Inst_button.grid_forget()
        global root
        Minesweeper.__init__(self,root)
            
    def level2(self):         #Forgets everything and opens 16 by 16 game 

        self.frame.grid_forget()
        self.label_minesweeper.grid_forget()
        self.level1_button.grid_forget()
        self.level2_button.grid_forget()
        self.QUit_button.grid_forget()
        self.Inst_button.grid_forget()
        global root
        Minesweeper2.__init__(self,root)

    def Quit(self):
 	End=tkMessageBox.askquestion("Quit", "Are You Sure You Want To Exit ?")
        global root
        if(End== 'no'): #if player wants to play again then it returns to the main window or else it destroys the window.
            self.forgetframe()
            self.__init__(self)
        else:
                tkMessageBox.showinfo(":-)","Thanks for playing!!")         
                root.destroy()
            

     
    def end(self):
        lose=tkMessageBox.askquestion("Game over!", "You Lose! Do you want to play again?")
        global root
        if(lose == 'yes'): #if player wants to play again then it returns to the main window or else it destroys the window.
            self.forgetframe()
            self.__init__(self)
        else:
            sure1 = tkMessageBox.askquestion("Game over!","Are you sure you want to exit?")
            if(sure1 == 'yes'): 
                tkMessageBox.showinfo(":-)","Thanks for playing!!")         
                root.destroy()
            else:
                self.forgetframe()
                self.__init__(self)

    def win(self):
        win = tkMessageBox.askquestion("Game over!","You Won! Do you want to play again?")
        global root
        if(win == 'yes'):    #if player wants to play again then it returns to the main window or else it destroys the window.
            self.forgetframe()
            self.__init__(self)
        else:
            sure2 = tkMessageBox.askquestion("Game over!","Are you sure you want to exit?")
        if(sure2 =='yes'): 
            tkMessageBox.showinfo(":-)","Thanks for playing!!")        
            root.destroy()
        else:
            self.forgetframe()
            self.__init__(self)
            
    def update_flag(self):   # This function updates the flags count.
        self.label3.configure(text="Flags: "+str(self.flags))
     
if __name__=="__main__":
    global root
    root=Tk()
    mine=minesweeper(root)
    root.mainloop()




