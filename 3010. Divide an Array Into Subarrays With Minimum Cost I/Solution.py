class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cost = nums[0]
        nums = nums[1:]
        nums.sort()
        return cost + sum(nums[:2])
