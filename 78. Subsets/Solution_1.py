class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        def perms(i,prev = []):
            if i==len(nums):
                return 
            ls = []
            for i in range(i,len(nums)):
                num = nums[i]
                s = sorted(prev+[num])
                if s not in result:
                    result.append(s)
                perms(i+1,prev+[num])
            return
        perms(0)
        return result
