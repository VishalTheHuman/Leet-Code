class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""
        i = 1
        count = 1
        prev = s[0]
        while i < len(s):
            while i < len(s):
                if prev:
                    if s[i]!=prev:
                        break
                prev = s[i]
                count += 1
                i += 1
            if count >2:
                count = 2
            ans += s[i-1]*count
            count = 0
            prev = ""
        return ans if ans else s
