class Solution:
    def numSteps(self, s: str) -> int:
        # Odd - Add 1 Bit
        # Even - Left shift by 1
        steps = 0
        s = list(s)
        while len(s) > 1:
            if s[-1] == "1":
                s[-1] = "0"
                i = len(s)-2
                put = False
                while i >= 0:
                    if s[i] == "1":
                        s[i] = "0"
                    else:
                        put = True
                        s[i] = "1"
                        break
                    i -= 1
                if not put:
                    s.insert(0,"1")
            else:
                s.pop()
            print(s)
            steps += 1
        return steps
            
                
