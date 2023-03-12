# Implementation document

## The goal of the program

The aim of this program is to build an AI-opponent that can play Connect Four against a human player.
<br/>
This requires the use of some sort of data-structure and an algorithm.

## The algorithm and data-structure used

The most simple and effective algorithm for this program is the Minimax algorithm.
This algorithm looks at all possible situations/positions at a certain depth. 
It can for example look at all scenarios that can happen within five moves of the current position.

Each position is evaluated individually by a position evaluation function. In this program the position evaluation function is tailored specifically to Connect 4. 
It favours positions where many pieces of the same color are next to each other in a row, column or a diagonal. The center column is also appreciated because it often leads to
more possible connect fours.

The game board can be easily represented as a 2D-array. For this program I chose a numpy array instead of a normal python list.

## The UI

This program is a game meant to be played by a real player. Because of this the UI is very important. This game has a Graphical User Interface/GUI that is made with the pygame library.

The GUI has two views: 
- A "start-menu" where the player can choose the difficulty
- A "game-view" where the actual gameplay happens

## The structure of the program

The program has 4 modules:
- matrix_logic with Logic-class
- AI with the AI-class
- GUI with the Gui-class
- game_main with the Game-class

### The following sequence diagram shows how the program operates when the player places down a piece on the board

```mermaid
sequenceDiagram
  actor User
  participant GUI
  participant Game
  participant Logic
  participant AI
  User->>Game: Press the 'ENTER' key
  Game->>Logic: dropPiece(board)
  Game->>AI: minimax(depth, board, maximizingPlayer, piece, alpha, beta)
  Game->>GUI: drawMainGUI(screen, board, currentColumn, currentPiece, winningText)
  ```

