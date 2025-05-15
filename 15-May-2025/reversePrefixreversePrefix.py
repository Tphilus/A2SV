"""
=====================================
    2000. Reverse Prefix of Word
=====================================
"""
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        list_val = list(word)
        
        for right_ptr in range(len(list_val)):
            if list_val[right_ptr] == ch:
                left = 0
                right = right_ptr

                while left < right:
                    list_val[left], list_val[right] = list_val[right], list_val[left]
                    left += 1
                    right -= 1
        
                return "".join(list_val)
        
        return word
                
                
        
        