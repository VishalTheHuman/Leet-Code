class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result = []
        prev = 0
        total = sum(nums)
        n = len(nums)
        for i in range(len(nums)):
            s = i*nums[i] - prev + abs(total-prev-(n-i)*nums[i])
            result.append(s)
            prev+=nums[i]
        return result
