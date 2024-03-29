class Solution:
    def myPow(self, x: float, n: int) -> float:
        #########################
        def power(x, n):
            if n == 0:
                return 1
            val = power(x,n//2) 
            val *= val
            if n%2:
                val *= x
            return val
        #########################
        flag = None
        if n < 0:
            flag = True
            n*=(-1)
        val = power(x, n)
        if flag:
            return 1 / val
        return val
