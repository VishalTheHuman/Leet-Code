class Solution:
    def minPartitions(self, n: str) -> int:
        max_times = 1
        n = set(n)
        for x in "987654321":
            if x in n:
                return int(x)
        return 1
