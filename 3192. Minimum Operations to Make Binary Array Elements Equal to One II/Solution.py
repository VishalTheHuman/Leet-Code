class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        for x in nums:
            if flips % 2 == 0:
                if x==0:
                    flips += 1
            else:
                if x == 1:
                    flips += 1
        
        return flips
