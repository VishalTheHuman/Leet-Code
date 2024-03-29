# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.dfs(root)
        return self.count

    def dfs(self,root):
        if not root:
            return 0,0
        leftSum, leftNodes = self.dfs(root.left)
        rightSum, rightNodes = self.dfs(root.right)
        allSum = leftSum + rightSum + root.val
        allNodes = 1 + leftNodes + rightNodes
        if allSum//allNodes == root.val:
            self.count+=1
        return allSum, allNodes
