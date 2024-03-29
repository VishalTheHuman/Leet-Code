class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        two_power = set()
        i = 0
        while True:
            if 2**i > 10e9:
                break
            two_power.add(".join(sorted(str(2**i))))
            i += 1
        n = ".join(sorted(str(n)))
        return n in two_power
