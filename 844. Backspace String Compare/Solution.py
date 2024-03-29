class Solution:
    def helper(self,string):
        stk = []
        for x in string:
            if x == "#":
                if stk:
                    stk.pop()
                continue
            stk.append(x)
        return stk

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.helper(s) == self.helper(t)
