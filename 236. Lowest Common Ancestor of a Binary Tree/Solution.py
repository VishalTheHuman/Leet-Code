# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = None
        def dfs(node):
            # Non - Local Values
            nonlocal ancestor, p, q
            # Base Cases
            if not node:
                return False
            # Recursion
            l = dfs(node.left)
            r = dfs(node.right)
            # Validation
            if ancestor:
                return True
            if (node == p or node == q) and not (l or r):
                return True
            elif (node == p or node == q) and (l or r):
                ancestor = node
                return True
            elif l and r:
                ancestor = node
            return l or r
        dfs(root)
        return ancestor
