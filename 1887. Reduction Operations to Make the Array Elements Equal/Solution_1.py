class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        up = 0
        count = 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                up+=1
            count+=up
        return count
