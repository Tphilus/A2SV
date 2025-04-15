# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(names)):
            max_ = i
            for j in range(i + 1, len(heights)):
                if heights[j] > heights[max_]:
                    max_ = j 
            print(max_)
            heights[i], heights[max_] = heights[max_], heights[i] 
            names[i], names[max_] = names[max_], names[i] 

        return names


