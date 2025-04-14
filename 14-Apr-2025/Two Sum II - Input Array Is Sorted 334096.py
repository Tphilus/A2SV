# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        current_sum = 0

        while left < right:
            current_sum = numbers[right] + numbers[left]
            if current_sum == target:
                return left + 1, right + 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

