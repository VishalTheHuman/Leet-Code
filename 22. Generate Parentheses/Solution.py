class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #######################################
        def generate(opened = 1, closed =0, string = "("):
            if opened == n and closed == n:
                result.append(string)
                return
            if opened < n:
                generate(opened+1, closed, string+"(")
            if closed < opened:
                generate(opened, closed+1, string+")")
        #######################################
        result = []
        generate()
        return result
