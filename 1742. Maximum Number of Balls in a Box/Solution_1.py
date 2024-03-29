class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dt = defaultdict(int)
        for i in range(lowLimit,highLimit+1):
            count = 0
            while i > 0:
                count+=(i%10)
                i//=10
            dt[count]+=1
        return max(dt.values())
