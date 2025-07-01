# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))

        while left <= right:
            # total = left * left + right * right
            total = pow(left, 2) + pow(right, 2)
            if total > c:
                right -= 1
            elif total < c:
                left += 1
            else:
                return True

        return False        
    