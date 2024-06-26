class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        t = {x:idx for idx, x in enumerate(t)}
        diff = 0
        for idx,x in enumerate(s):
            diff += abs(idx-t[x])
        return diff
