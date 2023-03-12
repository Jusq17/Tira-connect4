# User manual

## Installation

- Download the zip-package or clone the git repository to your computer
- Then install poetry if you don't have it already installed
- Use the command underneath to install the necessary dependencies

```bash
poetry install
```

You're all set after that.
Now the game can be launched with:

```bash
poetry run invoke start
```

The test coverage-report can be generated with:

```bash
poetry run invoke coveragereport
```

## Gameplay

### Menu
- After starting the game you will be in the "start-menu"
- You can choose from one of three difficulties
- Click the difficulty you want to choose

### Game
- Use the arrow keys to choose where to drop your piece
- Use the "ENTER" key to drop the piece on the board
- Wait for the AI-opponent to respond with a move
- You can use the "ESC" key to move back to the "start-menu"
