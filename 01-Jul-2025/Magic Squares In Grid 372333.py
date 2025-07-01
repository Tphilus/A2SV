# Problem: Magic Squares In Grid - https://leetcode.com/problems/magic-squares-in-grid/

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def magic(row, col):
            # Ensure 1 - 9 
            values = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if grid[i][j] in values or not (1 <= grid[i][j] <= 9):
                        return 0
                    values.add(grid[i][j])

            # Rows 
            for i in range(row, row + 3):
                if sum(grid[i][col:col + 3]) != 15:
                    return 0

            # Cols
            for i in range(col, col + 3):
                if(grid[row][i] + grid[row + 1][i] + grid[row+2][i]) != 15:
                    return 0
            
            # Diagonals
            if(
                grid[row][col] + grid[row + 1][col + 1] + grid[row+2][col+2] != 15 or 
                grid[row][col + 2] + grid[row + 1][col + 1] + grid[row+2][col] != 15
            ):
                return 0
            return 1
        
        res = 0

        for row in range(ROWS - 2):
            for col in range(COLS - 2):
                res += magic(row, col)
        
        return res