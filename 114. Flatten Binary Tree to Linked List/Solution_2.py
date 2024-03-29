# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return []
        self.stk = []
        self.dfs(root)
        node = self.stk.pop(0)
        node.left = None
        while self.stk:
            n = self.stk.pop(0)
            node.right = n
            node = node.right
            node.left = None
        return root

    def dfs(self,root):
        if not root:
            return
        self.stk.append(root)
        self.dfs(root.left)
        self.dfs(root.right)
