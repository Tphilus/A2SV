# Problem: Array Subset - https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

#User function Template for python3
from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        count_a = Counter(a)
        
        for element in b:
            if count_a[element] == 0:
                return False
            count_a[element] -= 1
        return True
        
