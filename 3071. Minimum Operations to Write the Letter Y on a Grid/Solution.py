class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        mid = len(grid)//2
        y_count = [0]*3
        
        # \
        for i in range(mid):
            y_count[grid[i][i]] += 1
            
        # / 
        j = 0
        for i in range(len(grid)-1, mid, -1):
            y_count[grid[j][i]] += 1
            j += 1 
        
        # |
        for i in range(mid, len(grid)):
            y_count[grid[i][mid]] += 1
        
        count = [-x for x in y_count]
        for x in range(len(grid)):
            count[0] += grid[x].count(0)
            count[1] += grid[x].count(1)
            count[2] += grid[x].count(2)
        
        minimum = float('inf')
        for i in range(3):
            in_y = sum(y_count[:i] + y_count[i+1:])
            out_y = count[i] + min(count[(i+1)%3], count[(i+2)%3])
            minimum = min(minimum, in_y + out_y)
            
        return minimum
