# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums) # k will not be out of bound

        # end = nums[-k:]
        end = nums[len(nums) - k : ]
        end.extend(nums[ : len(nums) - k])

        nums[:] = end
        return end     
