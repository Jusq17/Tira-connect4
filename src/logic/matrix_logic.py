
import numpy as np
import pygame

class Logic():

    """
        Luokka, joka käsittelee kaiken pelimatriisiin liittyvän.
        Sisältää metodit, jotka muokkaavat ja tarkastavat sitä.

        Attributes:

        rows: rivien määrä laudassa
        cols: sarakkeiden määrä laudassa
        board: pelilauta

    """

    def __init__(self):

        self.rows = 6
        self.columns = 7
        self.board = np.zeros((self.rows, self.columns), dtype=int)

    def getValidColumns(self, board):

        """
            Metodi, joka etsii vapaat sarakkeet, joihin voidaan pelata palanen.

            Args:

                board: pelilauta

        """

        columns = np.transpose(board)

        validLocations = []

        for c in range(7):

            if columns[c,0] != 0:

                pass
            else:
                validLocations.append(c)

        return validLocations

    def dropPiece(self, board, column, piece):

        """
            Metodi, joka laittaa palasen sarakkeeseen.

            Args:

                board: pelilauta
                column: sarake, johon palanen laitetaan
                piece: palasta vastaava numero arvo

        """

        for i in range(self.rows-1, -1, -1):

            if board[i, column] == 0:

                board[i, column] = piece
                return board, True

        if piece != 1:

            if board[0,column]:
                    
                self.dropPiece(board,column+1,piece)

        return board, False

    def clearBoard(self, board):

        """
            Metodi, joka tyhjentää pelilaudan ja alustaa sen.

            Args:

                board: pelilauta

        """

        board = np.zeros((self.rows, self.columns), dtype=int)

        return board