# Check if array is sorted
# Difficulty: EasyAccuracy: 39.37%Submissions: 246K+Points: 2Average Time: 15m
# Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

# Examples:

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: true
# Explanation: The given array is sorted.
# Input: arr[] = [90, 80, 100, 70, 40, 30]
# Output: false
# Explanation: The given array is not sorted.
# Constraints:
# 1 ≤ arr.size ≤ 106
# - 109 ≤ arr[i] ≤ 109

#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        # code here
        
        # for i in range(len(arr)-1):
        #     if arr[i] > arr[i + 1]:
        #         return False
        # return True
        
        left = 0
        right = 1
        size = len(arr)
        
        while right < size:
            if arr[left] > arr[right]:
                return False
            
            left += 1
            right += 1
        return True