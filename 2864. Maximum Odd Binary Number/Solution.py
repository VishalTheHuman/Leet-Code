class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        dt = Counter(s)
        return (dt["1"]-1)*"1" + dt["0"]*"0" + "1"
        
