class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)<3: 
            return 0
        count,i = 0,3
        dt = Counter(s[:2])
        for i in range(3,len(s)+1):
            dt[s[i-1]] += 1
            if max(dt.values())==1:
                count+=1
            if dt[s[i-3]] == 1:
                del dt[s[i-3]]
            else:
                dt[s[i-3]] -= 1
        return count
