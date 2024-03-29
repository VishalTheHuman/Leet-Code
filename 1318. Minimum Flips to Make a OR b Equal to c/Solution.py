class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a, b, c = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        max_len = max(len(a), len(b), len(c))
        a, b, c = a.zfill(max_len), b.zfill(max_len), c.zfill(max_len)
        flips = 0
        for i in range(max_len):
            if c[i]=="1":
                flips += (a[i]!="1" and b[i]!="1")
            else:
                flips += (a[i]=="1") + (b[i]=="1")
        return flips
