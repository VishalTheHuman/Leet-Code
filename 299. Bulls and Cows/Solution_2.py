class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        dt = defaultdict(int)
        ind = set()
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
                ind.add(i)
            else:
                dt[secret[i]]+=1
        cows = 0
        for i,j in enumerate(guess):
            if i not in ind:
                val = dt[j] 
                if val:
                    cows+=1
                    dt[j]-=1
        return f"{str(bulls)}A{str(cows)}B"
