# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_ = 0

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            a = w * h
            max_ = max(max_, a)

            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        
        return max_