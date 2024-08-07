class Solution:
    def getSmallestString(self, s: str) -> str:
        s1 = "9"*1000
        for i in range(1,len(s)):
            n1 = int(s[i-1])
            n2 = int(s[i])
            if n1 % 2 == n2 % 2:
                if n2 < n1:
                    s1 = min(s1, s[:i-1] + s[i] + s[i-1] + s[i+1:])
        return min(s,s1)
