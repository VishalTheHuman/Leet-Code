class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums,reverse=True)
        total = sum(nums)
        curr = 0
        for idx,val in enumerate(nums):
            curr += val
            if curr > total-curr:
                return nums[:idx+1]
        return []
