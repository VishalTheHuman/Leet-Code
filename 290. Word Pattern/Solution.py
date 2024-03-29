class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s)!=len(pattern):
            return False
        dt = {}
        for i in range(len(s)):
            if pattern[i] not in dt:
                if s[i] not in dt.values(): 
                    dt[pattern[i]] = s[i]
                else:
                    return False
            elif dt[pattern[i]] != s[i]:
                return False
        return True
