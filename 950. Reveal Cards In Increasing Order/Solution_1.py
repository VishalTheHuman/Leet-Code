class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = deque(sorted(deck))
        result = [None]*len(deck)
        to_fill = [i for i in range(len(deck))]
        put = True
        while to_fill:
            new_fill = []
            for x in to_fill:
                if put:
                    result[x] = deck.popleft()
                else:
                    new_fill.append(x)
                put = not put
            to_fill = new_fill
        return result
