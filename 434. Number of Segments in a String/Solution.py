class Solution:
    def countSegments(self, s: str) -> int:
        i = 0
        count = 0
        curr = ""
        while i < len(s):
            if s[i]!=" ":
                curr+=s[i]
            elif curr:
                count+=1
                curr = ""
            i+=1
        if curr:
            count+=1
        return count
