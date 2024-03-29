class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def perms(n,string=""):
            nonlocal k
            if n==0:
                return ""
            ls = []
            for x in "abc":
                if string==x:
                    continue
                else:
                    p = perms(n-1,x)
                    if p:
                        for i in p:
                            ls.append(i+x)
                    else:
                        ls.append(x)
            return ls
        l = sorted(perms(n))
        return l[k-1] if len(l) >= k else ""
