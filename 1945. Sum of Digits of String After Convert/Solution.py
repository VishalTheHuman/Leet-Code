class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ""
        for ch in s:
            num+=str(ord(ch)-ord("a")+1)
        n = 0
        for i in range(k):
            num = "".join(str(sum([int(c) for c in num])))
        return int(num)
