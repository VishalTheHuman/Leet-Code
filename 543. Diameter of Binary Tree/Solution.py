# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if not root:
                return 0
            nonlocal diameter
            l = traverse(root.left)
            r = traverse(root.right)
            diameter = max(diameter, l + r)
            return max(l,r) + 1
        diameter = 0
        traverse(root)
        return diameter
