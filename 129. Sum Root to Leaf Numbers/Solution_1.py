# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode],sum_ = 0) -> int:
        self.totalSum = 0
        self.dfs(root)
        return self.totalSum
    
    def dfs(self,root,number=""):
        if not root:
            return
        number+=str(root.val)
        if root.left is None and root.right is None:
            self.totalSum += int(number)
            return
        self.dfs(root.left,number)
        self.dfs(root.right,number)
