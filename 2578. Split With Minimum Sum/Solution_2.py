class Solution:
    def splitNum(self, num: int) -> int:
        num = sorted(str(num))
        num1 = int("".join([num[i] for i in range(0,len(num),2)]))
        num2 = int("".join([num[i] for i in range(1,len(num),2)]))
        return num1 + num2
