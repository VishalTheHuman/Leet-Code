# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0 
        count = 0
        def dfs(root,ancestors=[]):
            nonlocal count, targetSum
            ancestors.append(root.val)
            for i in range(0,len(ancestors)):
                if sum(ancestors[i:])==targetSum:
                    count+=1
            if root.left:
                dfs(root.left,ancestors.copy())
            if root.right:
                dfs(root.right,ancestors.copy()) 
        dfs(root)
        return count
