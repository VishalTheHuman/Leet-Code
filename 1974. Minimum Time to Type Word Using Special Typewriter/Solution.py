class Solution:
    def minTimeToType(self, word: str) -> int:
        ptr = "a"
        time = 0
        for x in word:
            v1 = abs(ord(ptr)-ord(x))
            v2 = 26 - v1
            time += (1 + min(v1,v2))
            ptr = x
        return time
