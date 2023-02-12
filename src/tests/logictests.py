
import numpy as np
from logic import matrix_logic
import game.game_main
import logic.AI
import unittest


class tests(unittest.TestCase):

    def setUp(self):

        self.logic = matrix_logic.Logic()
        self.game = game.game_main.Game()
        self.AI = logic.AI.AI()

        self.board = self.logic.board

    def testEvaluation(self):

        self.board[0, 5] = 1
        self.board[1, 5] = 1
        self.board[2, 5] = 1
        self.board[3, 5] = 1

        score = self.AI.evaluatePosition(self.board, 1)
        self.assertGreater(score, 10000)
        self.board = self.logic.clearBoard(self.board)

        self.board[0, 1] = 1
        self.board[0, 2] = 1
        self.board[0, 3] = 1
        self.board[0, 4] = 1

        score = self.AI.evaluatePosition(self.board, 1)
        self.assertGreater(score, 10000)
        self.board = self.logic.clearBoard(self.board)

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
        self.assertLess(score, -10000)
        self.board = self.logic.clearBoard(self.board)

    def testGameOver(self):

        self.board = self.logic.clearBoard(self.board)

        self.board[0, 5] = -1
        self.board[1, 5] = -1
        self.board[2, 5] = -1
        self.board[3, 5] = -1

        gameOverText = self.AI.Game_over(self.board)
        self.assertEqual(gameOverText, (True, "Player 1 wins!"))

        self.board = self.logic.clearBoard(self.board)
        gameOverText = self.AI.Game_over(self.board)
        self.assertEqual(gameOverText, (False, ""))

        self.board[0, 0] = 1
        self.board[1, 1] = 1
        self.board[2, 2] = 1
        self.board[3, 3] = 1

        gameOverText = self.AI.Game_over(self.board)
        self.assertEqual(gameOverText, (True, "AI opponent wins!"))


if __name__ == "__main__":

    unittest.main()
