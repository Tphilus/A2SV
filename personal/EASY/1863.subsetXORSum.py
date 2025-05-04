"""
1863. Sum of All Subset XOR Totals
"""
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for idx in range(len(nums)):
            res |= nums[idx]
        return res << (len(nums) - 1)
