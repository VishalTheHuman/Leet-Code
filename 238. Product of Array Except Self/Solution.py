class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        if zeros>1:
            return [0]*len(nums)
        ind = None
        prod = 1
        arr = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                ind = i
            else:
                prod*=nums[i]
        if ind is not None:
            arr[ind] = prod
        else:
            for i in range(len(nums)):
                arr[i] = prod//nums[i]
        return arr
