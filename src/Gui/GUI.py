
import pygame
from logic import matrix_logic

class Gui():

    def __init__(self):

        self.logic = matrix_logic.Logic()

        self.board = self.logic.board
        self.rows = self.logic.rows
        self.cols = self.logic.columns

        pygame.init()

        #self.size = self.width, self.height = 800, 800

        self.black = (0, 0, 0)
        self.gray = (128, 128, 128)
        self.red = (255, 50, 0)
        self.yellow = (255, 255, 0)

        self.block_size = 130
        self.circle_size = 50

    def draw_board_gui(self, screen, board, currentColumn, currentPiece):

        if currentPiece == 1:

            color = self.red

        elif currentPiece == -1:

            color = self.yellow

        pygame.draw.circle(screen, color, (self.block_size * currentColumn + self.circle_size + 5, 50), self.circle_size)

        for row in range(self.rows):

            for col in range(self.cols):

                color = self.black

                x = self.block_size * col
                y = self.block_size * row + 120

                pos = (x + self.circle_size + 5, y + self.circle_size + 5)

                piece = board[row,col]

                #print(board)

                #print(col)

                #print(self.board[0,0])

                #print(piece)

                if piece == 1:

                    color = self.red

                    #pygame.draw.circle(screen, color, (x + self.circle_size + 5), self.circle_size)

                elif piece == -1:

                    color = self.yellow

                #pygame.draw.rect(screen, self.gray,
                                     #(x, y, self.block_size+40, self.block_size+40))
                
                pygame.draw.circle(screen, color, pos, self.circle_size)


    def draw_main_gui(self, screen, board, currentColumn, currentPiece):

        screen.fill(self.gray)

        self.draw_board_gui(screen, board, currentColumn, currentPiece)

