class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ls = []
        def perms(curr_sum=0,l=[],i=0):
            nonlocal target
            if curr_sum==target:
                l = sorted(l)
                if l not in ls:
                    ls.append(l)
                return
            if curr_sum > target:
                return
            for i in range(i,len(candidates)):
                perms(curr_sum+candidates[i],l+[candidates[i]],i)
        perms()
        return ls
