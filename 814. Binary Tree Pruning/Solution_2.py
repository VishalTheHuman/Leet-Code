# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return None,0
            if root.val!=1:
                count = 0
            else:
                count = 1
            root.left,l = dfs(root.left)
            root.right,r = dfs(root.right)
            count+=(l+r)
            if count==0:
                return None,0
            return root,count
        root,count = dfs(root)
        return root if count else None
