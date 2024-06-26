class Solution:
    def calculate(self, s: str) -> int:
        def solve(arr):
            if len(arr) == 1:
                return arr[0]
            ptr = ans = negative = 0
            for x in arr:
                if type(x) is int:
                    ans += (-1 if negative else 1)*x
                    negative = False
                else:
                    negative = (x=="-")
            return ans

        num = ""
        stack = []
        for x in s:
            if x == " ":
                continue
            elif x in "()-+":
                if x in "+-":
                    if num:
                        stack.append(int(num))
                    num = ""
                if x != ")":
                    stack.append(x)
                else:
                    if num:
                        stack.append(int(num))
                        num = ""
                    ptr = len(stack)-1
                    while ptr >= 0 and stack[ptr]!="(":
                        ptr -= 1
                    ans = solve(stack[ptr+1:])
                    stack = stack[:ptr]
                    stack.append(ans)
            else:
                num += x
        if num:
            stack.append(int(num))
        return solve(stack)
