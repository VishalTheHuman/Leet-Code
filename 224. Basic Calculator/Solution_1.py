class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        ans = num = 0
        sign = 1
        for x in s:
            if x == '(':
                stack.append(ans)
                stack.append(sign)
                ans,sign =0,1
            elif x.isdigit():
                num = 10*num + int(x)
            elif x in '+-':
                ans += num*sign
                num =0
                sign = -1 if x=='-' else 1
            elif x == ')':
                ans += num*sign
                ans *= stack.pop()
                ans += stack.pop()
                num=0
        return ans + sign*num
        
