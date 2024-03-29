class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        beauty = 0
        j = nums[0]
        min_arr = []
        min_val = float('inf')
        for i in range(len(nums)-1,-1,-1):
            min_val = min(min_val, nums[i])
            min_arr.append(min_val)
        min_arr.reverse() 
        for i in range(1, len(nums)-1):
            k = min_arr[i+1]
            if j < nums[i] < k:
                beauty += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                beauty += 1
            if nums[i] > j:
                j = nums[i]
        return beauty
