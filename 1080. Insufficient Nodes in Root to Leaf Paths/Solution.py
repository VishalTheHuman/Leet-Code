# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        head = root 
        def dfs(root, s = 0):
            
            if not root.left and not root.right:
                return (s + root.val) >= limit

            left = right = False
            if root.left:
                left = dfs(root.left, s + root.val)
            if root.right:
                right = dfs(root.right, s + root.val)
            if not left:
                root.left = None
            if not right:
                root.right = None
            return left or right 
    
        if dfs(root):
            return head
        return None
        
