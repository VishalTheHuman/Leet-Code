class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dt = Counter(nums)
        twice = None
        none = None
        for i in range(len(nums)):
            if twice and none:
                break
            if (i+1) not in dt:
                none = i+1
            if dt[i+1]==2:
                twice = i+1
        return twice, none
