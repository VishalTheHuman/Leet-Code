class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        l = len(words)
        words = "".join(words)
        s = set(words)
        for x in s:
            if words.count(x)%l!=0:
                return False
        return True
