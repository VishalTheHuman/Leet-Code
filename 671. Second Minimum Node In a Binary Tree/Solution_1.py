# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ls = []
        def dfs(root):
            if not root:
                return 
            if root.val not in ls:
                ls.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        ls.sort()
        if len(ls)>1:
            return ls[1] 
        return -1
