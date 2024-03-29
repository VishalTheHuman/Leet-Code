class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def log2(num):
            if num < 1:
                return False
            if num == 1:
                return True
            if num%2:
                return False
            return log2(num/2)
        return log2(n)
