'''
assignment: programming assignment 5 - fifteen.py
author: Lucais Sanderson
date: June 2, 2022
file: fifteen.py creates the bones for the fifteen puzzle game. 
input: takes user input of tile number to move. 
output: prints the tile board in terminal. 
'''

import numpy as np
from random import choice

class Fifteen:
    
    def __init__(self, size = 4):
        # creates 1d array as the tile board
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        self.nummoves = 0

    def update(self, i, j=0):
        # checks that the move is possible
        # if yes, compute the transpose and update the tile board
        if self.is_valid_move(i, j):
            self.tiles = self.transpose(i, j)
        # if no, return False
        else:
            return False
        
    def transpose(self, i, j):
        # creates local instance of tile board
        tiles = self.tiles
        # records indices of both tiles
        index1 = np.where(tiles == i)
        index2 = np.where(tiles == j)
        # records their value
        entry1 = tiles[index1]
        entry2 = tiles[index2]
        # swaps their values
        tiles[index1] = entry2
        tiles[index2] = entry1
        # returns the transposed, local tile board
        return tiles

    def shuffle(self, steps=100):
        # creates local instance of tile board,
        # as a reshaped 4x4 matrix
        tiles = self.tiles.reshape(4,4)
        # all possible moves
        allmoves = ['up', 'down', 'left', 'right']
        move = None
        # for amount of desired steps
        for i in range(steps):
            # chooses randomly from allmoves until
            # a choice that works is chosen. (ie not off of the board/out of index range)
            while True:
                move = choice(allmoves)
                if move == 'up':
                    if np.where(tiles == 0)[0] + 1 <= 3:
                        move = (np.where(tiles == 0)[0] + 1, np.where(tiles == 0)[1])
                        break
                elif move == 'down':
                    if np.where(tiles == 0)[0] - 1 >= 0:
                        move = (np.where(tiles == 0)[0] - 1, np.where(tiles == 0)[1])
                        break
                elif move == 'left':
                    if np.where(tiles == 0)[1] + 1 <= 3:
                        move = (np.where(tiles == 0)[0], np.where(tiles == 0)[1] + 1)
                        break
                elif move == 'right':
                    if np.where(tiles == 0)[1] - 1 >= 0:
                        move = (np.where(tiles == 0)[0], np.where(tiles == 0)[1] - 1)
                        break
            # updates the main tile board
            self.update(tiles[move], 0)
        
    def is_valid_move(self, i, j=0):
        # creates local instance of tile board as a 4x4 matrix
        tiles = self.tiles.reshape(4,4)
        # records the indices of each tile
        j_index = np.where(tiles == j)
        i_index = np.where(tiles == i)
        # checks if the move is adjecent to a row/column and 
        # within a unit of the column/row.
        if abs(j_index[0] - i_index[0]) == 1 and j_index[1] == i_index[1]:
            valid = True
        elif abs(j_index[1] - i_index[1]) == 1 and j_index[0] == i_index[0]:
            valid = True
        else:
            valid = False
        # if niether tile is a 0, then the move cannot be valid
        if i != 0 and j != 0:
            valid = False
        return valid


    def is_solved(self):
        # uses method of numpy 'array_qual' to 
        # check equality of the current tile board to the winning 
        # tile board.
        # returns bool (T/F)
        return np.array_equal(self.tiles.reshape(-1), [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15,  0])
        
    def draw(self):
        size = int(self.tiles.size**0.5)
        for i in range(size):
            print('\n+---+---+---+---+\n|',end='')
            for j in range(i*size, i*size+size):
                if self.tiles[j] != 0:
                    if len(str(self.tiles[j])) == 1:
                        print(f' {self.tiles[j]} |',end='')
                    else: 
                        print(f'{self.tiles[j]} |',end='')
                else:
                    print('   |',end='')
        print('\n+---+---+---+---+')    
        

        
    def __str__(self):
        '''
        s = ''
        size = int(self.tiles.size**0.5)
        for i in range(size):
            for j in range(i*size, i*size+size):
                if self.tiles[j] != 0:
                    if len(str(self.tiles[j])) == 1:
                        s += f' {self.tiles[j]} '
                    else: 
                        s += f'{self.tiles[j]} '
                else:
                    s += '   '
                
            s += '\n'
        return s
                '''
        print(f' {self.tiles[0]}  {self.tiles[1]}  {self.tiles[2]}  {self.tiles[3]} ')
        print(f' {self.tiles[4]}  {self.tiles[5]}  {self.tiles[6]}  {self.tiles[7]} ')
        print(f' {self.tiles[8]}  {self.tiles[9]}  {self.tiles[10]}  {self.tiles[11]} ')
        print(f' {self.tiles[12]}  {self.tiles[13]}  {self.tiles[14]}  {self.tiles[15]} ')

if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(0,15) == True
    assert game.is_valid_move(0,12) == True
    assert game.is_valid_move(14,15) == False
    assert game.is_valid_move(0,14) == False
    game.update(0, 15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(0, 15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    
    '''You should be able to play the game if you uncomment the code below'''

    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    
        
