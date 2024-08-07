class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        
        rowFlips = columnFlips = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])//2):
                if grid[i][j]!= grid[i][-(j+1)]:
                    rowFlips += 1
                    
        for j in range(len(grid[0])):
            for i in range(len(grid)//2):
                if grid[i][j] != grid[-(i+1)][j]:
                    columnFlips += 1
        
        return min(rowFlips, columnFlips)
