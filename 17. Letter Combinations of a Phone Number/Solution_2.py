class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        def tree(original, string=""):
            if not original:
                possible.append(string)
                return
            for x in mapping[original[0]]:
                tree(original[1:],string+x)

        def buildMapping():
            dt = {}
            s = string.ascii_letters[:26]
            ind = 0
            for i in range(2,10):
                if i==7 or i==9:
                    dt[str(i)] = s[ind:ind+4]
                    ind+=4
                else:
                    dt[str(i)] = s[ind:ind+3]
                    ind+=3
            return dt
        mapping = buildMapping()
        possible = []
        tree(digits)
        return possible
