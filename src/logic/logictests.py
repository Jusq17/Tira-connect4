
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

        self.assertGreater(score, 100)


if __name__ == "__main__":

    unittest.main()
