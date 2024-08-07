class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_num = "0"*100
        for idx, num in enumerate(number):
            if num == digit:
                val = number[:idx]+number[idx+1:]
                if val > max_num:
                    max_num = val
        return str(max_num)
