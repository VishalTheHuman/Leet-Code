class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dt = {}
        for id,val in nums1:
            dt[id] = dt.get(id,0)+val
        for id,val in nums2:
            dt[id] = dt.get(id,0)+val
        return sorted([[id,val] for id,val in dt.items()])
