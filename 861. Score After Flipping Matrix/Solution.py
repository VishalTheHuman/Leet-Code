class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[i])):
                    grid[i][j] = 0 if grid[i][j] else 1
        
        rows = len(grid)
        for j in range(len(grid[0])):
            zeros = 0
            for i in range(len(grid)):
                if grid[i][j] == 0:
                    zeros += 1
            if rows - zeros < zeros:
                for i in range(len(grid)):
                    grid[i][j] = 0 if grid[i][j] else 1
        return sum(int("".join(list(map(str,x))),2) for x in grid)
        
