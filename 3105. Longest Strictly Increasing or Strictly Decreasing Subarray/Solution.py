class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def condition(val_1, val_2, mode):
            """
            I - Increasing
            D - Decreasing
            """
            if mode == "I":
                return val_2 > val_1
            return val_1 > val_2
        def check(mode):
            i = 1
            start = 0 
            max_length = 1
            while i < len(nums):
                prev = nums[start]
                while i < len(nums) and condition(prev, nums[i],mode):
                    prev = nums[i]
                    i += 1
                length = i - start
                if max_length < length:
                    max_length = length
                start = i
                i += 1
            return max_length
        return max(check("I"), check("D"))
