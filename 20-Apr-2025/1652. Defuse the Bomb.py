class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(code)
        res = [0 for _ in range(N)]
        left = 0
        cur_sum = 0

        for right in range(N + abs(k)):
            cur_sum += code[right % N]

            if right - left + 1 > abs(k):
                cur_sum -= code[left % N] 
                left = (left + 1) % N 

            if right - left + 1 == abs(k):
                if k > 0:
                    res[(left - 1) % N] = cur_sum
                elif k < 0:
                    res[(right + 1) % N] = cur_sum
        
        return res

            
            