class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []
        def dfs(n,curr = ""):
            if n == 0:
                result.append(curr)
                return
            if curr[-1] == "0":
                dfs(n-1, curr + "1")
            else:
                dfs(n-1, curr + "0")
                dfs(n-1, curr + "1")
        dfs(n-1,"0")
        dfs(n-1,"1")
        return result
