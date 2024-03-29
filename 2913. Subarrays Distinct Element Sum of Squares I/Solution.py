class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        def sumSquare(ls):
            return sum(x**2 for x in ls)
        total = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                total += len(set(nums[i:j]))**2
        return total
