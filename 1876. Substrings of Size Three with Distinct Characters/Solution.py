class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)<3: return 0
        count,i = 0,3
        for i in range(3,len(s)+1):
            dt = Counter(s[i-3:i])
            count+=(1 if max(dt.values())==1 else 0)
        return count
