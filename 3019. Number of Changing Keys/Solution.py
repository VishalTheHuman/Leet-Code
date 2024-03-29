class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        curr_key = s[0]
        count = 0
        for i in range(1,len(s)):
            if curr_key!=s[i]:
                count+=1
            curr_key = s[i]
        return count
