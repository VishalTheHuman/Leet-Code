class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ptr = 0 
        while ptr < len(nums):
            if nums[ptr] == ptr + 1 or nums[ptr] is None:
                ptr += 1
            elif nums[ptr] == nums[nums[ptr]-1]:
                nums[ptr] = None
                ptr += 1
            else:
                val = nums[nums[ptr]-1]
                nums[nums[ptr]-1] = nums[ptr]
                nums[ptr] = val
        return [i+1 for i in range(len(nums)) if nums[i] is None]
