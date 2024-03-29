# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stk = []
        def dfs(root):
            if root.left:
                dfs(root.left)
            stk.append(root)
            if root.right:
                dfs(root.right)
            root.left = None
        
        dfs(root)

        for i in range(1,len(stk)):
            stk[i-1].right = stk[i]

        return stk[0]
