class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        prev = sum(nums[:2])
        score = 1
        for i in range(3,len(nums),2):
            if nums[i]+nums[i-1]!=prev:
                return score
            score+=1
        return score
