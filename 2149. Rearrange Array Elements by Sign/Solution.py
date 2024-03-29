class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 1
        arr = [None]*len(nums)
        for num in nums:
            if num < 0:
                arr[neg] = num
                neg += 2
            else:
                arr[pos] = num
                pos += 2
        return arr
