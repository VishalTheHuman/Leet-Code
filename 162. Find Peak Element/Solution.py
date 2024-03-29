class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        index = None
        nums = [float('-inf')] + nums + [float('-inf')]
        def binarySearch(start, end):
            nonlocal index
            if start > end or index:
                return
            mid = (start + end)//2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                index = mid - 1
                return
            binarySearch(start, mid-1)
            binarySearch(mid+1, end)
        binarySearch(1,len(nums)-2)
        return index if index is not None else 0
