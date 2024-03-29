class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for x in tokens:
            if x in "+-*/":
                v1 = stk.pop()
                v2 = stk.pop()
                val = 0
                if x=="+":
                    val = v1 + v2
                elif x=="-":
                    val = v2 - v1
                elif x=="*":
                    val = v2*v1
                elif x=="/":
                    val = v2/v1
                    val = int(val)
                stk.append(val)
            else:
                stk.append(int(x))
        return stk[0]
