class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        windowSize = sum(nums)
        ones = 0
        for i in range(windowSize):
            ones += nums[i]
        swaps = windowSize - ones
        for i in range(len(nums)):
            ones += nums[(i+windowSize)%len(nums)]
            ones -= nums[i]
            swaps = min(swaps, windowSize - ones)
        return swaps
