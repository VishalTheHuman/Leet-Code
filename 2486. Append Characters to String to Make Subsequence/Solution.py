class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for ch in s:
            if i == len(t):
                break
            if ch==t[i]:
                i+=1
        return len(t)-i
