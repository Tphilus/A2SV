# Problem: Toeplitz matrix - https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        for row_idx in range(1, rows):
            for col_idx in range(1, cols):
                if matrix[row_idx][col_idx] != matrix[row_idx - 1][col_idx - 1]:
                    return False
        return True
        