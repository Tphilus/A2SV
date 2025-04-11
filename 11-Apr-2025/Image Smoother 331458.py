# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        # Create a new matrix of the same size to store the result
        result = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                total_sum = 0
                count = 0
                
                # Check the 3x3 grid centered at (i, j)
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        # Skip if position is outside the matrix
                        if 0 <= x < m and 0 <= y < n:
                            total_sum += img[x][y]
                            count += 1
                
                # Calculate the average and round down (floor division in Python)
                result[i][j] = total_sum // count
        
        return result
