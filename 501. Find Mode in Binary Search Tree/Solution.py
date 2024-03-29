# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dt = {}
        def dfs(root):
            if not root:
                return
            dt[root.val] = dt.get(root.val,0)+1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        ls = []
        mode_val = max(dt.values())
        for k,v in dt.items():
            if v==mode_val:
                ls.append(k)
        return ls
