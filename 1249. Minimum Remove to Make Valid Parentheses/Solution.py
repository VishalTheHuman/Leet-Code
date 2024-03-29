class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        valid = ""
        opened = 0
        for x in s:
            if x == "(":
                valid += x
                opened += 1
            elif x == ")":
                if opened:
                    valid += x
                    opened -= 1
            else:
                valid += x
        return valid[::-1].replace("(", "", opened)[::-1]
