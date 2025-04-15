# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1
        teams = []
        sums = skill[0] + skill[-1]
        sum_of_chemistry = 0
        while left < right:
            if skill[left] + skill[right] != sums:
                return -1
            else:
                sum_of_chemistry += (skill[left] * skill[right])
            left +=1
            right -=1
        
        return sum_of_chemistry