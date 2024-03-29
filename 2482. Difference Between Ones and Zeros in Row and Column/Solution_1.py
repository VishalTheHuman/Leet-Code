class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row, col = len(grid), len(grid[0])
        rows = [2*sum(grid[i])-row for i in range(len(grid))]
        cols = [2*sum(grid[i][j] for i in range(len(grid)))-col for j in range(len(grid[0]))]
        diff = []
        for i in range(row):
            arr = []
            for j in range(col):
                arr.append(cols[j]+rows[i])
            diff.append(arr)
        return diff
