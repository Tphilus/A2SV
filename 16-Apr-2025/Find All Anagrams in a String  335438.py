# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p) 
        k = len(p)
        result = s[:k]
        current = Counter(result)
        annagram = []

        for right in range(k, len(s)):
            left = right - k

            if current == target:
                annagram.append(left)
        
            current[s[left]] -= 1
            current[s[right]] += 1

        if current == target: annagram.append(len(s)-k)
        return annagram