"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""

#  I had to make my own Set data structure to add the functionality of returning
#  True when adding an element that is already in the set
class MySet:

    def __init__(self):
        self.the_set = []

    def add(self, val):
        if val in self.the_set:
            return True
        else:
            self.the_set.append(val)
            return False

    def display(self):
        for val in self.the_set:
            print(val)


def validate_sudoku_board(board):
    n = len(board)
    myset = MySet()
    for row in range(n):
        for col in range(n):
            # Checking/adding rows:
            # First condition must pass (element must not be a '.') in order to even add the element to our set.
            # If second condition is True (adding the string returns True) that means we've encountered a duplicate.
            #
            # 0 0 0 | 0 0 0 | 0 0 0 |
            # 1 1 1 | 1 1 1 | 1 1 1 |
            # 2 2 2 | 2 2 2 | 2 2 2 |
            # . . . | . . . | . . . |
            # n n n | n n n | n n n |

            if board[row][col] != '.' and myset.add(f'{board[row][col]} in row {row}'):
                myset.display()
                return False

            # Checking/adding columns:
            # Same as checking rows but it's not as intuitive because we're not checking column by column, we're
            # still going row by row, however strings are still being compared since they have similar strings.
            #
            # 0 1 2 | 3 4 5 | 6 7 8
            # 0 1 2 | 3 4 5 | 6 7 8
            # 0 1 2 | 3 4 5 | 6 7 8
            # . . . | . . . | . . .
            # 0 1 2 | 3 4 5 | 6 7 8

            if board[row][col] != '.' and myset.add(f'{board[row][col]} in column {col}'):
                return False

            # Checking/adding squares:
            # Here we are checking row by row, but every 3 elements the column number increases y 1 while the row
            # number increases by 1 every 27 elements (9 elements by 3 squares). This creates a series of strings
            # that are compared in a 3 by 3 square fashion
            #
            # 00 00 00 | 01 01 01 | 02 02 02
            # 00 00 00 | 01 01 01 | 02 02 02
            # 00 00 00 | 01 01 01 | 02 02 02
            # ------------------------------
            # 10 10 10 | 11 11 11 | 12 12 12
            # 10 10 10 | 11 11 11 | 12 12 12
            # 10 10 10 | 11 11 11 | 12 12 12
            # ------------------------------
            # 20 20 20 | 21 21 21 | 22 22 22
            # 20 20 20 | 21 21 21 | 22 22 22
            # 20 20 20 | 21 21 21 | 22 22 22

            if board[row][col] != '.' and myset.add(f'{board[row][col]} in row {row // 3} column {col // 3}'):
                return False

    return True


grid = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

grid2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(validate_sudoku_board(grid))
print(validate_sudoku_board(grid2))