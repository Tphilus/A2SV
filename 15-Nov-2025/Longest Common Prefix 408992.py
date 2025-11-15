# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            current_str = strs[i]

            while prefix != current_str[:len(prefix)]:
                prefix = prefix[:-1]

                if not prefix:
                    return ""
        
        return prefix