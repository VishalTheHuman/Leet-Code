class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        string = ""
        curr = 0
        while curr<=len(s):                
            string = string + (s[curr:curr+k] if i%2 else s[curr:curr+k][::-1])
            curr +=k
            i+=1
        return string
