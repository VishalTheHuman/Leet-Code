class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        pairs = 0
        seen = [0]*24
        for x in hours:
            x %= 24
            if x:
                pairs += seen[24-x] 
            else:
                pairs += seen[0]
            seen[x] += 1
        return pairs
