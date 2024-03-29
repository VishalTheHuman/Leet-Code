class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dt = Counter(nums)
        k = 0
        for i in [0,1,2]:
            val = dt[i]
            if val:
                nums[k:k+val] = [i]*val
            k+=dt[i]
