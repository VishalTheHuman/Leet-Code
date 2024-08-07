class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x : x[0])
        result = [intervals[0]]
        for x,y in intervals[1:]:
            if x<=result[-1][1]:
                result[-1][1] = max(result[-1][1], y)
            else:
                result.append([x,y])
        return result
