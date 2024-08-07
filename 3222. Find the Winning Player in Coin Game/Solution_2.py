class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        turn = True
        
        while x and y:
            if turn:
                if y < 4:
                    return "Bob"
                y-=4
                turn = False
            else:
                if y < 4:
                    return "Alice"
                y-=4
                turn = True
            x-=1
    
        return "Alice" if not turn else "Bob"
