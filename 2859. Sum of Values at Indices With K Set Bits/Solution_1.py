class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum_= 0 
        for i in range(len(nums)):
            if bin(i).count("1") == k:
                sum_+= nums[i]
        return sum_
