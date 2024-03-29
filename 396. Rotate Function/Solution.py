class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        prev_sum = sum(j*nums[j] for j in range(len(nums)))
        max_val = prev_sum
        normal_sum = sum(nums)
        nums_len = len(nums)
        for i in range(1, nums_len):
            curr_sum = prev_sum - (nums_len-1)*nums[-i] + normal_sum - nums[-i]
            if max_val < curr_sum:
                max_val = curr_sum
            prev_sum = curr_sum
        return max_val
