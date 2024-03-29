class Solution:
    def frequencySort(self, s: str) -> str:
        dt = {}
        seen = set()
        for x in s:
            if x not in seen:
                count = s.count(x)
                dt[count] = dt.get(count,[]) + [x]
                seen.add(x)
        s = ""
        for x in sorted(dt.keys(),reverse=True):
            for y in dt[x]:
                s += (x*y)
        return s
