class Solution:
    def minOperations(self, n: int) -> int:
        if n%2:
            return sum(2*i for i in range(1,n//2 + 1))
        return sum(2*i + 1 for i in range(n))//4
