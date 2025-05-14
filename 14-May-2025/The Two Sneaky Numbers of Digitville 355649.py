# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                res.append(nums[i])

        return res