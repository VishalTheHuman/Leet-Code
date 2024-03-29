# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.s = 0
        self.dfs(root)
        return self.s
    def dfs(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        l,r = self.dfs(root.left) ,self.dfs(root.right)
        self.s += abs(l-r)
        return root.val + l + r
