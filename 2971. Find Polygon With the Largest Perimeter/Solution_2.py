class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = nums[i] + prefix[i-1]
        for i in range(len(nums)-1,1,-1):
            if nums[i] < prefix[i-1]:
                return prefix[i-1]+nums[i]
        return -1
