class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dt = defaultdict(int)
        for i in range(lowLimit,highLimit+1):
            val = sum(int(x) for x in str(i))
            dt[val]+=1
        return max(dt.values())
