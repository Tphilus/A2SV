# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            boat += 1
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
        
        return boat
