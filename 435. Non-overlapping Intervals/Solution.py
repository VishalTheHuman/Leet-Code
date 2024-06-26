class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x  : x[1])
        s,e = intervals[0]
        count = 1
        for i in range(1,len(intervals)):
            itvl = intervals[i]
            if itvl[0] >= e:
                count += 1
                s,e = itvl
        return len(intervals) - count
