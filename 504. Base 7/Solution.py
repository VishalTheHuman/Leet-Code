class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        neg = False
        if num < 0:
            neg = True
            num *= -1
        result = ""
        while num>=7: 
            val = num % 7 
            result += str(val)
            num //= 7
        result += (str(num) if num > 0 else "") 
        result = result[::-1]
        if neg:
            return "-"+result
        return result
