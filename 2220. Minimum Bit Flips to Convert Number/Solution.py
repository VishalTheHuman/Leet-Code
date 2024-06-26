class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        max_len = max(len(start), len(goal))
        start = start.zfill(max_len)
        goal = goal.zfill(max_len)
        return sum(x!=y for x, y in zip(start, goal))
