# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        def dfs(root):
            nonlocal lca, p, q
            if not root:
                return False
            l = dfs(root.left)
            r = dfs(root.right)
            if l and r:
                lca = root
                return False
            elif root == p or root == q:
                if (l or r):
                    lca = root
                    return False
                else:
                    return True
            
            return l or r
        dfs(root)
        return lca
