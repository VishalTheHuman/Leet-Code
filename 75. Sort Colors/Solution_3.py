class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dt = Counter(nums)
        index = 0
        for i in [0,1,2]:
            while dt.get(i,False):
                nums[index] = i
                index+=1
                dt[i]-=1
