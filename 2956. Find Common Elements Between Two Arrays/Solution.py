class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = [0,0]
        count = 0
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                count+=1
        arr[0] = count
        count = 0
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                count+=1
        arr[1] = count
        return arr
