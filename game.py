''' 
assignment: programming assignment 5 - game.py
author: Lucais Sanderson
date: June 3, 2022
file: game.py creates a 15 puzzle GUI and uses the bones from fifteen.py
to implement the game.
input: using tkinter, user clicks buttons in a window to move tiles or 
reset the board.
output: a GUI window is displayed. the tileboard is displayed as several buttons
on a grid. under the grid is a reset button. 
'''

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
import numpy as np


class Game():
    def __init__(self, gui):
        # initiate fifteen game and shuffle
        self.f = Fifteen()
        self.f.shuffle()
        # make frame for tiles and one for 
        # other widgets
        frame1 = Frame(gui)
        frame1.pack(side=TOP, padx=10, pady=10)
        frame2 = Frame(gui)
        frame2.pack(side=BOTTOM, pady=10, ipadx=5)
        # make buttons for tiles 
        button1 = self.addButton(frame1, '1')
        button2 = self.addButton(frame1, '2')
        button3 = self.addButton(frame1, '3')
        button4 = self.addButton(frame1, '4')
        button5 = self.addButton(frame1, '5')
        button6 = self.addButton(frame1, '6')
        button7 = self.addButton(frame1, '7')
        button8 = self.addButton(frame1, '8')
        button9 = self.addButton(frame1, '9')
        button10 = self.addButton(frame1, '10')
        button11 = self.addButton(frame1, '11')
        button12 = self.addButton(frame1, '12')
        button13 = self.addButton(frame1, '13')
        button14 = self.addButton(frame1, '14')
        button15 = self.addButton(frame1, '15')
        self.button_list = [button1, button2, button3, button4,
                       button5, button6, button7, button8,
                       button9, button10, button11, button12, 
                       button13, button14, button15]
        # make reset button
        resetButton = Button(frame2, text='Reset', command= lambda  : self.reset())
        resetButton.pack(side=RIGHT)
        # var for tracking moves 
        self.plays = 0
        self.plays_label = Label(frame2, text=f'Moves:\n{self.plays}')
        self.plays_label.pack(side=LEFT)
        # match board from fifteen.py
        self.arrangeGrid(None)

    # add button with simpler parameters
    def addButton(self, gui, value):
        return Button(gui, text=value, height=4, width=4, command= lambda :self.clickButton(gui, value))

    # function for a tile click 
    def clickButton(self, gui, value):
        self.arrangeGrid(value)
        
    # updates tkinter board
    def arrangeGrid(self, value):
        if value != None:
            # 
            self.f.update(int(value))
            if self.f.is_valid_move(int(value)):
                self.plays += 1
                self.plays_label.configure(text=f'Moves:\n{self.plays}')
        tiles = self.f.tiles.reshape(4,4)
        for button in self.button_list:
            index = np.where(tiles == int(button.cget('text')))
            button.grid(row=int(index[0]) , column=int(index[1]))


    def reset(self):
        self.f.shuffle()
        self.arrangeGrid(None)
        self.plays=0
        self.plays_label.configure(text=f'Moves:\n{self.plays}')
        


    
if __name__ == '__main__':    

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make a game object
    g = Game(gui)

    # update the window
    gui.mainloop()
    