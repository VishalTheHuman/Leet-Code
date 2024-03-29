class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dt = {}
        for num in arr:
            total_ones = bin(num).count("1")
            dt[total_ones]  = dt.get(total_ones,[]) + [num]
        ls = []
        for x in sorted(dt.keys()):
            ls += sorted(dt[x])
        return ls
