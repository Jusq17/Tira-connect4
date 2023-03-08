
import numpy as np
from logic import matrix_logic
import game.game_main
import logic.AI
import unittest
import datetime
import timeit
import math

class tests(unittest.TestCase):

    def setUp(self):

        self.logic = matrix_logic.Logic()
        self.game = game.game_main.Game()
        self.AI = logic.AI.AI()

        self.board = self.logic.board

    def testColumnsEvaluation(self):

        self.board[0, 5] = 1
        self.board[1, 5] = 1
        self.board[2, 5] = 1
        self.board[3, 5] = 1

        score = self.AI.evaluatePosition(self.board, 1)
        self.assertGreater(score, 10000)
        self.board = self.logic.clearBoard(self.board)

    def testRowsEvaluation(self):

        self.board[0, 1] = 1
        self.board[0, 2] = 1
        self.board[0, 3] = 1
        self.board[0, 4] = 1

        score = self.AI.evaluatePosition(self.board, 1)
        self.assertGreater(score, 10000)
        self.board = self.logic.clearBoard(self.board)

    def testRowsEvaluationBoth(self):

        self.board[2, 1] = 1
        self.board[2, 2] = 1
        self.board[2, 3] = 1

        self.board[3, 2] = -1
        self.board[3, 3] = -1

        score = self.AI.evaluatePosition(self.board, 1)
        self.assertGreater(score, 0)
        self.board = self.logic.clearBoard(self.board)

    def testRowsEvaluation3(self):

        self.board[0, 1] = 1
        self.board[0, 2] = 1
        self.board[0, 3] = 1

        score = self.AI.evaluatePosition(self.board, 1)
        self.assertGreater(score, 7)
        self.board = self.logic.clearBoard(self.board)

    def testDiagonalsEvaluation(self):

        self.board[1, 1] = 1
        self.board[2, 2] = 1
        self.board[3, 3] = 1
        self.board[4, 4] = 1

        score = self.AI.evaluatePosition(self.board, 1)
        self.assertGreater(score, 10000)
        self.board = self.logic.clearBoard(self.board)

        self.board[1, 1] = -1
        self.board[2, 2] = -1
        self.board[3, 3] = -1
        self.board[4, 4] = -1

        score = self.AI.evaluatePosition(self.board, 1)
        self.assertLess(score, -1000)
        self.board = self.logic.clearBoard(self.board)

    def testGameOverPlayer(self):

        self.board = self.logic.clearBoard(self.board)

        self.board[0, 5] = -1
        self.board[1, 5] = -1
        self.board[2, 5] = -1
        self.board[3, 5] = -1

        gameOverText = self.AI.game_Over(self.board)
        self.assertEqual(gameOverText, (True, "Player 1 wins!"))

    def testGameOverFull(self):

        self.board = self.logic.clearBoard(self.board)
        gameOverText = self.AI.game_Over(self.board)
        self.assertEqual(gameOverText, (False, ""))

    def testGameOverAI(self):

        self.board = self.logic.clearBoard(self.board)

        self.board[0, 0] = 1
        self.board[1, 1] = 1
        self.board[2, 2] = 1
        self.board[3, 3] = 1

        gameOverText = self.AI.game_Over(self.board)
        self.assertEqual(gameOverText, (True, "AI opponent wins!"))

    def testMinimaxDepth1(self):

        self.board = self.logic.clearBoard(self.board)
        depth = 1

        startTime = datetime.datetime.now()
        self.AI.minimax(depth, self.board, True, 1, -math.inf, math.inf)
        endTime = datetime.datetime.now()

        executionTime = endTime - startTime
        executionTime = str(executionTime)[5:]
        executionTime = float(executionTime)
        
        self.assertLess(executionTime, 0.1)

    def testMinimaxDepth4(self):

        self.board = self.logic.clearBoard(self.board)
        depth = 4

        startTime = datetime.datetime.now()
        self.AI.minimax(depth, self.board, True, 1, -math.inf, math.inf)
        endTime = datetime.datetime.now()

        executionTime = endTime - startTime
        executionTime = str(executionTime)[5:]
        executionTime = float(executionTime)
        
        self.assertLess(executionTime, 5)

    def testMinimaxDepth5(self):

        self.board = self.logic.clearBoard(self.board)
        depth = 5

        startTime = datetime.datetime.now()
        self.AI.minimax(depth, self.board, True, 1, -math.inf, math.inf)
        endTime = datetime.datetime.now()

        executionTime = endTime - startTime
        executionTime = str(executionTime)[5:]
        executionTime = float(executionTime)
        
        self.assertLess(executionTime, 10)

if __name__ == "__main__":

    unittest.main()
