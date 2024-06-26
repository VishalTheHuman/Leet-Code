class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        
        h = [1000,-1]
        v = [1000,-1]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    h[0],h[1] = min(h[0],j), max(h[1],j)
                    v[0],v[1] = min(v[0],i), max(v[1],i)
        return (h[1]-h[0]+1) * (v[1]-v[0]+1)
