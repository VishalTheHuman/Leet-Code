class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        itr = set(list(word1+word2))
        word1 = Counter(word1)
        word2 = Counter(word2)
        for i in itr:
            val = abs(word1.get(i,0)-word2.get(i,0))
            if val > 3:
                return False
        return True
