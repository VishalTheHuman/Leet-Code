class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0 
        max_sum = 0
        for x in nums:
            if curr < 0:
                curr = 0
            curr += x
            if curr > max_sum: 
                max_sum = curr
        return max_sum if max_sum else max(nums)
