# Problem: Reshape the Matrix - https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = [[0] * c for _ in range(r)]
        reshape_arr = []

        if len(mat) * len(mat[0]) != r*c:
            return mat
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                reshape_arr.append(mat[i][j])
        
        l = 0
        for rows in range(r):
            for cols in range(c):
                res[rows][cols] = reshape_arr[l]
                l += 1
        
        return res