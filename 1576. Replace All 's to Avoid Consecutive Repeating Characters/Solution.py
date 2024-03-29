class Solution:
    def modifyString(self, s: str) -> str:
        s = s + "0"
        ans = "0"
        to_be = string.ascii_letters[:26]
        for i in range(len(s)-1):
            if s[i] != "?":
                ans += s[i]
            else:
                fill = "a"
                ptr = 1
                while fill == ans[-1] or fill == s[i+1]:
                    fill = to_be[ptr]
                    ptr += 1
                ans += fill
        return ans[1:]
