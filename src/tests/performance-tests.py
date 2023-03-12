import numpy as np
from logic import matrix_logic
import game.game_main
import logic.AI
import numpy as np
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

    def testMinimaxDepth2(self):

        self.board = self.logic.clearBoard(self.board)
        depth = 2

        startTime = datetime.datetime.now()
        self.AI.minimax(depth, self.board, True, 1, -math.inf, math.inf)
        endTime = datetime.datetime.now()

        executionTime = endTime - startTime
        executionTime = str(executionTime)[5:]
        executionTime = float(executionTime)

        self.assertLess(executionTime, 0.5)

    def testMinimaxDepth3(self):

        self.board = self.logic.clearBoard(self.board)
        depth = 3

        startTime = datetime.datetime.now()
        self.AI.minimax(depth, self.board, True, 1, -math.inf, math.inf)
        endTime = datetime.datetime.now()

        executionTime = endTime - startTime
        executionTime = str(executionTime)[5:]
        executionTime = float(executionTime)

        self.assertLess(executionTime, 2)

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

        self.assertLess(executionTime, 15)

    def testMinimaxDepth6(self):

        self.board = self.logic.clearBoard(self.board)
        depth = 6

        startTime = datetime.datetime.now()
        self.AI.minimax(depth, self.board, True, 1, -math.inf, math.inf)
        endTime = datetime.datetime.now()

        executionTime = endTime - startTime
        executionTime = str(executionTime)[5:]
        executionTime = float(executionTime)

        self.assertLess(executionTime, 60)