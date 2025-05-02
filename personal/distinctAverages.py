class Solution:
    def distinctAverages(self, nums: List[int]) -> int:

        nums.sort()
        total_avg = set()

        while nums:
            
            min_ = nums.pop(0)
            max_ = nums.pop(-1)

            avg = (min_ + max_) / 2
            total_avg.add(avg)
        
        return len(total_avg)
