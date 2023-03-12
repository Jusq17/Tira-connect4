# Tira-connect4
Algorithms and data structures course 2023

## Connect Four game with an AI opponent

The aim of this project is to create an AI that can play connect four using a minimax algorithm and alpha-beta pruning.

The game and AI are developed using Python3 and the GUI using the pygame library.
<br/>
The numpy library is also used heavily when dealing with the gameboard.

## Documentation

[Project Definition](https://github.com/Jusq17/Tira-connect4/blob/main/Documentation/project-definition.md)
<br/>
[Implementation Document]()
<br/>
[User Manual](https://github.com/Jusq17/Tira-connect4/blob/main/Documentation/user-manual.md)
<br/>
[Test Document](https://github.com/Jusq17/Tira-connect4/blob/main/Documentation/test-document.md)

## All of the commands that can be run from the terminal/command line

Starting the program:

```bash
poetry run invoke start
```
Running the tests:

```bash
poetry run invoke test
```
Generating the test coverage-report:

```bash
poetry run invoke coveragereport
```

Running the pylint checks:

```bash
poetry run invoke lint
```
