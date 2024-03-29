class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                break
            ch = s[i]
            while i < j and s[i]==ch:
                i += 1
            if i == j:
                return 0
            while i < j and s[j] == ch:
                j -= 1
        return j-i+1
