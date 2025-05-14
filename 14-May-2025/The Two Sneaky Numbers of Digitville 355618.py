# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = []
        
        for num, count in counter.items():
            if count > 1:
                res.append(num)
        
        return res