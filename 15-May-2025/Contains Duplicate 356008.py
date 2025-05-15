# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniq_val = set(nums)
        len_set = len(uniq_val)

        return len_set != len(nums)