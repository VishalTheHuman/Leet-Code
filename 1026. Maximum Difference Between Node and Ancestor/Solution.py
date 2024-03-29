# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root,min_val,max_val):
            if not root:
                return max_val-min_val
            min_val =  min(min_val,root.val)
            max_val =  max(max_val,root.val)
            l = dfs(root.left,min_val,max_val)
            r = dfs(root.right,min_val,max_val)
            return max(l,r)
        return dfs(root,root.val,root.val)
