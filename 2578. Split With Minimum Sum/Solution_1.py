class Solution:
    def splitNum(self, num: int) -> int:
        num = "".join(sorted(str(num)))
        num1 = int(num[::2])
        num2 = int(num[1::2])
        return num1 + num2
