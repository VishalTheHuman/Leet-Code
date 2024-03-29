class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        dt = {}
        for i in range(len(nums)):
            for num in nums[i]:
                dt[num] = dt.get(num,0)+1
        return sorted([k for k,v in dt.items() if v == len(nums)])
        
