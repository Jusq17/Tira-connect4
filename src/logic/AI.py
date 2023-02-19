
import numpy as np
import math
from logic import matrix_logic


class AI():

    def __init__(self):

        self.logic = matrix_logic.Logic()

        self.score = 0
        self.piece = 1
        self.game_over = False

    def gameOverRows(self, board):
        """
            Metodi, joka tarkastaa onko peli loppu rivien osalta.

            Args:

                board: pelilauta

        """

        for r in board:

            for c in range(4):

                window = r[c:c+4]

                pieceCount = np.count_nonzero(window == self.piece)
                enemyPieceCount = np.count_nonzero(window == self.piece*-1)

                if pieceCount == 4:

                    return True, "AI opponent wins!"

                if enemyPieceCount == 4:

                    return True, "Player 1 wins!"

    def gameOverColumns(self, board):
        """
            Metodi, joka tarkastaa onko peli loppu sarakkeiden osalta.

            Args:

                board: pelilauta

        """

        columns = np.transpose(board)

        for c in columns:

            for r in range(3):

                window = c[r:r+4]

                pieceCount = np.count_nonzero(window == self.piece)
                enemyPieceCount = np.count_nonzero(window == self.piece*-1)

                if pieceCount == 4:

                    return True, "AI opponent wins!"

                if enemyPieceCount == 4:

                    return True, "Player 1 wins!"

    def gameOverDiagonals(self, board):
        """
            Metodi, joka tarkastaa onko peli loppu diagonaalien osalta.

            Args:

                board: pelilauta

        """

        neg_diagonals = []
        pos_diagonals = []

        for offset in range(-2, 4):

            new_board = np.flipud(board)

            pos_diagonal = np.diagonal(new_board, offset)

            pos_diagonals.append(pos_diagonal)

        for r in pos_diagonals:

            # print(neg_diagonal)

            for c in range(3):

                # neg_diagonal = np.diagonal(board)

                window = r[c:c+4]

                pieceCount = np.count_nonzero(window == self.piece)
                enemyPieceCount = np.count_nonzero(window == self.piece*-1)

                if pieceCount == 4:

                    return True, "AI opponent wins!"

                if enemyPieceCount == 4:

                    return True, "Player 1 wins!"

        for offset in range(-2, 4):

            neg_diagonal = np.diagonal(board, offset)

            neg_diagonals.append(neg_diagonal)

        for r in neg_diagonals:

            # print(neg_diagonal)

            for c in range(3):

                # neg_diagonal = np.diagonal(board)

                window = r[c:c+4]

                pieceCount = np.count_nonzero(window == self.piece)
                enemyPieceCount = np.count_nonzero(window == self.piece*-1)

                if pieceCount == 4:

                    return True, "AI opponent wins!"

                if enemyPieceCount == 4:

                    return True, "Player 1 wins!"

    def Game_over(self, board):
        """
            Metodi, joka katsoo onko peli loppu. Eli kumpi pelaajista on voittaja vai onko lauta täynnä ilman voittajaa

            Args:

                board: pelilauta

        """

        zeroCount = 0

        self.gameOverRows(board)
        self.gameOverColumns(board)
        self.gameOverDiagonals(board)

        for i in board[0]:

            if i == 0:

                zeroCount += 1

        if zeroCount == 0:

            return True, "Board is full"

        return False, ""

    def evaluateRows(self, board, piece):

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

                    self.score -= 10000

                if enemyPieceCount == 3 and emptyCount == 1:

                    self.score -= 10000

                if enemyPieceCount == 2 and emptyCount == 2:

                    self.score -= 4

        return self.score

    def evaluateColumns(self, board, piece):

        columns = np.transpose(board)

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

                    self.score -= 10000

                if enemyPieceCount == 3 and emptyCount == 1:

                    self.score -= 10000

                if enemyPieceCount == 2 and emptyCount == 2:

                    self.score -= 2

        return self.score

    def evaluateDiagonals(self, board, piece):

        neg_diagonals = []
        pos_diagonals = []

        for offset in range(-2, 4):

            new_board = np.flipud(board)

            pos_diagonal = np.diagonal(new_board, offset)

            pos_diagonals.append(pos_diagonal)

        for r in pos_diagonals:

            # print(neg_diagonal)

            for c in range(3):

                # neg_diagonal = np.diagonal(board)

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

                    self.score -= 10000

                if enemyPieceCount == 3 and emptyCount == 1:

                    self.score -= 10000

                if enemyPieceCount == 2 and emptyCount == 2:

                    self.score -= 2

        for offset in range(-2, 4):

            neg_diagonal = np.diagonal(board, offset)

            neg_diagonals.append(neg_diagonal)

        for r in neg_diagonals:

            # print(neg_diagonal)

            for c in range(3):

                # neg_diagonal = np.diagonal(board)

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

                    self.score -= 10000

                if enemyPieceCount == 2 and emptyCount == 2:

                    self.score -= 2

        return self.score

    def evaluatePosition(self, board, piece):
        """
            Metodi, joka arvostelee tietyn tilanteen pelilaudalla.
            Käyttää muita evaluate-metodeja hyödykseen.

            Args:

                board: pelilauta
                piece: palasta vastaava numero arvo

        """

        self.piece = piece

        self.score = 0

        columns = np.transpose(board)

        centerColumn = columns[3]

        neg_diagonals = []
        pos_diagonals = []

        for piece in centerColumn:

            if piece == self.piece:

                self.score += 4

        return self.score + self.evaluateRows(board, piece) + self.evaluateColumns(board, piece) + self.evaluateDiagonals(board, piece)

    def minimax(self, depth, board, maximizingPlayer, piece, alpha, beta):
        """
            Metodi, joka toteuttaa minimax-algoritmin.

            Args:

                depth: syvyys, johon algoritmi menee
                board: pelilauta
                maximizingPlayer: totuusarvo, joka kertoo onko pelaaja maksivoiva
                piece: palasta vastaava numero arvo

        """

        bestPosition = 0

        validLocations = self.logic.getValidColumns(board)

        self.Game_over(board)

        if depth == 0 or self.Game_over(board)[0] == True:

            score = self.evaluatePosition(board, -1)

            return score, bestPosition

        if maximizingPlayer == True:

            maxScore = -math.inf

            for i in validLocations:

                newBoard = np.copy(board)

                newBoard = self.logic.dropPiece(newBoard, i, -piece)[0]

                score = self.minimax(
                    depth-1, newBoard, False, -piece, alpha, beta)[0]

                # if score >= math.inf:

                # return score, bestPosition

                if score > maxScore:

                    maxScore = score
                    bestPosition = i

                alpha = max(alpha, score)

                if alpha >= beta:

                    break
                    pass

                # if score <= -1000:

                    # break

            # print(maxScore, bestPosition, depth)

            return maxScore, bestPosition

        else:

            minScore = math.inf

            for i in validLocations:

                newBoard = np.copy(board)

                newBoard = self.logic.dropPiece(newBoard, i, -piece)[0]

                score = self.minimax(
                    depth-1, newBoard, True, -piece, alpha, beta)[0]

                if score < minScore:

                    minScore = score
                    bestPosition = i

                beta = min(beta, score)

                if alpha >= beta:

                    break
                    pass

                # if score <= -10000:

                    # return score, bestPosition

                # if score <= -1000:

                    # return score, bestPosition

            return minScore, bestPosition
