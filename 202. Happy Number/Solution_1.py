class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while True:
            s = 0
            num = n
            while num:
                s += ((num)%10)**2
                num//=10
            if s == 1:
                return True
            if s in seen:
                return False
            seen.add(s)
            n = s
        return False
        
