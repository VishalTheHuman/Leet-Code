class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(0,len(nums),3):
            if abs(nums[i]-nums[i+1]) <= k and abs(nums[i]-nums[i+2]) <=k and abs(nums[i+1]-nums[i+2]) <= k:
                result.append([nums[i], nums[i+1],nums[i+2]])
            else:
                return []
        return result
        
