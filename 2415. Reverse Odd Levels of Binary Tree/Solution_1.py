# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode],isOdd = True) -> Optional[TreeNode]:
        def helper(left,right,isOdd = True):
            if not left and not right:
                return
            if isOdd:
                left.val,right.val = right.val, left.val
            helper(left.left, right.right, not isOdd)
            helper(left.right,right.left, not isOdd)
        helper(root.left,root.right)
        return root
