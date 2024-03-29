class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        dt = Counter([v - int(str(v)[::-1]) for v in nums])
        return sum(val*(val-1)//2 for val in dt.values()) % (10**9 + 7)
