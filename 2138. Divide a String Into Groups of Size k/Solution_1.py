class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ls = [s[i:i+k] for i in range(0,len(s),k)]
        ls[-1]+=fill*(k-len(ls[-1]))
        return ls
