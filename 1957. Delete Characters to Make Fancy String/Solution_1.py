class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = s[0]
        count = 0
        ans = ""
        for x in s:
            if x != prev:
                count = 2 if count > 2 else count
                ans += prev*count
                count = 1
            else:
                count += 1
            prev = x
        if count > 2:
            count = 2
        ans += prev*count
        return ans
