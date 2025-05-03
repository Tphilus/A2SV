# Problem: Defanging an IP Address - https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for _ , char in enumerate(address):
            if char != ".":
                res += char
            else:
                res += "[.]"
        
        return res
        