class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        moves = {
            "U" : (-1,0), 
            "D" : (1,0),
            "R" : (0,1),
            "L" : (0,-1)
        }
        arr = [0]*len(s)
        for i in range(len(s)):
            count = 0 
            x, y = startPos
            for ch in s[i:]:
                move = moves[ch]
                x += move[0]
                y += move[1]
                if x < 0 or x >= n or y < 0 or y >= n:
                    break
                count += 1
            arr[i] = count
        return arr
