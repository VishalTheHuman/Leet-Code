class Solution:
    def longestPalindrome(self, s: str) -> int:
        s = sorted(Counter(s).values(), reverse = True)
        odds = True
        length = 0
        for x in s:
            if x % 2 == 0:
                length += x
            elif odds:
                length += x
                odds = False
            else:
                length += (x-1)
        return length
