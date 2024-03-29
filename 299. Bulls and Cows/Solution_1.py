class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        sec,gus = {},{}
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
            else:
                sec[secret[i]] = sec.get(secret[i],0)+1
                gus[guess[i]] = gus.get(guess[i],0)+1
        cows = 0
        for k,v in sec.items():
            s = v
            g = gus.get(k,None)
            if s and g:
                cows += min(g,s)
        return f"{str(bulls)}A{str(cows)}B"
