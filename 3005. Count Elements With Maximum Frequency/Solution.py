 class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dt = Counter(nums)
        max_val = max(dt.values())
        count = 0
        for x,y in dt.items():
            if y==max_val:
                count+=y
        return count
