class Solution:
    def doesAliceWin(self, s: str) -> bool:
        odd = even = 0
        
        # True (Odd) False (Even)
        
        turn = True 
        
        while s:
            vowelCount = 0
            odd = -1
            even = 1 if s[0] not in "aeiou" else -1
            for i in range(len(s)):
                if s[i] in "aeiou":
                    vowelCount += 1
                    if vowelCount % 2 == 1:
                        odd = i+1
                    else:
                        even = i+1
            
            if turn and odd == -1: 
                return False
            
            if turn and vowelCount % 2 == 1:
                return True
            elif not turn and vowelCount % 2 == 0:
                return False
            
            if turn:
                s = s[odd:]
            elif even!= -1:
                s = s[even:]
            else:
                return True

            turn = not turn 

        return not turn 
                
