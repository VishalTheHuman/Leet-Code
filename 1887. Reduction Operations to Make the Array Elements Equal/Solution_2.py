class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 1
        count = 0
        while i < len(nums):
            if nums[i]!=nums[i-1]:
                count+= (n-i)
            i+=1
        return count
