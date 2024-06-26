# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        found = False
        def dfs(root):
            nonlocal found
            if not root or found:
                return

            if root.val == subRoot.val:
                found = check(root, subRoot)

            dfs(root.left)
            dfs(root.right)

        def check(r1, r2):
            if (not r1 and r2) or (not r2 and r1):
                return False 
            if not r1 and not r2:
                return True
            return (r1.val == r2.val) and check(r1.left, r2.left) and check(r1.right, r2.right)
        
        dfs(root)
        return found
