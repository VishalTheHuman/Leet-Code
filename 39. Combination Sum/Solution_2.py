class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ls = []
        def perms(curr_sum=0,l=[]):
            nonlocal target
            if curr_sum==target:
                l = sorted(l)
                if l not in ls:
                    ls.append(l)
                return
            if curr_sum > target:
                return
            for x in candidates:
                perms(curr_sum+x,l+[x])
        perms()
        return ls
