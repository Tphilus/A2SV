# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        maxLocal = [[0] * (N-2) for _ in range(N-2)]
        
        for i in range(N-2):
            for j in range(N-2):
                curr = 0
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        curr = max(curr, grid[row][col])
                        
                maxLocal[i][j] = curr
        
        return maxLocal