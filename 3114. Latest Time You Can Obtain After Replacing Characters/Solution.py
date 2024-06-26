class Solution:
    def findLatestTime(self, s: str) -> str:
        s = s.split(":")
        if s[0][0]=="?":
            s[0] = ("1" if s[0][1] in ["0","1", "?"] else "0") + s[0][1]
        if s[0][1] == "?":
            s[0] = "11" if s[0][0] == "1" else "09"
        if s[1][0] == "?":
            s[1] = "5" + s[1][1]
        if s[1][1] == "?":
            s[1] = s[1][0] + "9"
        return ":".join(s)
