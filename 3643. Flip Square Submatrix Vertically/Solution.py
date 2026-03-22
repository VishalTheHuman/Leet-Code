class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for j in range(y,y+k): 
            temp = k-1
            for i in range(x,x+(k//2)): 
                grid[i][j], grid[i+temp][j] = grid[i+temp][j], grid[i][j]
                temp -= 2
        return grid
