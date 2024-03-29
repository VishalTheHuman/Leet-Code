class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for i in range(32):
            result += 1 & (n>>i)
        return result
