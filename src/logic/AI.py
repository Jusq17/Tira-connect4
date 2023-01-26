
import numpy as np
import math
from logic import matrix_logic

class AI():

    def __init__(self):

        self.logic = matrix_logic.Logic()

        self.score = 0
        self.piece = 1

    def getValidColumns(self, board):

        columns = np.transpose(board)

        validLocations = []

        for c in range(7):

            if columns[c,0] != 0:

                pass
            else:
                validLocations.append(c)

        return validLocations


    def evaluatePosition(self, board, piece):

        self.piece = piece

        self.score = 0

        columns = np.transpose(board)

        centerColumn = columns[3]

        neg_diagonals = []
        pos_diagonals = []

        for piece in centerColumn:

            if piece == self.piece:

                self.score += 4

        for r in board:

            for c in range(4):

                window = r[c:c+4]

                pieceCount = np.count_nonzero(window == self.piece)
                enemyPieceCount = np.count_nonzero(window == self.piece*-1)
                emptyCount = np.count_nonzero(window == 0)

                if pieceCount == 4:

                    self.score += 10000

                if pieceCount == 3 and emptyCount == 1:

                    self.score += 4

                if pieceCount == 2 and emptyCount == 2:

                    self.score += 2

                if enemyPieceCount == 4:

                    self.score -= 1000

                if enemyPieceCount == 3 and emptyCount == 1:

                    self.score -= 100

                if enemyPieceCount == 2 and emptyCount == 2:

                    self.score -= 4

                #if board[r,c] == self.piece and board[r,c+1] == self.piece and board[r,c+2] == self.piece and board[r,c+3] == self.piece:

                    #self.score += 10000

        for c in columns:

            for r in range(3):

                window = c[r:r+4]

                pieceCount = np.count_nonzero(window == self.piece)
                enemyPieceCount = np.count_nonzero(window == self.piece*-1)
                emptyCount = np.count_nonzero(window == 0)

                if pieceCount == 4:

                    self.score += 10000

                if pieceCount == 3 and emptyCount == 1:

                    self.score += 4

                if pieceCount == 2 and emptyCount == 2:

                    self.score += 2

                if enemyPieceCount == 4:

                    self.score -= 1000

                if enemyPieceCount == 3 and emptyCount == 1:

                    self.score -= 100

                if enemyPieceCount == 2 and emptyCount == 2:

                    self.score -= 2

            for offset in range(-2,4):

                new_board = np.flipud(board)

                pos_diagonal = np.diagonal(new_board, offset)

                pos_diagonals.append(pos_diagonal)

            for r in pos_diagonals:

            #print(neg_diagonal)

                for c in range(3):

                    #neg_diagonal = np.diagonal(board)

                    window = r[c:c+4]

                    pieceCount = np.count_nonzero(window == self.piece)
                    enemyPieceCount = np.count_nonzero(window == self.piece*-1)
                    emptyCount = np.count_nonzero(window == 0)

                    if pieceCount == 4:

                        self.score += 10000

                    if pieceCount == 3 and emptyCount == 1:

                        self.score += 4

                    if pieceCount == 2 and emptyCount == 2:

                        self.score += 2

                    if enemyPieceCount == 4:

                        self.score -= 1000

                    if enemyPieceCount == 3 and emptyCount == 1:

                        self.score -= 100

                    if enemyPieceCount == 2 and emptyCount == 2:

                        self.score -= 2

            for offset in range(-2,4):

                neg_diagonal = np.diagonal(board, offset)

                neg_diagonals.append(neg_diagonal)

            for r in neg_diagonals:

                #print(neg_diagonal)

                for c in range(3):

                    #neg_diagonal = np.diagonal(board)

                    window = r[c:c+4]

                    pieceCount = np.count_nonzero(window == self.piece)
                    enemyPieceCount = np.count_nonzero(window == self.piece*-1)
                    emptyCount = np.count_nonzero(window == 0)

                    if pieceCount == 4:

                        self.score += 10000

                    if pieceCount == 3 and emptyCount == 1:

                        self.score += 4

                    if pieceCount == 2 and emptyCount == 2:

                        self.score += 2

                    if enemyPieceCount == 4:

                        self.score -= 1000

                    if enemyPieceCount == 3 and emptyCount == 1:

                        self.score -= 100

                    if enemyPieceCount == 2 and emptyCount == 2:

                        self.score -= 2

        #print(neg_diagonals)

        return self.score

    def minimax(self, depth, board, maximizingPlayer, piece):

        bestPosition = 0
        maxScore = 0
        minScore = 0

        validLocations = self.getValidColumns(board)

        if depth == 0:

            score = self.evaluatePosition(board, -1)

            return score, bestPosition

        if maximizingPlayer == True:

            score = -math.inf

            for i in validLocations:

                newBoard = np.copy(board)

                newBoard = self.logic.dropPiece(newBoard, i, -piece)[0]

                #score = -math.inf

                #self.piece *= -1

                score = self.minimax(depth-1, newBoard, False, -piece)[0]

                if score > maxScore:

                    maxScore = score
                    bestPosition = i

            return score, bestPosition

        else:

            score = math.inf

            for i in validLocations:

                newBoard = np.copy(board)

                newBoard = self.logic.dropPiece(newBoard, i, -piece)[0]

                #score = math.inf

                #self.piece *= -1

                score = self.minimax(depth-1, newBoard, True, -piece)[0]

                if score < minScore:

                    minScore = score
                    bestPosition = i

            return score, bestPosition

        #if board[0,bestPosition] != 0:

            #bestPosition += 1

        print(self.getValidColumns(board))

        self.logic.dropPiece(board, bestPosition, self.piece)