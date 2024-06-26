class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        start = 1 if nums[0]%2 == 0 else 0
        for i in range(1, len(nums)):
            if nums[i]%2 != start:
                return False
            start = not start
        return True
