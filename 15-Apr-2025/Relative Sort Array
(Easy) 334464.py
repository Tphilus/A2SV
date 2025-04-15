# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        result = []

        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    result.append(arr1[j])
                    arr1[j] = -1
                
        arr1.sort()
        arr2.sort()

        for i in range(len(arr1)):
            if arr1[i] != -1:
                result.append(arr1[i])
        
        return result
