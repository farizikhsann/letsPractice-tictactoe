# letsPractice-tictactoe
## Question-4

A tic-tac-toe board looks like a large hash symbol (#) with nine slots that can each contain an *X*, an *O*, or a blank. To represent the board with a dictionary, you can assign each slot a string-value key, as shown in figure.

You can use string values to represent what’s in each slot on the board: 'X', 'O', or ' ' (a space). Thus, you’ll need to store nine strings. You can use a dictionary of values for this. The string value with the key 'top-R' can represent the top-right corner, the string value with the key 'low-L' can represent the bottom-left corner, the string value with the key 'mid-M' can represent the middle, and so on. If player X went first and chose the middle space, you could represent that board as shown in figure.

Of course, the player sees only what is printed to the screen, not the contents of variables. Let’s create a `printBoard()` function to print the board dictionary onto the screen.

```python
def printBoard(board):
    print(board[key] + '|' + board[key] + '|' + board[key])
    print('-+-+-')
    print(board[key] + '|' + board[key] + '|' + board[key])
    print('-+-+-')
    print(board[key] + '|' + board[key] + '|' + board[key])
```

This isn’t a complete tic-tac-toe game for instance, it doesn’t ever check whether a player has won but it’s enough to see how data structures can be used in programs.
