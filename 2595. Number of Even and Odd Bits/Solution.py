class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = odd = 0
        for ind, x in enumerate(bin(n)[2:][::-1]):
            if ind % 2 == 0:
                even += (x=="1")
            else:
                odd += (x=="1")
        return even, odd
