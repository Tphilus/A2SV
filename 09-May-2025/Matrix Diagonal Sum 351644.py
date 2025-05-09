# Problem: Matrix Diagonal Sum - https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        count = 0

        for i in range(n):
            count += mat[i][i] # primary diagonal
            count += mat[i][n - 1 - i] # secondary diagonal
        
        return count - (mat[n // 2][n // 2] if n % 2 else 0)
