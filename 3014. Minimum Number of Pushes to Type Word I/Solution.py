class Solution:
    def minimumPushes(self, word: str) -> int:
        l = len(word)
        return sum(i*8 for i in range(1, (l//8)+1)) + ((l%8) * ((l//8)+1))
