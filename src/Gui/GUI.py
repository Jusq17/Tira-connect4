
import pygame
from logic import matrix_logic
from logic import AI


class Gui():

    """
        Luokka, joka vastaa Käyttöliittymän ja grafiikan piirtämisestä näytölle.

        Attributes:

            black: musta väri
            gray: harmaa väri
            blue: sininen väri
            yellow: keltainen väri
            rows: laudan rivien määrä
            cols: laudan sarakkeiden määrä
            block_size: laudan laatikoiden koko
            circle_size: laudan ympyröiden koko

    """

    def __init__(self):

        self.logic = matrix_logic.Logic()
        self.AI = AI.AI()

        self.board = self.logic.board
        self.rows = self.logic.rows
        self.cols = self.logic.columns

        pygame.init()

        self.black = (0, 0, 0)
        self.white = (255,255,255)
        self.gray = (128, 128, 128)
        self.red = (255, 50, 0)
        self.orange = (255, 165, 0)
        self.yellow = (255, 255, 0)
        self.blue = (0, 0, 255)
        self.font = pygame.font.Font('freesansbold.ttf', 80)
        self.screenDimensions = (900, 900)
        self.screenCenter = (self.screenDimensions[0]/2, self.screenDimensions[1]/2)

        self.difficultyText = self.font.render("Select difficulty", True, self.white)
        self.easyText = self.font.render("Easy", True, self.yellow)
        self.mediumText = self.font.render("Medium", True, self.orange)
        self.hardText = self.font.render("Hard", True, self.red)

        self.easyRect = self.easyText.get_rect().inflate(10,10)
        self.mediumRect = self.mediumText.get_rect()
        self.hardRect = self.hardText.get_rect()

        self.easyRect.center = (450, 200 + self.easyRect[1]/2 + 50)
        self.mediumRect.center = (450, 440)
        self.hardRect.center = (450, 645)

        self.block_size = 130
        self.circle_size = 50

    def draw_board_gui(self, screen, board, currentColumn, currentPiece):

        pygame.draw.rect(screen, self.blue, (0, 110, 1000, 1000))

        if currentPiece == 1:
            color = self.red

        elif currentPiece == -1:
            color = self.yellow

        pygame.draw.circle(screen, color, (self.block_size *
                           currentColumn + self.circle_size + 5, 50), self.circle_size)

        for row in range(self.rows):

            for col in range(self.cols):

                color = self.black

                x = self.block_size * col
                y = self.block_size * row + 120

                pos = (x + self.circle_size + 5, y + self.circle_size + 5)
                piece = board[row, col]

                if piece == 1:
                    color = self.red

                elif piece == -1:
                    color = self.yellow

                pygame.draw.circle(screen, color, pos, self.circle_size)

    def draw_winning_gui(self, player, screen):

        x = 200

        if player != "":
            pygame.draw.rect(screen, self.black, (0, 0, 1000, 110))

        if len(player) > 13:

            x = 100

        screen.blit(self.font.render(player, True, self.orange), (x, 20))

    def draw_menu_gui(self, screen):

        screen.fill(self.black)
        screen.blit(self.difficultyText, (150, 20))
        screen.blit(self.easyText, (350, 200))
        screen.blit(self.mediumText, (290, 400))
        screen.blit(self.hardText, (350, 600))

        print(self.easyRect)

    def draw_main_gui(self, screen, board, currentColumn, currentPiece, winningText):

        screen.fill(self.black)
        self.draw_board_gui(screen, board, currentColumn, currentPiece)
        self.draw_winning_gui(winningText, screen)
