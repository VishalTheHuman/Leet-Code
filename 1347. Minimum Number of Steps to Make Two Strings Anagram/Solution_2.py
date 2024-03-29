class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s1 = [0]*26
        t1 = [0]*26
        for i in range(len(s)):
            s1[ord(s[i])-ord('a')]+=1
            t1[ord(t[i])-ord('a')]+=1
        diff = 0
        for i in range(26):
            diff+=abs(s1[i]-t1[i])
        return diff//2
