class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums = nums+[int(str(num)[::-1]) for num in nums]
        return len(set(nums))
