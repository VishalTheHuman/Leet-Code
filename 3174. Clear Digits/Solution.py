
class Solution:
    def clearDigits(self, s: str) -> str:
        stk = []
        for x in s:
            if x in "1234567890":
                if stk:
                    stk.pop()
            else:
                stk.append(x)
        return "".join(stk)
