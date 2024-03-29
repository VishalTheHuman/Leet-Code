class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)[::-1]
        num2 = num2.zfill(max_len)[::-1]
        result = ""
        for i in range(max_len):
            s = carry
            s += (ord(num1[i])-ord("0"))
            s += (ord(num2[i])-ord("0"))
            result += str(s%10)
            if s>=10:
                carry = s//10
            else:
                carry = 0
        if carry:
            result+=str(carry)
        return result[::-1]
