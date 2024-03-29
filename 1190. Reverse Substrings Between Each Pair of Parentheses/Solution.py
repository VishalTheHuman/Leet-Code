class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        i = 0
        while i < len(s):
            if s[i]==")":
                string = ""
                while stk[-1] != "(":
                    string += stk.pop()
                stk.pop()
                j = 0
                while j <len(string):
                    stk.append(string[j])
                    j+=1
            else:
                stk.append(s[i])
            i+=1
        return "".join(stk)
