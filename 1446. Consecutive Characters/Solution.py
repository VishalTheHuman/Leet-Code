class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        max_count = 1
        i = 1
        while i < len(s):
            if s[i-1]==s[i]:
                count+=1
            else:
                max_count = max(count,max_count)
                count = 1
            i+=1
        max_count = max(count,max_count)
        return max_count
