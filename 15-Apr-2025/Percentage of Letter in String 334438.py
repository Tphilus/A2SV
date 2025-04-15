# Problem: Percentage of Letter in String - https://leetcode.com/problems/percentage-of-letter-in-string/description/%20meaning/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        num_letter = s.count(letter)
        print(num_letter)

        arr_len = len(s)
        print(arr_len)

        percentage_char = num_letter * 100 // arr_len

        return percentage_char