class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return sum(1 for x in s[:len(s)//2] if x in "AEIOUaeiou") == sum(1 for x in s[len(s)//2:] if x in "AEIOUaeiou")
