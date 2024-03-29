class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        for x in d2.keys():
            if d1.get(x,False):
                times = min(d1[x],d2[x])
                result.extend([x]*times)
        return result
