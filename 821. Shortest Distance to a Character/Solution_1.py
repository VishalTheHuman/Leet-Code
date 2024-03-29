class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ls = [i for i in range(len(s)) if s[i]==c]
        ret  = []
        for i in range(len(s)):
            ind = min([abs(x-i) for x in ls])
            ret.append(ind)
        return ret
