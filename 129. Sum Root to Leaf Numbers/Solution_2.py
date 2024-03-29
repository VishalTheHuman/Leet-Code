# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode],sum_ = 0) -> int:
        totalSum = [0]
        def dfs(root,number=""):
            if not root:
                return
            number+=str(root.val)
            if root.left is None and root.right is None:
                totalSum[0] += int(number)
                return
            dfs(root.left,number)
            dfs(root.right,number)
        dfs(root)
        return totalSum[0]
