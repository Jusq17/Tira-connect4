from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN
import sys
import math
import pygame
import time
import numpy as np
from Gui import GUI
from logic import matrix_logic
from logic import AI


class Game():

    """
        Luokka joka hoitaa pygame-eventtien tarkastuksen.
        Mahdollistaa, että pelaaja voi pelata käyttäen nuolinäppäimiä.

        Attributes:

            logic: pelimatriisia käsittelevä luokka.
            gui: Käyttöliittymää ja grafiikkaa käsittelevä luokka.
            clock: pygame kello, jonka avulla asetetaan framerate.
            size: pygame ikkunan koko
            screen: pygame ikkuna, jolle grafiikat piirretään.

    """

    def __init__(self):

        self.gui = GUI.Gui()
        self.logic = matrix_logic.Logic()
        self.AI = AI.AI()

        self.board = self.logic.board
        self.piece = 1
        self.currentColumn = 3
        self.gameState = 0
        self.depth = 1

        pygame.init()
        pygame.display.set_caption("Connect Four")
        self.clock = pygame.time.Clock()
        self.size = self.width, self.height = 900, 900
        self.screen = pygame.display.set_mode(self.size)

    def menu_handler(self, event):

        self.gui.draw_menu_gui(self.screen)

        if event.type == MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            if self.gui.easyRect.collidepoint(pos):

                self.gameState = 1
                self.depth = 1

            elif self.gui.mediumRect.collidepoint(pos):

                self.gameState = 1
                self.depth = 4

            elif self.gui.hardRect.collidepoint(pos):

                self.gameState = 1
                self.depth = 5

    def game_handler(self, event, depth):
        """

        Metodi, joka hoitaa pygame-eventtien tarkastamisen, kun pelaaja pelaa peliä.

        Args:

            event: pygame-event, joka tarkastetaan.

        """

        winningText = ""

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.currentColumn -= 1

                if self.currentColumn < 0:
                    self.currentColumn = 0

            if event.key == pygame.K_RIGHT:
                self.currentColumn += 1

                if self.currentColumn > 6:
                    self.currentColumn = 6

            if event.key == pygame.K_ESCAPE:

                self.gameState = 0
                self.board = self.logic.clearBoard(self.board)

            if event.key == pygame.K_RETURN:

                if self.AI.game_Over(self.board)[0] == True:
                    self.board = self.logic.clearBoard(self.board)

                else:

                    if self.logic.dropPiece(self.board, self.currentColumn, self.piece)[1] == True:

                        self.piece *= -1

        if winningText == "":

            if self.piece == -1:

                bestColumn = self.AI.minimax(
                    depth, self.board, True, -self.piece, -math.inf, math.inf)[1]
                self.logic.dropPiece(self.board, bestColumn, self.piece)
                self.piece *= -1

            if self.AI.evaluatePosition(self.board, self.piece) > 1000:

                #winningText = self.AI.game_Over(self.board)[1]
                winningText = "Player 1 wins!"
                self.gui.draw_winning_gui(winningText, self.screen)
                self.currentColumn = 3

            elif self.AI.evaluatePosition(self.board, -self.piece) > 1000:

                #winningText = self.AI.game_Over(self.board)[1]
                winningText = "AI opponent wins!"
                self.gui.draw_winning_gui(winningText, self.screen)
                self.currentColumn = 3

            #winningText = self.AI.game_Over(self.board)[1]

        self.gui.draw_main_gui(self.screen, self.board,
                               self.currentColumn, self.piece, winningText)

    def event_handler(self):
        """
            Metodi, joka hoitaa pygame-eventtien tarkastamisen.

            Args:

            none

        """

        event_list = pygame.event.get()

        for event in event_list:

            if self.gameState == 0:

                self.menu_handler(event)

            elif self.gameState == 1:

                self.game_handler(event, self.depth)

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

    def run(self):
        """
            Funktio, joka päivittää ruudun kellon määräämällä frameratella.

            Args:

            none

        """

        self.event_handler()
        pygame.display.update()
        self.clock.tick(60)
