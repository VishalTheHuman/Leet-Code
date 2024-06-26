class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        count = defaultdict(int)
        for i in range(0, len(word), k):
            count[word[i:i+k]] += 1
        return len(word)//k - max(count.values())
