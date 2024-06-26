class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        average = sys.maxsize
        l = 0
        r = len(nums)-1
        while r>l:
            val = (nums[l]+nums[r])/2
            if val < average:
                average = val
            l+= 1
            r-=1
        return average
