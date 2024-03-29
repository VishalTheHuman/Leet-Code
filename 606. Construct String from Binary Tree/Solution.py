# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = ""
        def dfs(root):
            nonlocal string
            string += str(root.val)
            if root.left is None and root.right is None:
                return 
            if root.left:
                string+="("
                dfs(root.left)
                string+=")"
            else:
                string+="()"
            if root.right:
                string+="("
                dfs(root.right)
                string+=")"
        dfs(root)
        return string
