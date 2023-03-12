
import pygame
from logic import matrix_logic
from logic import AI


class Gui():

    """
        Luokka, joka vastaa Käyttöliittymän ja grafiikan piirtämisestä näytölle.

        Attributes:

            black: musta väri
            white: valkoinen väri
            gray: harmaa väri
            blue: sininen väri
            blue2: sininen väri
            yellow: keltainen väri
            orange: oranssi väri
            red: punainen väri
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
        self.white = (255, 255, 255)
        self.red = (255, 50, 0)
        self.orange = (255, 165, 0)
        self.yellow = (255, 255, 0)
        self.blue = (0, 85, 102)
        self.blue2 = (204, 221, 255)
        self.green = (0, 230, 77)
        self.font = pygame.font.Font('freesansbold.ttf', 80)
        self.font2 = pygame.font.Font('freesansbold.ttf', 80)
        self.font3 = pygame.font.Font('freesansbold.ttf', 100)
        self.font4 = pygame.font.Font('freesansbold.ttf', 101)

        self.gameText = self.font3.render("Connect 4", True, self.blue2)
        self.gameText2 = self.font4.render("Connect 4", True, self.black)
        self.easyText = self.font.render("Easy", True, self.black)
        self.mediumText = self.font.render("Medium", True, self.black)
        self.hardText = self.font.render("Hard", True, self.black)

        self.easyRect = self.easyText.get_rect().inflate(20, 20)
        self.easyRect2 = self.easyRect.inflate(15, 15)
        self.mediumRect = self.mediumText.get_rect().inflate(20, 20)
        self.mediumRect2 = self.mediumRect.inflate(15, 15)
        self.hardRect = self.hardText.get_rect().inflate(20, 20)
        self.hardRect2 = self.hardRect.inflate(15, 15)

        self.easyRect.center = (445, 240)
        self.easyRect2.center = (445, 240)
        self.mediumRect.center = (445, 440)
        self.mediumRect2.center = (445, 440)
        self.hardRect.center = (445, 640)
        self.hardRect2.center = (445, 640)

        self.block_size = 130
        self.circle_size = 50

    def drawBoardGui(self, screen, board, currentColumn, currentPiece):

        """
            Metodi, joka hoitaa pelilaudan piirtämisestä ruudulle

            Args:

                screen:  pygame ikkuna, johon grafiikat piirretään
                board: pelilauta
                currentColumn: Sarake johon pelinappula laitetaan
                currentPiece: numeroarvo, joka kuvaa pelinappulaa

        """

        pygame.draw.rect(screen, self.blue, (0, 110, 1000, 1000))

        if currentPiece == 1:
            color = self.white

        elif currentPiece == -1:
            color = self.yellow

        pygame.draw.circle(screen, color, (self.block_size *
                           currentColumn + 5 + self.circle_size + 5, 50), self.circle_size)

        for row in range(self.rows):

            for col in range(self.cols):

                color = self.black

                x = self.block_size * col + 5
                y = self.block_size * row + 120

                pos = (x + self.circle_size + 5, y + self.circle_size + 5)
                piece = board[row, col]

                if piece == 1:
                    color = self.white

                elif piece == -1:
                    color = self.green

                pygame.draw.circle(screen, color, pos, self.circle_size)

    def drawWinningGui(self, winningText, screen):

        """
            Metodi, joka hoitaa voitto-tekstin piirtämisestä ruudulle.

            Args:
            
                screen:  pygame ikkuna, johon grafiikat piirretään
                winningText: teksti, joka piirretään näytölle

        """

        x = 200

        if winningText != "":
            pygame.draw.rect(screen, self.black, (0, 0, 1000, 110))

        if len(winningText) > 14:

            x = 100

        screen.blit(self.font.render(winningText, True, self.orange), (x, 20))

    def drawMenuGui(self, screen):

        """
            Metodi, joka hoitaa start-menun piirtämisestä näytölle

            Args:

                screen:  pygame ikkuna, johon grafiikat piirretään

        """

        screen.fill(self.blue)
        screen.blit(self.gameText2, (193, 46))
        screen.blit(self.gameText, (190, 42))

        pygame.draw.rect(screen, self.black, self.easyRect2)
        pygame.draw.rect(screen, self.yellow, self.easyRect)
        screen.blit(self.easyText, (350, 200))

        pygame.draw.rect(screen, self.black, self.mediumRect2)
        pygame.draw.rect(screen, self.orange, self.mediumRect)
        screen.blit(self.mediumText, (290, 400))

        pygame.draw.rect(screen, self.black, self.hardRect2)
        pygame.draw.rect(screen, self.red, self.hardRect)
        screen.blit(self.hardText, (350, 600))

    def drawMainGui(self, screen, board, currentColumn, currentPiece, winningText):

        """
            Metodi, joka hoitaa GUI:n piirtämisestä näytölle

            Args:

                screen:  pygame ikkuna, johon grafiikat piirretään
                board: pelilauta
                currentColumn: Sarake johon pelinappula laitetaan
                currentPiece: numeroarvo, joka kuvaa pelinappulaa
                winningText: teksti, joka piirretään näytölle

        """

        screen.fill(self.black)
        self.drawBoardGui(screen, board, currentColumn, currentPiece)
        self.drawWinningGui(winningText, screen)
