class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def find(arr, xor):
            nonlocal s
            s += xor
            if not arr:
                return 
            for i in range(len(arr)):
                find(arr[i+1:], xor^arr[i])

        s = 0
        for i in range(len(nums)):
            find(nums[i+1:], nums[i])
        return s
