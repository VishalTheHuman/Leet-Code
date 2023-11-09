class Solution:
    def isValid(self, s: str) -> bool:
        while s:
            found = False
            for i in range(len(s)-2):
                if s[i:i+3]=="abc":
                    found = True
                    s = s[:i]+s[i+3:]
                    break
            if not found:
                return False
        return True
