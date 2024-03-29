class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        count = 0
        for x in s:
            if x in seen:
                count+=1
                seen.clear()
                seen.add(x)
            else:
                seen.add(x)
        if seen:
            count+=1
        return count
