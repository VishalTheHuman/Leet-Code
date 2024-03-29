class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        nums +=  [0]
        ranges = []
        start = end = nums[0] 
        for i in range(1,len(nums)-1):
            if (nums[i]-nums[i-1]) == 1:
                end = nums[i]
            else:
                if start == end:
                    ranges.append(str(start))
                elif start != end:
                    ranges.append(str(start)+"->"+str(end))
                start = end = nums[i]
        return ranges + [str(start) if start == end else str(start)+"->"+str(end)]
