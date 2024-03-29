class Solution:
    def integerReplacement(self, n: int) -> int:
        def recurse(n):
            if n == 1:
                return 0
            else:
                if n%2:
                    v1 = recurse(n-1)
                    v2 = recurse(n+1)
                    return 1 + min(v1,v2)
                else:
                    return 1 + recurse(n//2)  
        return recurse(n)
