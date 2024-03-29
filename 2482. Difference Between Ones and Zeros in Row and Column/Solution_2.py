class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = [sum(grid[i]) for i in range(len(grid))]
        cols = [sum(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]
        diff = []
        row, col = len(grid), len(grid[0])
        for i in range(row):
            arr = []
            for j in range(col):
                arr.append(2*(cols[j]+rows[i]) - (row+col))
            diff.append(arr)
        return diff
