class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        table = defaultdict(list)
        for idx, val in enumerate(cards):
            table[val].append(idx)
        
        minimum = float("inf")
        for y in table.values():
            for i in range(1,len(y)):
                dis = y[i]-y[i-1]+1
                if dis < minimum:
                    minimum = dis
        return minimum if minimum < float("inf") else -1
