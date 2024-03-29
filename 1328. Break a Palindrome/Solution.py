class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ""
        for i in range(len(palindrome)):
            if palindrome[i] > "a":
                curr = palindrome[:i] + "a" + palindrome[i+1:]
                if curr != curr[::-1]:
                    return curr
        return palindrome[:-1] + "b"
