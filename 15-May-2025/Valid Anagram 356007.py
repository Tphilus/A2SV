# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        char_counter_s = Counter(s)
        char_counter_t = Counter(t)

        return char_counter_s == char_counter_t