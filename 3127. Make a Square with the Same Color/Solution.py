class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        w = b = 0
        def check(i,j):
            dt = defaultdict(int)
            moves = [
                (0,0),
                (0,1),
                (1,0),
                (1,1)
            ]
            for move in moves:
                dt[grid[i+move[0]][j+move[1]]] += 1
            return dt["W"], dt["B"]
        for i in range(2):
            for j in range(2):
                w = b = 0
                w,b = check(i,j)
                if w >= 3 or b >= 3:
                    return True
        return False        
