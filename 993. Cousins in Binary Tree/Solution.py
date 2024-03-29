# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(root, val, parent = None, depth = 0):
            if not root:
                return
            if root.val == val:
                return parent, depth+1
            depth+=1
            parent = root
            r = dfs(root.right, val, parent, depth)
            l = dfs(root.left, val, parent, depth)
            return r if r else l
        c1 = dfs(root,x)
        c2 = dfs(root,y)
        if c1[0]==c2[0] or c1[1]!=c2[1]:
            return False
        return True
