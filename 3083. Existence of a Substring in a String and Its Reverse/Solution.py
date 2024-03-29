class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        table = set()
        reverse = set()
        for j in range(0, len(s)-2+1):
            if s[j:j+2][::-1] in table or s[j:j+2] in reverse or s[j:j+2][::-1]==s[j:j+2]:
                return True
            table.add(s[j:j+2])
            reverse.add(s[j:j+2][::-1])
        return False
