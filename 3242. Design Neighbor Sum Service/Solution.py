class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.indexStore = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.indexStore[grid[i][j]] = [i,j]
                

    def adjacentSum(self, value: int) -> int:
        i, j = self.indexStore[value]
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        adjSum = 0
        for nxt_i, nxt_j in moves:
            if 0<=i+nxt_i<len(self.grid) and 0<=j+nxt_j<len(self.grid[0]):
                adjSum += self.grid[i+nxt_i][j+nxt_j]
        return adjSum
                

    def diagonalSum(self, value: int) -> int:
        i, j = self.indexStore[value]
        moves = [(1,1), (1,-1), (-1,-1), (-1,1)]
        diagSum = 0
        for nxt_i, nxt_j in moves:
            if 0<=i+nxt_i<len(self.grid) and 0<=j+nxt_j<len(self.grid[0]):
                diagSum += self.grid[i+nxt_i][j+nxt_j]
        return diagSum


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
