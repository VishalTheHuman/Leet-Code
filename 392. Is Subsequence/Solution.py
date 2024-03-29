class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_ind = s_ind = 0
        while t_ind < len(t) and s_ind < len(s):
            if t[t_ind]==s[s_ind]:
                s_ind+=1
            t_ind+=1
        return s_ind == len(s)
