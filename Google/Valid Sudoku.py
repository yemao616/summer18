# Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

# The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.



# The input corresponding to the above configuration :

# ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
# A partially filled sudoku which is valid.

#  Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        def is_valid_row(board):
            for row in board:
                if not is_valid(row):
                    return 0
            return 1
            
        def is_valid_column(board):
            for col in zip(*board): 
                if not is_valid(col):
                    return 0
            return 1
            
        def is_valid_square(board):
            for i in (0,3,6):
                for j in (0,3,6):
                    square = [board[x][y] for x in range(i,i+3) 
                                            for y in range(j,j+3)]
                    if not is_valid(square):
                        return 0
            return 1
        
        def is_valid(value):
            res = [i for i in value if i != '.']
            return len(res) == len(set(res))
        board = A
        return is_valid_row(board) and is_valid_column(board) and is_valid_square(board)