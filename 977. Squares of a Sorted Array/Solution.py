class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        ind = None
        i = 0
        while i < len(nums):
            if nums[i] >= 0:
                ind = i
                break
            nums[i]*= nums[i]
            i += 1
        j = i
        i -= 1 
        while i >= 0 and j < len(nums):
            val = nums[j]**2
            if nums[i] < val:
                result.append(nums[i])
                i -= 1
            else:
                result.append(val)
                j += 1
        while i >= 0:
            result.append(nums[i])
            i -= 1
        while j < len(nums):
            result.append(nums[j]**2)
            j += 1
        return result
