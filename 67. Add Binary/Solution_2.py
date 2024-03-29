class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        carry = 0
        result = ""
        a = a.zfill(max_len) 
        b = b.zfill(max_len) 
        for i in range(max_len - 1, -1, -1):
            s = carry 
            s += (a[i]=="1")
            s += (b[i]=="1")
            result += ("1" if (s % 2) == 1 else "0")
            carry = (s==2 or s==3)
        if carry:
            result += "1"
        return result[::-1]
