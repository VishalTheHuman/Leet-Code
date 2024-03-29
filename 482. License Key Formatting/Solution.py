class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        hold = ""
        val = len(s) % k
        if len(s) % k:
            hold = s[:val]
            s = s[val:]
        ans = []
        for i in range(0,len(s)-k+1, k):
            ans.append(s[i:i+k])
        if hold:
            ans.insert(0,hold)
        return "-".join(ans)
