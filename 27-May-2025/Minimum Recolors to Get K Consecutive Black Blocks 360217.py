# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        white_count = blocks[:k].count("W")
        min_ = white_count

        for char in range(k, n):
            if blocks[char] == "W":
                white_count += 1
            
            if blocks[char - k] == "W":
                white_count -= 1
            
            min_ = min(min_, white_count)
        
        return min_
            
            