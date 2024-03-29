class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        repeated = None
        missing = None
        dt = defaultdict(int)
        for x in grid:
            for y in x:
                dt[y]+=1
        for i in range(1,len(grid)**2+1):
            if repeated and missing:
                break
            if i not in dt:
                missing = i
            elif dt[i]==2:
                repeated = i
        return repeated, missing
