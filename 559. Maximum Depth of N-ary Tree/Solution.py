"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root,lvl =1) -> int:
        if not root:
            return 0
        def dfs(root,lvl=1):
            if not root:
                return lvl
            ls = [lvl]
            for node in root.children:
                ls.append(dfs(node,lvl+1))
            return max(ls)
        return dfs(root)
