class Solution:
    def integerReplacement(self, n: int) -> int:
        def recurse(n):
            if n == 1:
                return 0
            else:
                if n%2:
                    if (n+1)%4 == 0 and n+1!=4:
                        return 1 + recurse(n+1)
                    else:
                        return 1 + recurse(n-1)
                else:
                    return 1 + recurse(n//2)  
        return recurse(n)
