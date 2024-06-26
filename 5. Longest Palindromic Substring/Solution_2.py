class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0 
        string = ""

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if max_length < r-l+1:
                max_length = r-l+1
                string = s[l+1:r]
            
            
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if max_length < r-l+1:
                max_length = r-l+1
                string = s[l+1:r]
        return string
