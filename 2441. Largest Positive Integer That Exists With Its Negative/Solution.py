class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        s = set(nums)
        i = 0
        while i < len(nums) and nums[i] < 0:
            if -nums[i] in s:
                return -nums[i]
            i += 1
        return -1
