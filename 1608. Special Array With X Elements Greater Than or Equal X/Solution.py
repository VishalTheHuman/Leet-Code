class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        idx = 0
        for i in range(len(nums)+1):
            if idx < len(nums):
                while idx < len(nums) and nums[idx] < i:
                    idx += 1
                if len(nums) - idx == i:
                    return i 
            else:
                break
        return -1
