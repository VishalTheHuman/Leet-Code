class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = []
        for i in range(n-2):
            a = []
            for j in range(n-2):
                a.append(max(max(x[j:j+3]) for x in grid[i:i+3]))
            result.append(a) 
        return result
