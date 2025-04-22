# Problem: Concatenation of Array - https://leetcode.com/problems/concatenation-of-array/description/

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for num in nums:
            result.append(num)
        for num in nums:
            result.append(num)
        return result
            
            
            