class Solution:
    def isValid(self, s: str) -> bool:
        while s:
            r = s.replace("abc","")
            if s==r:
                return False
            s = r
        return True
