class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dt = {}
        for i in range(len(s)):
            if s[i] not in dt:
                if t[i] not in dt.values():
                    dt[s[i]] = t[i]
                else:
                    return False
            elif dt[s[i]]!=t[i]:
                return False
        return True
