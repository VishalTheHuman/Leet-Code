class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = sum(int(i) for i in str(x))
        return -1 if x%s!=0 else s
