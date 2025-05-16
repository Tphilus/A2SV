# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        window_sum = sum(nums[:k])
        max_avg = window_sum

        for num in range(k, n):
            window_sum += nums[num] - nums[num - k]
            max_avg = max(max_avg, window_sum)
        
        return max_avg / k