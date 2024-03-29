class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win, lose = defaultdict(int), defaultdict(int)
        for w,l in matches:
            win[w] += 1
            lose[l] += 1
        answer = [[],[]]
        answer[0] = sorted([x for x in win.keys() if x not in lose])
        answer[1] = sorted([x for x,y in lose.items() if y==1])
        return answer
