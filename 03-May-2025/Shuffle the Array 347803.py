# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        lens = len(nums) // 2
        
        for i in range(lens):
            res.append(nums[i])
            res.append(nums[i + lens])
        
        return res