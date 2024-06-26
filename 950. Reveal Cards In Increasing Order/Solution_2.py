class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = deque(sorted(deck))
        to_fill = deque([i for i in range(len(deck))])
        result = [None]*len(deck)
        while to_fill:
            idx = to_fill.popleft()
            if to_fill:
                to_fill.append(to_fill.popleft())
            result[idx] = deck.popleft()
        return result
