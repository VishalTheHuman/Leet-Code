class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        diff = 0
        nums = sorted(set(nums))
        for j in range(1,len(nums)):
            diff = max(diff,nums[j]-nums[j-1])
        return diff
