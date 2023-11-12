class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        elems = set(nums1+nums2+nums3)
        ls = []
        for x in elems:
            if (x in nums1 and x in nums2) or (x in nums2 and x in nums3) or (x in nums3 and x in nums1):
                ls.append(x)
        return ls
