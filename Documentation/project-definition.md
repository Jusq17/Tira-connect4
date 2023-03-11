# Project definition

The aim of this project is to create an AI that can play connect four using a minimax algorithm and alpha-beta pruning.
The game and AI will be developed using Python3 and the GUI using the pygame library.

## Difficulty settings

### There will be three difficulty settings to choose from:

All of the difficulties use the same algorithm but with different depths. The harder ones will look at more moves when deciding the best move.

The first difficulty is "Easy" and only has a depth of 1. This way beginner players can have an opponent to play against. Because of the low depth the response time in the game is instant. The AI opponent instantly moves on all modern processors. 

There are two other difficulties called "Medium" and "Hard". These have a depth of 3 and 5 in the algorithm. The medium opponent responds in less than a second and can be quite difficult to beat. The Hard opponent responds in less than 10 seconds on modern processors. Because the minimax algorithm has an exponential time complexity the response times can vary from 2-9 seconds on most processors.

## Graphical User Interface

The GUI will be made using the pygame library. It will have a "start-menu" where the player can choose the difficulty. 

After the player has chosen the difficulty, the game will render the "game-view" where the gameplay happens. After the player is satisfied they can use the "ESC" key to move back to the "start-menu" and choose another difficulty with their mouse.
