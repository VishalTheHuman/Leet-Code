class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = l = 0
        length = 0
        seen = set()
        while r<len(s):
            if s[r] in seen:
                length = max(r-l,length)
                l+=1
                r = l
                seen.clear()
                continue
            seen.add(s[r])
            r+=1
        length = max(length,r-l)
        return length
