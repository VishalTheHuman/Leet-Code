class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while n!=1:
            n = sum(int(x)**2 for x in str(n))
            if n in seen:
                return False
            seen.add(n)
        return True
