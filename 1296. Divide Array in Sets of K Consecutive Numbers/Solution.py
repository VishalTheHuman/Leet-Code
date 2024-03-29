class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        dt = dict(sorted(Counter(nums).items(), key = lambda x : x[0]))
        curr = 0
        while dt:
            curr = k
            ls = []
            for x in list(dt.keys()):
                if curr == 0:
                    break
                if ls:
                    if abs(ls[-1] - x) != 1:
                        return False
                ls.append(x)
                curr -= 1
                if dt[x] == 1:
                    del dt[x]
                else:
                    dt[x] -= 1 
            if curr:
                return False
        return curr==0
            
