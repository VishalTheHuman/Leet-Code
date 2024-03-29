# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root,prev_val):
            nonlocal count
            if root.val >=prev_val:
                count+=1
                val = root.val
            else:
                val = prev_val
            if root.left:
                dfs(root.left,val)
            if root.right:
                dfs(root.right,val)
        dfs(root,root.val)
        return count
