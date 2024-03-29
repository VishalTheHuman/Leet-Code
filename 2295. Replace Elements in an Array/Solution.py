class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dt = {x:ind for ind,x in enumerate(nums)}
        for old, new in operations:
            ind = dt[old]
            del dt[old]
            dt[new] = ind
        for val,ind in dt.items():
            nums[ind] = val
        return nums
