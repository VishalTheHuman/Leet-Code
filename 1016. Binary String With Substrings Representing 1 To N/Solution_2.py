class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1,n+1):
            try:
                s.index(bin(i)[2:])
            except:
                return False
        return True
