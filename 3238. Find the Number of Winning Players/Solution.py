class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        won = set()
        players = [defaultdict(int) for _ in range(n+1)]
        for p, b in pick:
            players[p][b] += 1
            if players[p][b] > p:
                won.add(p)
        return len(won)
