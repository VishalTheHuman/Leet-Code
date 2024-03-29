class Solution:
    def isPathCrossing(self, path: str) -> bool:
        weights = {
            "N":(0,1),
            "E":(1,0),
            "S":(0,-1),
            "W":(-1,0)
        }
        paths = [[0,0]]
        curr = [0,0]
        for side in path:
            move = weights[side]
            curr[0]+=move[0]
            curr[1]+=move[1]
            if curr in paths:
                return True
            paths.append(curr[:])
        return False
