class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0 
        end = len(nums)-1
        while start < end: 
            if nums[start]+nums[end] == target:
                break
            elif nums[start]+nums[end] > target:
                end -= 1
            else:
                start += 1
        return start+1, end+1
