# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max_ = 0
        for i in range(len(accounts)):
            count = 0
            for j in range(len(accounts[0])):
                count += accounts[i][j]
                max_ = max(max_, count)
        return max_