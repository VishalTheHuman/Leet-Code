class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = curr_depth = 0
        for x in s:
            if x == "(":
                curr_depth += 1
                if curr_depth > max_depth:
                    max_depth = curr_depth
            elif x == ")":
                curr_depth -= 1
        return max_depth 
