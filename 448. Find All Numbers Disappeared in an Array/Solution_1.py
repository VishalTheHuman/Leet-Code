class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = [False] * len(nums)
        for x in nums:
            ret[x-1] = True
        return [i+1 for i in range(len(ret)) if not ret[i]]
