class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        arr = [0]
        curr = 0
        for num in nums:
            curr+=num
            arr.append(curr)
        for i in range(len(nums)):
            if arr[i+1] == arr[-1]-arr[i]:
                return i
        return -1
