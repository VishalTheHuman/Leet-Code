class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            nonlocal seen, count
            moves = [
                (0,1), 
                (1,0), 
                (0,-1),
                (-1,0)
            ]
            seen.add((i,j))
            for move in moves: 
                idx_i = i + move[0]
                idx_j = j + move[1]
                if 0 <= idx_i < len(grid) and 0 <= idx_j < len(grid[0]):
                    if (idx_i, idx_j) not in seen:
                        if grid[idx_i][idx_j] == 1:
                            dfs(idx_i, idx_j)
                        else:
                            count += 1
                else:
                    count += 1
        start_i = start_j = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start_i = i
                    start_j = j
                    break
        seen = set()
        count = 0
        dfs(start_i, start_j)
        return count
