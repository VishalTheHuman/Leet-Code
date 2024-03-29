# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ls = []
        def dfs(root,string = ""):
            string+=chr(97+root.val)
            if root.left is None and root.right is None:
                ls.append(string[::-1])
                return 
            if root.left:
                dfs(root.left,string)
            if root.right:
                dfs(root.right,string)
        dfs(root)
        ls.sort()
        return ls[0]
