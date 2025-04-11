# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        result = set(nums)
        
        for num in range(len(nums)):
            str_num = str(nums[num])
            reverse_str = str_num[::-1]
            str_num = int(reverse_str)

            
            result.add(str_num)
                
        return len(result)