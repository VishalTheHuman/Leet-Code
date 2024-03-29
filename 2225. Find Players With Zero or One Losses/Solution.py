class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser = defaultdict(int)
        winner = defaultdict(int)
        for i in range(len(matches)):
            loser[matches[i][1]]+=1
            winner[matches[i][0]]+=1
        ls = [[],[]]
        for k,v in loser.items():
            if v ==1:
                ls[1].append(k)
        for k in winner:
            if k not in loser:
                ls[0].append(k)
        ls[0].sort()
        ls[1].sort()
        return ls
