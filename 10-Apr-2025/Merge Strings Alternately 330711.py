# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = []

        # Use the two pointer to iterate through both strings
        i = j = 0
        while i < min(len(word1), len(word2)):
            result.append(word1[i] + word2[i])
            i += 1

        result.append(word1[i:])
        result.append(word2[i:])
        

        return "".join(result)
        