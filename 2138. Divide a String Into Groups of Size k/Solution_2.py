class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ls = []
        i = 0 
        while i+k < len(s):
            ls.append(s[i:i+k])
            i+=k
        ls.append(s[i:])
        ls[-1] = ls[-1] + fill*(k-len(ls[-1]))
        return ls
