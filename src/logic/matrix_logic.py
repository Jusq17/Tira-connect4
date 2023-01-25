
import numpy as np
import pygame

class Logic():

    def __init__(self):

        self.rows = 6
        self.columns = 7
        self.board = np.zeros((self.rows, self.columns), dtype=int)

    def dropPiece(self, board, column, piece):

        for i in range(self.rows-1, -1, -1):

            if board[i, column] == 0:

                board[i, column] = piece
                return board, True

        if piece != 1:

            if board[0,column]:
                    
                self.dropPiece(board,column+1,piece)

        return board, False

    def clearBoard(self, board):

        board = np.zeros((self.rows, self.columns), dtype=int)

#logic = Logic()

#logic.dropPiece(logic.board, 1)
#logic.dropPiece(logic.board, 1)

#print(logic.board)

#print("fjiaajf")