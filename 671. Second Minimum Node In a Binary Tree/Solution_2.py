# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        s = set()
        def dfs(root):
            if not root:
                return 
            s.add(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        s = sorted(s)
        if len(s)>1:
            return s[1] 
        return -1
